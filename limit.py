# f(x): x -> a lim f(x)


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

    def compute(self, x):
        return x**2*self.a + x*self.b + self.c

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

class FractionalFunction:
    def __init__(self, nominator: QuadraticFunction, denominator: QuadraticFunction):
        # f(x) = g(x)/h(x)
        self.nom = nominator
        self.den = denominator
        self.eps = 10**-9

    def rlimit(self, x):
        return self.compute(x + self.eps)

    def llimit(self, x):
        return self.compute(x - self.eps)

    def compute(self, x):
        return self.nom.compute(x)/self.den.compute(x)

    def deriv(self, x):
        return (self.compute(x + self.eps) - self.compute(x))/self.eps

"""
Maths
1 - Find roots of nominator
2 - Finds roots of denominator
3 - If denominator has no roots
    Then no problems
4 - If denominator has roots that does not collide with nominator roots
    Then Inf or -Inf
5 - If roots are colliding
    Then L'Hospital and calculate
Scientific Computing
get real close


|
|
|
|    ***    ***
|   *   *  * 
|  *     ** 
|______________________
"""


qf1 = QuadraticFunction(1, 2, 1)
qf2 = QuadraticFunction(1, 3, 2)
ff = FractionalFunction(qf1, qf2)

# ff = (x^2 + 2x + 1)/(x^2 + 3x + 2)
# ff = (2x + 2)/(2x + 3)

print(ff.rlimit(-1))


# f(x + h) - f(x)
# ---------------
#        h

