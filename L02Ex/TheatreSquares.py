n, m, a = map(int, input().split())
nStones = 0
mStones = 0
if n % a == 0:
    nStones = n // a
else:
    nStones = n // a + 1
if m % a == 0:
    mStones = m // a
else:
    mStones = m // a + 1
print(nStones * mStones)