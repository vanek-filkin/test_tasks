import math


def get_prime_nums(n: int):
    return [i for i in range(2, n) if is_prime(i)]


def is_prime(num: int):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

print(get_prime_nums(100))
