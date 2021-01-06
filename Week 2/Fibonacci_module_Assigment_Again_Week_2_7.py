
def fib(j,n,m):
    if n==0:
        return 0
    sum3=0
    sum1=1
    sum2=1
    ind1=[0,1]
    for i in range(n-1):
        sum2=(sum3+sum1)%m
        if i>1 and sum2 ==0 and sum1==1:  
            if n%(i+2)+1>=j%(i+2): 
                return sum(ind1[j%(i+2):n%(i+2)+1])%m 
            else:
                ind1[n%(i+2)+1:j%(i+2)]=[]
                return sum(ind1)%10
        ind1.append(sum2)
        sum3=sum1%m
        sum1=sum2%m
    return sum(ind1[j:])%10
data=list(map(int, input().split()))



print(fib(data[0],data[1],10))
