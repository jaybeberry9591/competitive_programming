k,n,w = map (int, input().split(" "))

total = int((w*(w+1))/2) * k

if total-n > 0:
    
    print(abs(n-total))

else: 
    print(0)
