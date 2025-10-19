prevPot = 0
flag = True
while True:
    n = int(input())
    if n == 0:   
        break
    if n > prevPot:
        prevPot = n
    else:       
        flag = False
if flag:
    print("YES")
else:
    print("NO")
