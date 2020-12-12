l0 = list()
l1 = []
l2 = [3, 5, 7, 9]

# Indexing
# 0 indexed
# [ 3 , 5 , 7 , 9 ]
# | 0 | 1 | 2 | 3 |
# |-4 |-3 |-2 |-1 |
# len(li) - 1 = 3

print(l2[1])
print(l2[-3])

# Length
len(l2)
print(len(l2))


# Printing List
print(l2)

# Appending element to end of the list
l2.append(11)
print(l2)

# Inserting an element to middle of the list
l2.insert(0, -1)
print(l2)

# List Concatenation
l3 = [13]
l2 = l2 + l3
print(l2)

# Pop Last Element from List
l2.pop()
print(l2)

# Pop An Index From List
l2.pop(2)
print(l2)

# Remove a value from list
l2.remove(7)
print(l2)

# Backward Indexing
print("l2[-1]: ", l2[-1])

# Sorting List
l2.insert(0, 10)
print(l2)
print("Before Sort: ", l2)
l2.sort()
l2 = sorted(l2)
print("After Sort: ", l2)
l2.sort(reverse=True)
print("After Reverse Sort: ", l2)

print("Last List: ", l2)
print(sorted(l2))
print(l2)

# [3,  5,  7,  9]
# |0  |1  |2  |3 |
# |-4 |-3 |-2 |-1|

