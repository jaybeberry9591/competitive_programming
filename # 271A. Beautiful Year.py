n = int(input())

# a = n % 10;
# b = n % 100; 
# c = n % 1000;

# d = int(n / 10);
# e = int(n / 100);
# f = int(n /1000);

# print(a,b,c,d,e,f)

while n != 0:
    
    n += 1
    a = int(n / 1000)
    b = int(n / 100 % 10)
    c = int(n / 10 % 10)
    d = int(n % 10)
#     print(n,a,b,c,d)
    if ( a != b and b!= c and c!= d and d != a and d != b and a != c ):
        
        break;
print(n)
