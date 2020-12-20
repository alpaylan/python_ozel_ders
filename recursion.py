# recursion -> self-calling function

# fib = 0, 1, 1, 2, 3, 5, 8
# fib(n) = fib(n-1) + fib(n-2)
# fib(n - 1) = fib(n-2) + fib(n-3)
# fib(n - (n - 1)) = fib(1) = 0
# fib(n - (n - 2)) = fib(2) = 1
# fib(n - (n - 3)) = fib(3) = fib(3 - 1) + fib(3 - 2) = 0 + 1 = 1
def fib(n):
    # Base Case
    if n <= 1:
        return 0
    if n == 2:
        return 1
    # Recursive Case
    else:
        return fib(n - 1) + fib(n - 2)

# fib(5)
# fib(4) + fib(3)
#   f4= fib(3) + fib(2)
#       f3= fib(2) + fib(1)
#           f2 = 1
#           f1 = 0
#       f3 = 1
#       f2 = 1
#   f4 = 2
#   fib(2) + fib(1)
#       1
#   3

# lmin(1, 5, 7, 9, 0)
#   1
#   lmin(5, 7, 9, 0)
#       5
#       lmin(7, 9, 0)
#           7
#           lmin(9, 0)
#               9
#               lmin(0)
#                   0


def l_min_it(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i

    return min

minimum_of_list = l_min_it([3, 7, 1, 9, 8])


# list = elem|rest
# list = [3, 7, 1, 9, 8]
# list = 3 | [7, 1, 9, 8]
# l_min([3, 7, 1, 9, 8])
#   if 3 < l_min([7, 1, 9, 8]):
#       then return 3
#   else return l_min([7, 1, 9, 8])
# l_min([7, 1, 9, 8])
#   if 7 < l_min([1, 9, 8]):
#       then return 7


def l_min(l):
    # Base Case
    if len(l) == 1:
        return l[0]
    # Recursive Case
    f_elem = l[0]
    r_min = l_min(l[1:])

    if f_elem > r_min:
        return r_min
    else:
        return f_elem



def l_search_it(l, x):
    for i in l:
        if i == x:
            return True

    return False


def l_search2(l, x):
    # Base Case
    if len(l) == 1:
        if l[0] == x:
            return True
        else:
            return False
    # Recursive Case
    if l[0] == x:
        return True
    else:
        return l_search2(l[1:], x)

def l_search(l, x):
    # Base Case
    if len(l) == 1:
        return l[0] == x

    # Recursive Case
    f_elem = l[0]
    r_list = l[1:]
    if f_elem == x:
        return True
    else:
        return l_search(r_list, x)


# cetvel(1)
# 1
# cetvel(2)
# 121
# cetvel(3)
# 1213121
# cetvel(4)
# 121312141213121
# cetvel(5)
# 1213121412131215121312141213121
def cetvel(n):
    if n == 1:
        return "1"

    return cetvel(n-1) + str(n) + cetvel(n-1)

print(cetvel(4))
