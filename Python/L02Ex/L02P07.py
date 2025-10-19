# lastMonth, thisMonth = map(int, (input().split()))
# elecUsage = thisMonth - lastMonth
# elecBill = 0

# toFifty = 1484 * 50
# toOneHundred = toFifty + 1533 * 50
# toTwoHundred = toOneHundred + 1786 * 100
# toThreeHundred = toTwoHundred + 2242 * 100
# toFourHundred = toThreeHundred + 2503 * 100
# overFourHundred = toFourHundred + 2587 * (elecUsage - 400)

# if (elecUsage <= 50):
#     elecBill = elecUsage * 1484
# elif (50 < elecUsage <= 100):
#     elecBill = toFifty + (elecUsage - 50) * 1533
# elif (100 < elecUsage <= 200):  
#     elecBill = toOneHundred + (elecUsage - 100) * 1786
# elif (200 < elecUsage <= 300):
#     elecBill = toTwoHundred + (elecUsage - 200) * 2242
# elif (300 < elecUsage <= 400):
#     elecBill = toThreeHundred + (elecUsage - 300) * 2503
# else:
#     elecBill = overFourHundred

# totalBill = elecBill + elecBill * 0.1
# print (int(totalBill))

lastMonth, thisMonth = map(int, input().split())
elecUsage = thisMonth - lastMonth

# Define the tiers: (max_units, rate)
tiers = [
    (50, 1484),
    (100, 1533),
    (200, 1786),
    (300, 2242),
    (400, 2503),
    (float('inf'), 2587)  # anything above 400
]

elecBill = 0
prev_limit = 0

for limit, rate in tiers:
    if elecUsage > prev_limit:
        usage_in_tier = min(elecUsage, limit) - prev_limit
        elecBill += usage_in_tier * rate
        prev_limit = limit
    else:
        break

totalBill = elecBill * 1.1  # add 10% tax
print(int(totalBill))
