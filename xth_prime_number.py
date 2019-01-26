from math import floor, ceil, log as ln


def get_lower_limit(x):
    return x*ln(x) + x*(ln(ln(x))-1)


def get_upper_limit(x):
    return x*ln(x) + x*ln(ln(x))


def is_prime(x):
    if x % 2 == 0:
        return x == 2
    elif x % 3 == 0:
        return x == 3

    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i+2) == 0:
            return False
        i += 6
    return True


def get_xth_prime_number(x):
    if x <= 100000:
        if x == 1:
            return 2
        elif x == 2:
            return 3

        current_num = 5
        count = 2
        step = 4

        while count < x:
            if is_prime(current_num):
                count += 1
            step = 6 - step
            current_num += step
        return current_num - step

    else:
        upper_limit = floor(get_upper_limit(x))
        lower_limit = ceil(get_lower_limit(x))
        return "The %d prime number lies within the range (%d, %d)" % (x, lower_limit, upper_limit)


def main():
    try:
        x = int(input("Enter a number: "))
        print(get_xth_prime_number(x))
    except ValueError:
        raise ValueError("Input must be a number")


if __name__ == '__main__':
    main()