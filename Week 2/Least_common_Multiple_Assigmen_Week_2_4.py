def gcd(k,m):
    n=[k,m]
    n.sort()
    
    if n[1]%n[0]==1:
        return 1
    elif n[1]%n[0]==0:
        return n[0]
    else:
        return gcd(n[0],n[1]%n[0])
data=list(map(int, input().split()))

print(data[0]*data[1]//gcd(data[0],data[1]))
