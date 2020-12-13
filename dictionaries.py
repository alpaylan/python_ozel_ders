
d0 = dict()
# key -> value
d1 = {}
d2 = {
    1: "alperen",
    2: "serhan",
    "alperen": 3,
    "serhan": 4,
    False: "keles",
    True: d1,

}

# Get value of key
print(d2.get(1))
print(d2[1])
print(d2['alperen'])

print(d2['serhan'] + d2['alperen'])

# d2_serhan = 4
# d2_alperen = 3


# Keys must be hashable
# Hashable means corresponding to a unique number
# Dicts are mutable
# Addable
d2['alperen'] = 5
d2['turan'] = 7

print(d2)

a = 3
b = 3
d3 = {
    a: 3,
}
d4 = {
    # [1, 3]: 5,
    2: 2.5,
    b: 4,
}

# d5 = d3 + d4

# Clear Dictionary
print("prev", d3)
d3.clear()
print("after", d3)

d3 = {
    1: 2,
    3: 4,
    5: 7
}
print(d3)

# Pop Last Item
a = d3.popitem()
print(a)
print(d3)

# Pop Value for given Key
b = d3.pop(1)
print(b)
print(d3)
