arr = list(map(int, input().split()))
inverse_arr = []

for i in range(len(arr)):
    inverse_arr.append(arr.pop())


print(inverse_arr)