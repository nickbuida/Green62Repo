n = int(input())

original = n
reversed_num = 0

while n > 0:
    digit = n % 10          
    reversed_num = reversed_num * 10 + digit  
    n = n // 10             

if original == reversed_num:
    print("YES")
else:
    print("NO")
