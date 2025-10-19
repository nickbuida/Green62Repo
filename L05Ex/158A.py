participants, scorePos = map(int, input().split())
scoreArr = list(map(int, input().split()))
count = 0

for score in scoreArr:
    if scorePos > len(scoreArr) - 1:
        print (len(scoreArr))
        break
    else:
        if score >= scoreArr[scorePos] and score > 0:
            count+= 1
        else: break

print (count)