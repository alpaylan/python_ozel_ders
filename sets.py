s0 = set()
s1 = {}
s2 = {1, 3, 5, 7}
s3 = {2, 4, 6, 8}
# Elements must be hashable
s4 = s2.union(s3)
s5 = s2.intersection(s3)
s6 = s4.difference(s3)
s7 = s4.pop()
s4.clear()

b8 = s6.isdisjoint(s2)  # Ayrık
b9 = s6.issubset(s2)
b10 = s6.issuperset(s2)

print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)
print(b8)
print(b9)
print(b10)

