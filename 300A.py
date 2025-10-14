# n = int(input())
# a = list(map(int, input().split()))

# neg = [x for x in a if x < 0]
# pos = [x for x in a if x > 0]
# zeros = [x for x in a if x == 0]

# if len(neg) % 2 == 0:
#     zeros.append(neg.pop())

# if not pos:
#     pos.append(neg.pop())
#     pos.append(neg.pop())

# print(len(neg), *neg)
# print(len(pos), *pos)
# print(len(zeros), *zeros)

n = int(input())
a = list(map(int, input().split()))

neg = []
pos = []
zeros = []

# put numbers into 3 groups
for x in a:
    if x < 0:
        neg.append(x)
    elif x > 0:
        pos.append(x)
    else:
        zeros.append(x)

# make sure first group has product < 0
if len(neg) % 2 == 0:
    x = neg.pop()     # take one negative number out
    zeros.append(x)   # move it to zeros

# make sure second group has product > 0
if len(pos) == 0:
    x1 = neg.pop()    # take one negative
    x2 = neg.pop()    # take another negative
    pos.append(x1)
    pos.append(x2)

# print the results
print(len(neg), *neg)
print(len(pos), *pos)
print(len(zeros), *zeros)
