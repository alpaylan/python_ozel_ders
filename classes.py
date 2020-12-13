
# class MyComplex2:
#     def __init__(self):
#         self.real = 0
#         self.imag = 0
#
#     def __str__(self):
#         return '(' + str(self.real) + '+' + str(self.imag) + 'j)'
#
# c01 = MyComplex2()
# c01.real = 3
# c01.imag = 5

# print(c0.real)
# print(c0.imag)

class MyComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return '(' + str(self.real) + '+' + str(self.imag) + 'j)'

    def add(self, other_complex):
        new_real = self.real + other_complex.real
        new_imag = self.imag + other_complex.imag

        return MyComplex(new_real, new_imag)

    def add_real(self, other_real):
        new_real = self.real + other_real
        new_imag = self.imag

        return MyComplex(new_real, new_imag)

    def copy(self):
        return MyComplex(self.real, self.imag)

c0 = MyComplex(3, 5)
cn = c0.copy()
c0.imag = 2
print(c0)
print(cn)

c1 = MyComplex(2, 4)
print(c1)

c2 = c0.add(c1)
print(c2)

c3 = c0.add_real(6)
print(c3)

# print('(' + str(c2.real) + '+' + str(c2.imag) + 'j)')


# Point Class (Cartesian x,y)
# Add
# Sub
# Magnitude
# Reflect
# Manhattan Distance
# Euclidian Distance

# Write a code
# decides if a point is in a function
# f(x) = y
# p = (x0, y0)
# print yes if f(x0) = y0

# Write a code
# decides if all points are in a function
# f(x) = y
# p = [(x0, y0), (x1, y1)...(xn, yn)]
# print yes if f(x0) = y0 and f(x1) = y1 ... and f(xn) = yn


# a = input()
# i = int(input())
# 
# j = input()
# i = int(j)
# f = float(j)

# j = input("Give me an integer")
# print("Give me an integer")
# j = input()



