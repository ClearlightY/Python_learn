# dict: 使用键-值存储
d = {'Mike': 90, 'Bob': 70, 'Luck': 100}
print(d['Luck'])

# 最后放入key的value, 将会把前面的值冲掉
d['Mike'] = 98
print(d)

# 避免key不存在的错误
# 1. 通过in判断key是否存在
if 'Mike' in d:
    print(d['Mike'])

# get(): 如果key不存在可以返回None或者返回指定的value, 若存在则返回key对应的value
print(d.get('Bob'))
print(d.get('Blue', -1))
print(d.get('Bob', 99))
print(d.get('Blue'))

# pop(key)方法: 删除一个key, 同时对应的value也会从dict中删除
luck = d.pop('Luck')
print(luck)
print(d)

# set: 是一组key的集合, 但不存储value.
# 没有重复的值, 且set(list)需要提供一个list作为输入集合
# 无序 无重复 的集合
s = set([1, 1, 2, 2, 3, 3])
print(s)

s = {1, 1, 2, 2, 3, 3}
print(s)

# 添加元素
s.add(4)
print(s)
s.add(-12)
print(s)

# 移除元素
s.remove(3)
print(s)

#  &: 交集    |: 并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

l = [1, 1, 2, 2, 3, 3, 4]
s = set(l)
print('s:', s)

s1 = (1, 2, 3)
s2 = (1, [2, 3])
print('s1:', s1)
print('s2:', s2)
# 如果存入set时存在list则会报错, 因为list属于可变(不可hash),因此不能存入s2
d = {s1, s1}
print('d:', d)

# set可以直接用{}定义 等价于 set([])

