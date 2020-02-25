def is_power_of_two(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2

    return True


if __name__ == '__main__':
    print(is_power_of_two(0))  # Should be False
    print(is_power_of_two(1))  # Should be True
    print(is_power_of_two(8))  # Should be True
    print(is_power_of_two(9))  # Should be False
