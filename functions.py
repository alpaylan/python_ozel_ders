# Name, Domain, Range
# for function f and for d in domain, there exists a r in Range
# such that f(d) = r
# d = (x, y, z, w, t)
# f(x, y) = x + y
# f(r0) = r1
# f(x) = y


# Takes a string, returns the first character as Capslocked
def first_char_capitalized(name):
    return name.capitalize()[0]

r_value = first_char_capitalized("alperen")

# a -> A
# b -> B
# ...
# aa -> A

print(r_value)


# def <function_identifier> (<parameter>, <parameter>..., <parameter>):
#     s0
#     s1
#     ...
#     sn
#     (?) return v

def sqr(x):
    sqr_x = x
    sqr_x = sqr_x * sqr_x
    return sqr_x

x = 5
a = sqr(x)

# f(x) = x*x

def sumlist(l):
    s = 0
    for i in l:
        s = s + i

    l[0] = 5

    return s


def sumlistc(l):
    sumlist_l = l
    s = 0
    for i in sumlist_l:
        s = s + i

    sumlist_l[0] = 5

    return s


def change_first_element_of_list_to_0(l):
    new_l = l.copy()
    new_l[0] = 0
    return new_l

l6 = [3, 5, 7]
l7 = change_first_element_of_list_to_0(l6)

print(l6)
print(l7)

def change_first_element_of_list_to_0_side_effect(l):
    l[0] = 0
    return l

l8 = [3, 5, 7]
l9 = change_first_element_of_list_to_0_side_effect(l8)
print(l8)
print(l9)


def change_first_element_of_list_to_1_modifier(l):
    l[0] = 1

l10 = [3, 5, 7]
change_first_element_of_list_to_1_modifier(l10)
print(l10)

def change_first_element_of_list_to_1_returner(l):
    new_l = l.copy()
    new_l[0] = 1
    return new_l

l11 = [3, 5, 7]
l11 = change_first_element_of_list_to_1_returner(l11)
print(l11)

# primitive types are copied in assignments
# compound and container types are referenced in assignments

def five():
    return 5

# a = five()
# print(a)
# print(five())

def print_5_7_9():
    print("5")
    print("7")
    print("9")




# print("5")
# print("7")
# print("9")
#
# print("5")
# print("7")
# print("9")
#
# print("5")
# print("7")
# print("9")



# print_5_7_9()
# print_5_7_9()
# print_5_7_9()

def f(arr):
    return arr*arr
twentyfive= f(5)

def ff(arr):
    return arr[0]

arr_zero = ff([3, 5, 7])

arr = []
arr = {
    3: 5,
    7: 2
}
arr = (1, 4, 9)
arr = "asdasjdsjal"

F = 7

def fff():
    global F
    # fff_F = F
    # fff_F = fff_F + 1
    F = F + 1
    # fff_F = fff_F + 1
    # F = fff_F
    # return fff_F
    return F

