n = int(input())

max_ = -1
count = 0

for i in range(n):
    a,b = map(int,input().split(" "))
    count -= a
    count += b
    
    if max_ < count:
        max_ = count

print(max_)
