n = int(input())

x_axis = 0 
y_axis = 0
z_axis = 0

for i in range (n):
    x,y,z = map(int, input().split(" "))
    x_axis += x
    y_axis += y
    z_axis += z

if x_axis == 0 and y_axis == 0 and z_axis == 0:
    print("YES")
else:
    print("NO")
