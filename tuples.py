t0 = tuple()
t1 = ()
# l0 = [1, 3]
t2 = (3, 5, "alperen", [1, 3])
# t2[2] = 7 is forbidden
l0 = t2[3]
print(t0)
print(t1)
print(t2)
l0[1] = 2
print(t2)

t3 = (3, 5)
t4 = (4, 6)
t5 = (t3, t4)
# t5 = ((3, 5), (4, 6))
t3 = t3 + t4
t3 = (t3[0], t4[1])
# t3 = (3, 6)
print(t5)
print(t3)



t7 = (1, 2, 3, 4, 5)
# t7 =       1     2     3     4     5
# in =       0     1     2     3     4
# sl =    0  |  1  |  2  |  3  |  4  |  5

t8 = (6, 7, 8, 9, 10)
print("t7 slice 0,5,2", t7[slice(0, 5, 2)])

t7 = t7[slice(0, 3)] + t8[slice(2, 5, 1)]
# t7 = (1, 2, 3, 8, 9, 10)


# t8 = (6, 7, 111, 9, 10)


# t8 = list(t8)
# t8[2] = 111
# t8 = tuple(t8)
t8 = (6, 7) + (8, 9, 11)
# t8 = t8[slice(0, 2)] + tuple([111]) + t8[slice(3, 5)]

# slice
# (start, stop, step)
# (0, 5, 2)
# 0, 2, 4
# (0, 5, 3)
# 0, 3

# remove(t0, 5)
# append(t0, 11)
# pop(t0)
# pop(t0, 3)
start = 0
stop = 5
step = 2
print(t8[0:5:2])
print(t8[start:stop:step])
print(t8[     start : stop : step])
print(t8[slice(start, stop, step)])



print(t8)


# Aliasing
# (5, 7, 9) -> address = 100
# a = 100
# b = a = 100
# a[0:2] = (5, 7, 9) -> address = 200
# a = 200

a = (5, 7, 9)
b = a
print(a)
print(b)
a = a[0:2]
print(a)
print(b)


print("#########")
a1 = [  5  ,  7  ,  9]
#    0  |  1  |  2  |  3
b1 = a1
print(a1)
print(b1)
a1 = a1[0:2]
a1[0] = 2
print(a1)
print(b1)
print("#########")

a2 = [5, 7, 9]
b2 = a2
print(a2)
print(b2)
a2[2] = 4
a2.append(5)
a2.pop(1)
print(a2)
print(b2)

a3 = [5, 7, 9]
b3 = a3
print(a3)
print(b3)
a3 = tuple(a3)
# a3 = a3.copy()
a3 = list(a3)
a3.append(10)
print(a3)
print(b3)

# [5, 7, 9] -> address = 100
# a_list -> 100
# b_list -> a_list -> 100
# address = 100_list [2] = 4
# [5, 7, 4] -> address = 100


# [5, 7, 9] -> address = 100
# a_list -> 100
# b_list -> a_list -> 100
# [5, 7] -> address = 200
# a_list -> 200
# b_list -> 100
# [5, 7, 9] -> address = 100
# [5, 7] -> address = 200


