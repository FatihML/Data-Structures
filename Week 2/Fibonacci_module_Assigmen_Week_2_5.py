
def fib(n,m):
    if n==0:
        return 0
    sum=0
    sum1=1
    sum2=1
    ind1=[0,1]
    for i in range(n-1):
        sum2=(sum+sum1)%m
        if i>1 and sum2 ==0 and sum1==1:  
            return ind1[n%(i+2)]
        ind1.append(sum2)
        sum=sum1%m
        sum1=sum2%m
    return sum2
data=list(map(int, input().split()))

print(fib(data[0],data[1]))
