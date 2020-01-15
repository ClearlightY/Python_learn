# 高级特性: 切片
L = ['Mike', 'Jerry', 'Bob', 'Luck']

# 1
print([L[0], L[1]])

# 2. 循环
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

# 3. 切片
print('切片')
print(L[0:3])
print(L[:3])
print(L[1:3])
# 倒数第一个元素的索引是 -1
print(L[-2:])
print(L[-2:-1])