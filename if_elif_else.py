
b0 = 5 == 5  # True
b1 = bool([])


age = 22
cond1 = age < 20
cond2 = age >= 20

if cond1:
    print('Don\'t rent a car')
else:   # if not cond1:
    print('Rent a car')
# ...

price = 100
balance = 80
cond3 = balance >= price

if cond1:
    print('Don\'t rent a car')
else:   # if not cond1:
    print('Can rent a car')
    if cond3:
        print('Rented the car')
    else:
        print('Can\'t rent the car because he doesn\'t have money')


AA = 90
BB = 80
CC = 70
DD = 60
grade = 75

if grade >= AA:
    print('AA')
else:  # grade < AA(90)
    if grade >= BB:
        print('BB')
    else:  # grade < BB(80)
        if grade >= CC:
            print('CC')
        else:  # grade < CC(70)
            if grade >= DD:
                print('DD')
            else:  # grade < DD(60)
                print('FF')


if grade >= AA:
    print('AA')
elif grade >= BB:
    print('BB')
elif grade >= CC:
    print('CC')
elif grade >= DD:
    print('DD')
else:
    print('FF')





"""
b0 -> True  => l0.append(5)
b0 -> False => go beyond

l0.append(5) sadece b0 doğruysa yap

"""
