def division(a, b):
    while a % b == 0:
        a = a // b
    return a

def ugly(n):
    n = division(n, 2)
    n = division(n, 3)
    n = division(n, 5)
    if n == 1:
        return 1
    else:
        return 0


for i in range(int(input())):
    n = int(input())

    cnt, i = 1, 1

    while cnt < n:
        i += 1
        if ugly(i):
            cnt += 1
    print(i)

    
