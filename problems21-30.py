def divisors(n):
    return (x for x in range(1, int(n/2+1)) if n % x == 0)


def problem21():
    """
    Amicable numbers
    """
    d = [0]
    for n in range(1, 10000):
        d.append(sum(divisors(n)))
    amicable_sum = 0
    for a in range(0, 10000):
        b = d[a]
        if b < 10000 and a != b and d[b] == a:
            amicable_sum += a
    print(amicable_sum)


def problem22():
    """
    Names scores
    """
    names = open('files/problem22_file.txt').read()
    sorted_names = [name.replace('"', '') for name in sorted(names.split(','))]
    name_score = 0
    for i in range(0, len(sorted_names)):
        name_score += sum(ord(char)-64 for char in sorted_names[i]) * (i+1)
    print(name_score)


def sum_of_two_abundant_numbers(n, abundant_numbers):
    for abund_n in abundant_numbers:
        if n - abund_n in abundant_numbers:
            return True
    return False


def problem23():
    """
    Non-abundant sums
    """
    abundant_numbers = set(n for n in range(0, 28124) if sum(divisors(n)) > n)
    print(sum(n for n in range(1, 28124) if not sum_of_two_abundant_numbers(n, abundant_numbers)))


problem23()