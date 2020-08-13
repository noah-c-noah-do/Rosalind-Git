# Fn = F(n-1) + k*F(n-2)
n = int(input())    # number of months examined
k = int(input())    # rabbit reproduction rate
a = 0
b = 1
c = 0
rabbits = 0
month = 1


while month < n:
    # print(f'{rabbits} rabbits in month {month}')
    c = k * a + b
    a = b
    b = c
    print(f'{c} rabbits in month {month}')
    month += 1
    rabbits = c
