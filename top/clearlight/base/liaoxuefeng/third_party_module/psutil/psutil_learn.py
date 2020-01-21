import psutil

# 获取CPU逻辑数量
print(psutil.cpu_count())
# CPU物理核心 : 2说明是双核超线程, 4则是4核非超线程
print(psutil.cpu_count(logical=False))

# 统计CPU的用户/系统/空闲时间
print(psutil.cpu_times())

# 实现类似top命令的CPU使用率
for x in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))

# 获取内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 获取磁盘信息
# 磁盘分区信息
print(psutil.disk_partitions())
# 磁盘使用情况
print(psutil.disk_usage('/'))
# 磁盘IO
print(psutil.disk_io_counters())

# 获取网络信息
# 获取网络读写字节/包的个数
print(psutil.net_io_counters())
# 获取网络接口信息
print(psutil.net_if_addrs())
# 获取网络接口状态
print(psutil.net_if_stats())
# 获取网络连接信息
print(psutil.net_connections())

# 获取进程信息
# 所有进程ID
print(psutil.pids())
# 进程名称
p = psutil.Process(17628)
print(p.name())
# 进程exe路径
print(p.exe())
# 进程工作目录
print(p.cwd())
# 进程启动的命令行
print(p.cmdline())
# 父进程ID
print(p.ppid())
# 父进程
print(p.parent())
# 子进程列表
print(p.children())
# 进程状态
print(p.status())
# 进程用户名
print(p.username())
# 进程创建时间
print(p.create_time())
# 进程终端
# print(p.terminal())
# 进程使用CPU的时间
print(p.cpu_times())
# 进程使用的内存
print(p.memory_info())
# 进程打开的文件
print(p.open_files())
# 进程相关网络连接
print(p.connections())
# 进程的线程数量
print(p.num_threads())
# 所有进程信息
print(p.threads())
# 进程环境变量
print(p.environ())
# 结束进程
# p.terminate()

# test()函数: 模拟出ps命令的效果
psutil.test()