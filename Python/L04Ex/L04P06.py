def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def closest_prime(num):
    if num < 2:
        return 2
    low_bound = num
    upper_bound = num
    while True:
        if is_prime(low_bound):
            return low_bound
        if is_prime(upper_bound):
            return upper_bound
        low_bound -= 1
        upper_bound += 1

n = int(input())
print(closest_prime(n))