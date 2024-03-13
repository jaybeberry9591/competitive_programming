n,h = map(int,input().split(" "))
s = input()
s_list = s.split(" ")

count = 0

for i in s_list:
    if int(i) > h:
        count += 2
    else :
        count += 1
        
print(count)
