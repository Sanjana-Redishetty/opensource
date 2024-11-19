def rev_int(n):
    sign = -1 if n<0 else 1
    rev_num = int(str(abs(n))[::-1])
    rev_num *= sign
    if rev_num <-2**31 or rev_num > 2**31-1:
        return 0
    return rev_num
n=int(input().strip())
print(rev_int(n))
