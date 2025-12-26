def fib(limit):
    a=0;b=1
    print(a)
    print(b)
    while True:
        c=a+b
        a=b
        b=c
        if c<=limit:
            print(c)
        else:
            return
limit=int(input("set the limit:-"))
fib(limit)