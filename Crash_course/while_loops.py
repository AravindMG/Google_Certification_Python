def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    n = 2
    while n <= x:
        if x % n == 0:
            return n
        n = n + 1  # Fix for infinite loop


if __name__ == '__main__':
    print(smallest_prime_factor(12))  # should be 2
    print(smallest_prime_factor(15))  # should be 3
