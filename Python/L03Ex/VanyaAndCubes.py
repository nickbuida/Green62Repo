n = int(input())
height = 0
cubes = 0
while cubes <= n:
    height += 1
    cubes += height * (height + 1) // 2
print(height - 1)
