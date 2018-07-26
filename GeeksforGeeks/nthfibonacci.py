def fib(n):
    a = 1
    b = 1
    cnt = 2
    if n == 1 or n == 2:
        return 1

    while cnt != n:
        c = a + b
        a = b
        b = c
        cnt += 1

    return b
    
for i in range(int(input())):
    print(fib(int(input())) % (10 **9 + 7))

