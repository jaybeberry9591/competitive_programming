s = input()
flag = 0
count = 0
for i in s:
    if i == '4' or i == '7':
        count += 1
#         continue
        
#     else:
#         flag = 1
#         break
        
        
# if flag == 1:
#     print("NO")
# else:
#     print("YES")

if count == 4 or count == 7 :
    print("YES")
else: 
    print("NO")
