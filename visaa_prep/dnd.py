N,m =map(int,input().strip().split())
arr=list(map(int, input().strip().split()))
n1=0
n2=0
for n in arr:
    if n % m==0:
        n2 += n
    else:
        n1 += n
print(n2-n1)
