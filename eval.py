
l0 = eval('[2, 5, 7]')
print(type(l0))
print(l0)

i0 = eval('45645')
print(type(i0))
print(i0)

f0 = eval('3.1415926')
print(type(f0))
print(f0)

t0 = eval('(3, 5, 7)')
print(type(t0))
print(t0)

# h0 = eval('(3, 5, 7]')
# print(type(h0))
# print(h0)

print(eval('3+ 5 +7'))

def sqr(sqr_str):
    return eval(sqr_str + '*' + sqr_str)

print(sqr('5'))

def sqr2(sqr_int):
    return eval(str(sqr_int) + '*' + str(sqr_int))

print(sqr2(5))

d0 = {
    1: 2,
}


def f(aa):
 a = 7
 b = 5
 if True:
   c = 7
    # d = 8 is forbidden
