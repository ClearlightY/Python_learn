from operator import itemgetter
# 高阶函数: sorted

print(sorted([36, 12, 43, -8]))

print(sorted([35, 12, 43, -13], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(L[0][0])


def by_name(t):
    return t[0]


def by_score(t):
    return -t[1]


L2 = sorted(L, key=by_name)
print(L2)

L2 = sorted(L, key=by_score)
print(L2)


students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
