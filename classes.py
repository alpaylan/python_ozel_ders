
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

# Object Oriented Programming Paradigm
# Imperative Programming Paradigm
# Functional Programming Paradigm
# Logical Programming Paradigm
# Concurrent Programming Paradigm
# OOP
# Objects, Attributes, Relations and Engagements
# Kalem: Ömür, Uzunluk, Yazabildiği Yüzeyler
# Tükenmez Kalem, Kurşun Kalem
# İnsan
# İnsan: Öğrenci, Hemşire, Polis, Mühendis
# Öğrenci: Lise, Üniversite
# Üniversite: Beşeri, Mühendislik
# Mühendislik: EE, CENG

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

    def __add__(self, other_complex):
        new_real = self.real + other_complex.real
        new_imag = self.imag + other_complex.imag

        return MyComplex(new_real, new_imag)

    def __sub__(self, other):
        new_real = self.real - other.real
        new_imag = self.imag - other.imag

        return MyComplex(new_real, new_imag)

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5

    def __bool__(self):
        return True

    def add_real(self, other_real):
        new_real = self.real + other_real
        new_imag = self.imag

        return MyComplex(new_real, new_imag)

    def copy(self):
        return MyComplex(self.real, self.imag)


c0 = MyComplex(3, 5)
# MyComplex(c0, 3, 5)
print(c0)

c1 = MyComplex(2, 4)
print(c1)

c2 = c0.add(c1)
print(c2)

c3 = c0.add_real(6)
print(c3)

c4 = c0 + c1
print(c4)


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



