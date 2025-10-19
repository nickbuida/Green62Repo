x = int(input())
steps = 0

if x % 5 == 0:
    steps = x // 5
else:
    steps = x // 5 + 1
print(steps)