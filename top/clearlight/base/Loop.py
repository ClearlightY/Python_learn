names = ['Mike', 'Bob', 'Luck']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# 从0加到100, 其中range()函数可以生成一个整数序列
i = 0
nums = list(range(101))
print(nums)
for num in nums:
    i = i + num
print(i)

# 上面代码的简化形式
sum = 0
for num in range(101):
    sum += num
print(sum)

# while循环
sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    # print('Hello,', i, '!')
    print('Hello,' + i + '!')

# 通过while打印1-10
n = 1
while n <= 10:
    print(n)
    n += 1
print('END')

n = 1
while n <= 10:
    if n > 3:
        break # break语句会结束当前循环
    print(n)
    n += 1
print('END')

# continue 跳过当前的这次循环
n = 0
while n < 10:
    n += 1
    if n % 2 == 0: # 如果n是偶数, 执行continue语句
        continue # continue语句会直接继续下一轮循环, 后续的print()语句不会执行
    print(n)

