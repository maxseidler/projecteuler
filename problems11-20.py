def prod(numbers):
    p = 1
    for n in numbers:
        if n == '0':
            return 0
        p *= int(n)
    return p


def problem11():
    """
    Largest product over a grid
    """
    matrix = []
    grid = open("files/problem11_file.txt")
    for i in range(0, 20):
        matrix.append(grid.readline().replace('\n', '').split())

    prod_list = []
    # horizontal
    for i in range(0, 20):
        for j in range(0, 17):
            prod_list.append(prod(matrix[i][j+n] for n in range(0, 4)))

    # vertical
    for i in range(0, 17):
        for j in range(0, 20):
            prod_list.append(prod(matrix[i+n][j] for n in range(0, 4)))

    # diagonal top-left to bottom-right
    for i in range(0, 17):
        for j in range(0, 17):
            prod_list.append(prod(matrix[i+n][j+n] for n in range(0, 4)))

    # diagonal top-right to bottom-left
    for i in range(0, 17):
        for j in range(3, 20):
            prod_list.append(prod(matrix[i+n][j-n] for n in range(0, 4)))

    print(max(prod_list))


primes = {2}
def is_prime(n):
    if n in primes:
        return True
    if not n & 1:       # equal to x % 2 == 0 but 30% faster
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    primes.add(n)
    return True


def divisor_counter(n):
    prime_factors = []
    while n != 1:
        for x in range(2, n+1):
            if is_prime(x) and n % x == 0:
                prime_factors.append(x)
                n = int(n / x)
                break
    divisors = 1
    for prime in set(prime_factors):
        divisors *= (prime_factors.count(prime)+1)
    return divisors


def problem12():
    """
    Highly divisible triangular number
    """
    triangle_number = 0
    n = 1
    while True:
        triangle_number += n
        if divisor_counter(triangle_number) > 500:
            break
        n += 1
    print(triangle_number)


def problem13():
    """
    Large sum
    """
    f = open("files/problem13_file.txt")
    sum_array = [0] * 52

    for line in f:
        number_array = [int(i) for i in str(line.replace('\n', ''))][::-1]
        carry = 0
        for d in range(0, 50):
            if sum_array[d] + number_array[d] + carry > 9:
                sum_array[d] = (sum_array[d] + number_array[d] + carry) % 10
                carry = 1
            else:
                sum_array[d] += number_array[d] + carry
                carry = 0
        for d in range(50, 52):
            if sum_array[d] + carry > 9:
                sum_array[d] = (sum_array[d] + carry) % 10
                carry = 1
            else:
                sum_array[d] += carry
                carry = 0

    print(''.join(map(str, sum_array[52:41:-1])))


def problem14():
    """
    Longest Collatz sequence
    """
    collcatz_table = {}
    max_sequence = (0, 0)
    for n in range(1, 1_000_000):
        sequence_length = 1
        temp = n
        while temp != 1:
            if temp in collcatz_table:
                sequence_length += collcatz_table[temp]
                break
            if temp & 1:
                temp = 3 * temp + 1
            else:
                temp = int(temp / 2)
            sequence_length += 1
        collcatz_table[n] = sequence_length
        if collcatz_table[n] > max_sequence[1]:
            max_sequence = (n, sequence_length)

    print(max_sequence[0])


def fac(n):
    result = 1
    while n != 1:
        result *= n
        n -= 1
    return result


def problem15():
    """
    Lattice paths
    """
    print(int(fac(40)/(fac(20) * fac((40-20)))))


def problem16():
    """
    Power digit sum
    """
    print(sum(int(i) for i in str(pow(2, 1000))))


def written_out(n):
    table = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
             10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 15: 'fifteen', 18: 'eighteen', 20: 'twenty',
             30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    if n in table:
        return table[n]
    if n < 20:
        return table[n % 10] + 'teen'
    if n < 100:
        return table[int(n/10)*10] + '-' + written_out(n % 10)
    if n < 1000:
        return written_out(int(n/100)) + ' hundred' if n % 100 == 0\
            else written_out(int(n/100)) + ' hundred and ' + written_out(n % 100)
    if n < 10000:
        return written_out(int(n/1000)) + ' thousand' if n % 1000 == 0\
            else written_out(int(n/1000)) + ' thousand, ' + written_out(n % 1000)
    if n > 9999:
        print("Not yet implemented for number 10000 and bigger!")
        exit()


def problem17():
    """
    Number letter counts
    """
    char_count = 0
    for n in range(1, 1001):
        char_count += len(written_out(n).replace('-', '').replace(' ', ''))
    print(char_count)


def problem18():
    """
    Maximum path sum I *not finished*
    """
    t = open("files/problem18_file.txt")
    triangle = []
    for line in t:
        triangle.append(line.replace('\n', '').split(' '))
    for row in range(0, 15):
        max_n = max(triangle[row])
        print(max_n, triangle[row].index(max_n), triangle[row])


def problem19():
    """
    Counting Sundays
    """
    number_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 7
    month = 1
    year = 1900
    nr_of_sundays = 0
    while year < 2001:
        day += 7
        if day > number_of_days[month-1]:
            day = day - number_of_days[month-1]
            month += 1
        if month > 12:
            year += 1
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # leap year
                number_of_days[1] = 29
            else:
                number_of_days[1] = 28
            month = 1
        if year > 1900 and day == 1:
            nr_of_sundays += 1
    print(nr_of_sundays)


def problem20():
    """
    Factorial digit sum
    """
    print(sum(int(d) for d in str(fac(100))))


problem20()
