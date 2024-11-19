x,y,z=map(int,input().split())
req_time=x*y
avail_time = z*24*60
if req_time >= avail_time:
    print("NO")
else:
    print("YES")
