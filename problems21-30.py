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


problem21()
