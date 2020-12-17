b0 = bool()
b1 = bool(True)
b2 = bool(False)
b3 = bool(1)  # True
b4 = bool(0)  # # False
b5 = bool(-1)  # True
b6 = bool(2)  # True
b7 = True
b8 = False

# 0 -> False
# else -> True

# print(b0)
# print(b1)
# print(b2)
# print(b3)
# print(b4)
# print(b5)
# print(b6)

## Comparison Ops
# ==, !=
# b9  = 5 == 5
# b10 = 5 == 7
# print(b9)
# print(b10)

b11 = (5 != 5)  # False
b12 = (5 != 7)  # True
# print(b11)
# print(b12)
# <, <=, >, >=

b13 = 5 < 5
b14 = 5 <= 5
b15 = 5 > 5
b16 = 5 >= 5

# print(b13)
# print(b14)
# print(b15)
# print(b16)

# Logical Ops
# and, or, xor, not
b17 = True
b18 = False
b19 = not 5 == 5 or b17 and b18 and True and False
# b19 = (True or True) and False and True and False
# b19 = (True and False) and True and False
# b19 = (False and True) and False
# b19 = (False and False)
# b19 = False
# Precedence Table
# b19 = not 5 == 5 or b17 and b18 and True and False
# b19 = not True or True and False and True and False
# b19 = False or True and False and True and False
# b19 = False or False and True and False
# b19 = False or False and False
# b19 = False or False
# b19 = False
# not > and > or
print("b19", b19)

b19_ = b17 & b18
b20 = b17 or b18
b20_ = b17 | b18
b21 = b17 ^ b18

# print(b17)
# print(b18)
print(b19)
# print(b19_)
# print(b20)
# print(b20_)
# print(b21)


# bx = (a = 5) | (b = 7) -> forbidden

# Statement vs Expression
# Expressions have values
# a = expr
# Statements don't have values
# a = statement (x)
# Assignment is a statement
