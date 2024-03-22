test = int (input())

for i in range (test):
    b,c,k = map(int,input().split(" "))
    b_str = input()
    c_str = input()
    
    count = 0
    
    b_list = list(b_str.split(" "))
    c_list = list(c_str.split(" "))
    
#     print (b_list,c_list)

    for bi in b_list:
        for ci in c_list:
            if int(bi) + int(ci) <= k:
                count += 1
    
    print(count)
