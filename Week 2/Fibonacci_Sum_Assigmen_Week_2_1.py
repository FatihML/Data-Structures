def fib(n):
    if n==0:
     return 0
    sum=0
    sum1=1
    sum2=1
    for i in range(n-1):
        sum2=(sum+sum1)
        sum=sum1
        sum1=sum2
    return sum2
print(fib(int(input())))
