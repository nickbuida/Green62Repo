n = int(input())
arr = list(map(int, input().split()))

max_val = -1
min_val = 1001

max_idx = 0
min_idx = 0

for i in range(n):
    if arr[i] > max_val:
        max_val = arr[i]
        max_idx = i
    if arr[i] <= min_val:
        min_val = arr[i]
        min_idx = i

# Number of swaps:
# Move max to front: max_idx swaps
# Move min to back: (n - 1 - min_idx) swaps
# If min is before max, one step less because shifting max first moves min right
steps = max_idx + (n - 1 - min_idx)
if min_idx < max_idx:
    steps -= 1

print(steps)
