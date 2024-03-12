s = input()

upper_count = 0
lower_count = 0

# j = 'i' 
# print(j.isupper())

for i in s:
#     print(i)
    if i.isupper() == True:
        upper_count += 1
#         print(upper_count)
    else:
        lower_count += 1
        
# print(lower_count, upper_count)
if lower_count >= upper_count:
    print(s.lower())
else: 
    print(s.upper())
