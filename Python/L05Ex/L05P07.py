n = int(input())
arr = list(map(int, input().split()))
flag = True
if n % 2 != 0:
    print("NO")
else:
    count_zeros = 0
    count_ones = 0
    for x in arr:
        if x == 0:
            count_zeros += 1
        if x == 1:
            count_ones += 1
        if count_zeros > len(arr)/2 or count_ones > len(arr)/2:
            print("NO")
            break
    else:
        print("YES")
        

