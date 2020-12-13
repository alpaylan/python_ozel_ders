s0 = str()
s1 = ""
s2 = "alperen"
s3 = 'alperen'
s4 = 'sErhan' + ' ' + 'turan'
s5 = ['s', 'e', 'r', 'h', 'a', 'n']

print(s4)

s6 = s4.capitalize()
print(s6)
s7 = s4.find("rh", 0, 10)
print(s7)
s8 = s4.count('an', 0, 10)
print(s8)
b9 = s4.isdigit()

# identifier <-> variable name
# alphanum: a..z A..Z 0..9
# digit: 0..9

b10 = s4.isalnum()

# strings are immutable
# s4[3] = 'l' -> is forbidden
# slicing is possible
