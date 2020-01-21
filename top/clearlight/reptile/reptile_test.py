import requests, json, os, threading, time, logging
from bs4 import BeautifulSoup
from multiprocessing import Process, Queue
from multiprocessing.queues import Empty
from urllib.request import urlretrieve

# 首先在f盘新建一个img文件夹, 用来保存图像

logging.basicConfig(level=logging.ERROR, filename='failed_img.log')

# 抓取地址
answers_url = 'https://www.zhihu.com/api/v4/questions/29815334/answers?data[*].author.follower_count%2Cbadge[*].topics=&data[*].mark_infos[*].url=&include=data[*].is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled&limit=5&offset=0&platform=desktop&sort_by=default'

# 待下载图片队列
img_queue = Queue()
# 下载图片失败队列
bad_queue = Queue()

# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Host': 'www.zhihu.com'
}

'''
请求知乎回答数据
:param answers_url: 知乎问题的第一个回答请求地址
:param imgq: 待下载图片队列
:param count: 递归结束标识，用于判断是否最后一页
:return: 
'''


def getR(answers_url, imgq, count=0):
    while True:
        try:
            r = requests.get(answers_url, headers=headers)
        except BaseException:
            continue
        else:
            rj = str(r.json()).replace("True", "\"true\"").replace("False", "\"false\"")
            rj = json.loads(json.dumps(eval(rj)))

            for x in rj['data']:
                content = x['content']
                soup = BeautifulSoup(content, 'lxml')
                # 查找img标签并且class属性等于origin_image zh-lightbox-thumb的元素
                for img in soup.find_all('img', attrs={'class': 'origin_image zh-lightbox-thumb'}):
                    # 保存图片到img_queue队列
                    imgq.put(img['data-original'])
                    print('保存%s到img_queue' % os.path.split(img['data-original'])[1])
            if rj['paging']['is_end'] != 'true':
                answers_url = rj['paging']['next']
            else:
                print('request_pro 执行完毕')
                # 最后一页
                break


'''
下载进程：分别创建四个线程，用于下载图片
:param imgq:    待下载图片队列
:param badq:    下载图片失败队列
:param pname:   进程名称
:return: 
'''


def download_pro(imgq, badq, pname):
    # 这里设置name可用于区分是哪个进程的哪个线程
    t1 = threading.Thread(target=download, args=(imgq, badq), name='%s - 下载线程1' % pname)
    t2 = threading.Thread(target=download, args=(imgq, badq), name='%s - 下载线程2' % pname)
    t3 = threading.Thread(target=download, args=(imgq, badq), name='%s - 下载线程3' % pname)
    t4 = threading.Thread(target=download, args=(imgq, badq), name='%s - 下载线程4' % pname)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()


'''
下载图片函数
:param imgq:    待下载图片队列
:param badq:    下载图片失败队列
:return: 
'''


def download(imgq, badq):
    thread_name = threading.current_thread().name
    while True:
        try:
            # 设置timeout=10,10秒后队列都拿取不到数据，那么数据已经下载完毕
            c = imgq.get(True, timeout=10)
            name = os.path.split(c)[1]
        except Empty:
            print('%s 执行完毕' % thread_name)
            # 退出循环
            break
        else:
            imgcontent = requests.get(c)
            ''' 图片请求失败,将图片地址放入bad_queue,等待bad_pro处理'''
            if imgcontent.status_code != 200:
                print('%s 下载%s失败' % (thread_name, name))
                badq.put(c)
                continue
            with open(r'F:\img\%s' % name, 'wb') as f:
                f.write(imgcontent.content)
                print('%s 下载%s成功' % (threading.current_thread().name, name))


'''
创建四个线程用于尝试bad_queue队列中的图片，
:param badp: bad_queue
:return: 
'''


def again_pro(badq):
    b1 = threading.Thread(target=again_download, args=(badq,), name='重下线程1')
    b2 = threading.Thread(target=again_download, args=(badq,), name='重下线程2')
    b3 = threading.Thread(target=again_download, args=(badq,), name='重下线程3')
    b4 = threading.Thread(target=again_download, args=(badq,), name='重下线程4')

    b1.start()
    b2.start()
    b3.start()
    b4.start()


'''
尝试重复下载bad_queue队列中的图片
:param badq: bad_queue
:return: 
'''


def again_download(badq):
    while True:
        c = badq.get(True)
        name = os.path.split(c)[1]
        # 尝试重复下载5次，如果5次均下载失败，记录到错误日志中
        for x in range(5):
            try:
                # 个人感觉使用urlretrieve下载的成功率要高些，哈哈^_^
                urlretrieve(c, r'F:\img\%s' % name)
            except BaseException as e:
                if x == 4:
                    logging.error('%s 重复下载失败,error：[%s]' % (c, repr(e)))
                # 下载失败; 再次尝试
                continue
            else:
                # 下载成功；跳出循环
                print('%s 在第%s次下载%s成功' % (threading.current_thread().name, (x + 1), name))
                break


'''
监听器，用于关闭程序，10秒刷新一次
:param imgq: img_queue
:param badq: bad_queue
:return: 
'''


def monitor(imgq, badq):
    while True:
        time.sleep(10)
        if imgq.empty() and badq.empty():
            print('所有任务执行完毕，40秒后系统关闭')
            count = 39
            while count > 0:
                time.sleep(1)
                print('距离系统关闭还剩：%s秒' % count)
                count -= 1
            break


if __name__ == '__main__':
    # 请求数据进程
    request_pro = Process(target=getR, args=(answers_url, img_queue))

    ''' 下载图片进程[first]和[second] '''
    download_pro_first = Process(target=download_pro, args=(img_queue, bad_queue, 'download process first'))
    download_pro_second = Process(target=download_pro, args=(img_queue, bad_queue, 'download process second'))

    # 处理[first]和[second]进程下载失败的图片
    bad_pro = Process(target=again_pro, args=(bad_queue,))
    bad_pro.daemon = True

    # req_pro进程启动
    request_pro.start()
    print('3秒之后开始下载 >>>>>>>>>>>>>>>')
    time.sleep(3)

    # first 和 second 进程启动
    download_pro_first.start()
    download_pro_second.start()

    # 重复下载进程启动
    bad_pro.start()

    # 监听线程：判断系统是否退出
    request_pro.join()
    print('监听线程启动 >>>>>>>>>>>>>>>')
    sys_close_t = threading.Thread(target=monitor, args=(img_queue, bad_queue,))
    sys_close_t.start()
