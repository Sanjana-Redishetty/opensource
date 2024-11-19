def fact(n):
    if n==0:
        return 1
    result=1
    for i in range(1,n+1):
        result *= 1
    return n*fact(n-1)
n = int(input())
if 1<=n<=15:
    print(fact(n))
else:
    print("1")
