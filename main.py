import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_composite(n):
    if n % 2 == 0:
        for i in range(4, n//2 + 1):
            if not is_prime(i) and not is_prime(n-i):
                return i, n-i
    else:
        if not is_prime(n-9) and not is_prime(9):
            return 9, n - 9
    return None

num = int(input())
result = sum_of_composite(num)
if result:
    print(result[0])
    print(result[1])