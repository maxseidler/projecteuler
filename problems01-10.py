def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:       # equal to x % 2 == 0 but 30% faster
        return False

    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def is_palindrome(n):
    number = str(n)
    if number == number[::-1]:
        return True
    return False


def prod(numbers):
    p = 1
    for n in numbers:
        if n == '0':
            return 0
        p *= int(n)
    return p


def problem1():
    """
    Multiples of 3 and 5
    """
    sum_ = 0
    for x in range(1, 1000):
        if x % 3 == 0 or x % 5 == 0:
            sum_ += x
    print(sum_)


def problem2():
    """
    Even Fibonacci numbers
    """
    sum_even = 2
    prev1 = 1
    prev2 = 2
    new = 0
    while new < 4000000:
        new = prev1 + prev2
        prev1 = prev2
        prev2 = new
        if new % 2 == 0:
            sum_even += new
    print(sum_even)


def problem3():
    """
    Larges prime factor
    """
    n = 600851475143
    while n != 1:
        for x in range(2, n+1):
            if n % x == 0 and is_prime(x):
                n = int(n/x)
                print(x)
                break


def problem4():
    """
    Largest palindrome product
    """
    highest_palindrome = 1
    for factor1 in range(100, 1000):
        for factor2 in range(factor1, 1000):
            if factor1*factor2 > highest_palindrome and is_palindrome(factor1*factor2):
                highest_palindrome = factor1 * factor2
    print(highest_palindrome)


def problem5():
    """
    Smallest multiple
    """
    n = 20
    while True:
        if all(n % x == 0 for x in range(11, 20+1)):
            print(n)
            break
        n += 20


def problem6():
    """
    Sum square differences
    """
    print(sum(n for n in range(1, 101))**2 - sum(n**2 for n in range(1, 101)))


def problem7():
    """
    10001st prime
    """
    n = 3
    primecounter = 1
    while primecounter != 10001:
        if is_prime(n):
            primecounter += 1
        n += 2
    print(n-2)


def problem8():
    """
    Largest product in a series
    """
    digits = open("files/problem08_file.txt").read().replace('\n', '')
    digit_sequences = (digits[n:n+13] for n in range(0, 1000-13))
    print(max(prod(seq) for seq in digit_sequences))


def problem9():
    """
    Special Pythagorean triplet
    """
    for a in range(1, 332):
        for b in range(a+1, 499):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a*b*c)


def problem10():
    """
    Summation of primes
    """
    prime_sum = 2
    for n in range(3, 2000001, 2):
        if is_prime(n):
            prime_sum += n
    print(prime_sum)


problem10()
