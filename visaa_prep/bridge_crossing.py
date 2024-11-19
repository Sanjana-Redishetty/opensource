a,b,c=map(int,input().split())
max_man_wt=c-b
if max_man_wt <=0:
    max_man=0
else:
    max_man = max_man_wt // a
print(max_man)
