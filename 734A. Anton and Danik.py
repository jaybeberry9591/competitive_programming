n = input()
s = input()

count_a = 0
count_d = 0

for i in s :
    if i == "A":
        count_a += 1
    elif i == "D":
        count_d += 1

if count_a > count_d :
    print("Anton")
elif count_a < count_d :
    print("Danik")
else:
    print("Friendship")
