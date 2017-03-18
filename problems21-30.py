import itertools


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


def problem24():
    """
    Lexicographic permutations
    """
    print("".join(list(itertools.permutations('0123456789'))[999999]))


def problem25():
    """
    1000-digit Fibonacci number
    """
    prev1 = 1
    prev2 = 2
    new = 0
    index = 3
    while len(str(new)) != 1000:
        new = prev1 + prev2
        prev1 = prev2
        prev2 = new
        index += 1
    print(index)


def problem26():
    """
    Reciprocal cycles, incomplete!
    """
    for d in range(2, 100):
        print(1/d, str(1/d).replace('0.', ''))


problem26()
