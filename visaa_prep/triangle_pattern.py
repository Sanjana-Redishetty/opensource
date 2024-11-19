n=int(input().strip())
curr_no=1
for i in range(1,n+1):
    for j in range(i):
        print(curr_no,end=" ")
        curr_no+=1
    print()
