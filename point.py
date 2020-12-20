from math import inf

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5

    def manhattan_dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def euclidian_dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5


class LinearFunction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # f(x) = y = a*x + b

    def point_belong(self, p: Point):
        if p.y == self.a * p.x + self.b:
            return True
        else:
            return False

    def is_parallel(self, other):
        return self.a == other.a

    def intersection(self, other):
        if self.is_parallel(other):
            return inf
        # f(x) = ax + b
        # g(x) = cx + d
        # ax + b = cx + d
        # x = (d-b)/(a-c)
        # y = cx + d
        x_new = (other.b - self.b)/(self.a - other.a)
        y_new = other.a*x_new + other.b
        return Point(x_new, y_new)


lf = LinearFunction(3, 5)
lf2= LinearFunction(3, 10)
p = Point(0, 2)
p2 = Point(3, 7)
p3 = p + p2

print(lf.point_belong(p))
print(lf.intersection(lf2))


class QuadraticFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # f(x) = ax^2 + bx + c

    def __str__(self):
        str_a = (lambda x: "" if x == 1 else str(x))(self.a)
        str_b = (lambda x: "" if x == 1 else str(x))(self.b)
        str_c = str(self.c)
        return "f(x) = " + str_a + "x^2 + " + str_b + "x + " + str_c




    def discriminant(self):
        # b^2 - 4ac
        return self.b**2 - 4*self.a*self.c

    def roots(self):
        discr = self.discriminant()

        # (-b +- sqrt(discr))/2a
        r1 = (-self.b + discr**0.5)/(2*self.a)
        r2 = (-self.b - discr**0.5)/(2*self.a)

        if discr < 0:
            return None
        elif discr == 0:
            return r1
        else:
            return r1, r2

qf = QuadraticFunction(1, 2, 1)
print(qf)

print(qf.roots())
