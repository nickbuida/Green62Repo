n = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(n - 1): 
    if arr[i] + 1 != arr[i+1]:
        print(arr[i] + 1)
        break  
else:
    print (arr[n -1] + 1)
