a,b = map(int,input().split(" "))

count = 0
for i in range (6):
    a =  a * 3
    b =  b * 2
    if a > b:
        break
    else :
        count = count + 1
        
        
print(count+1)
