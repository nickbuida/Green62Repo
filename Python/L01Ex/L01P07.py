a, b, c = map(float, input().split())
P = a + b + c
p = P/2
myArea = p*(p-a)*(p-b)*(p-c) 
# S = math.sqrt(myArea)
S = myArea ** 0.5
print (f"{P:.2f} {S:.2f}")