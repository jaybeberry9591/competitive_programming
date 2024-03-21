test_cases = int(input())

for i in range (test_cases):
    a,b,c = map(int, input().split(" "))
    ans = a
    r = b % 3 
    
    if r == 0:
        e = int (b/3)
        ans = ans+ e
        if (c % 3 == 0):
            d = int(c/3)
            ans = ans + d
        else:
            d = int(c/3)
            ans = ans + d + 1
        print(ans)
    
    elif(c>=3-r):
        b+= 3-r
        c-= 3-r
        e = int(b/3)
        ans = ans + e
        if (c%3==0):
            d = int(c/3)
            ans = ans + d
        else:
            d = int(c/3)
            ans = ans + d + 1
        print(ans)
    
    else:
        print (-1)
