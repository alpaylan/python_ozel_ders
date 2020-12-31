
def div(x, y):
    try:
        return x/y
    except NameError:
        print("Name Error")
        return -1
    except ZeroDivisionError:
        print("Zero Division Error")
        return -2

def f(x):
    try:
        raise Exception("garip error")
    except:
        print("Çözeriz")


def mydiv(x, y):
    if y == 0:
        raise Exception("sıfıra bölme")
    else:
        return x/y


print(mydiv(5, 0))
print("Bye")

# try:
#     print(mydiv(5, 0))
# except:
#     print("Bölemedik")

# print(div(5, 0))
# print("Bye")

