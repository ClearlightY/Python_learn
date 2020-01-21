def BubbleSort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                (lst[j], lst[j + 1]) = (lst[j + 1], lst[j])
    return lst


x = input("请输入待排序数列:\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = BubbleSort(arr)
print('数列排序如下:')
for i in arr:
    print(i, end=' ')

x, y = 1, 2
print(x, y, end=' ')
print('adsf')
