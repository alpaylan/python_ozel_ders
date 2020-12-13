# loops
# Iterative Control Structure/Backward Branch

# for
# for <identifier> in <iterable>:
#   statement0
#   statement1
#   ...
#   statementn

# <iterable>: Container Types
# <iterable>: List, Tuple, Dict, Set, String, Range
# <identifier>: a placeholder
# Containers are collections of items
# A placeholder travels through this collection
l0 = [1, 3, 5, 7]
for i in l0:
    print(i)

i = l0[0]
print(i)

i = l0[1]
print(i)

i = l0[2]
print(i)

i = l0[3]
print(i)

# len(l0) = 4
# range(4) = (0, 1, 2, 3)

print(tuple(range(0, len(l0))))

for i in range(len(l0)):
    j = l0[i]
    print(j)

i = 0
j = l0[i]
print(j)

j = l0[1]
print(j)

j = l0[2]
print(j)

j = l0[3]
print(j)

for s in "alperen":
    print(s)

for t in (3, "alp", 'k', False):
    print(t)

d0 = {
    1: "a",
    2: 'b',
    3: 'c'
}

for d in d0.items():
    print(d)

for (k, v) in d0.items():
    print(v)

s0 = {1, 2, 4, 'a'}

for s in s0:
    print(s)


# while

# while <cond>:
#   s0
#   s1
#   ...
#   sn

# cond = 5 == 5
#
# while cond:
#     alp = 2


i = 0
while i < 5:
    print(i)
    i = i + 1


# continue
i = 0
while i < 5:  # ...
    if i == 3:
        i = i + 1
        continue
    print(i)
    i = i + 1

# break
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i = i + 1
# ...

i = 0
while True:
    if i >= 5:
        break
    print(i)
    i = i + 1
# ...

print("#########")
for i in range(5):
    print(i)
    i = i + 1
    print(i)
print("#########")

i = 0
while True:
    if i >= 5:
        break

    print(i)

    i = i + 1

i = 0
while i < 5:
    print(i)
    i = i + 1

for i in range(5):
    print(i)


l5 = [3, 4, 5]

for i in l5:
    print(i)

for j in range(len(l5)):
    print(l5[j])
