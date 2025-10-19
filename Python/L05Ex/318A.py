n = int(input())
arr = list(map(int, input().split()))

l, r = 0, n - 1
sereja = 0
dima = 0
turn_sereja = True

while l <= r:
    if arr[l] > arr[r]:
        pick = arr[l]
        l += 1
    else:
        pick = arr[r]
        r -= 1

    if turn_sereja:
        sereja += pick
    else:
        dima += pick

    turn_sereja = not turn_sereja

print(sereja, dima)
