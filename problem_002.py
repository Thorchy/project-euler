INPUT_NUMBER = 4000000


def generate_fibonacci_sequence(top_number):
    fibonacci_sequence = [1, 2]

    i = 2
    while i <= top_number:
        i = fibonacci_sequence[-2] + fibonacci_sequence[-1]
        fibonacci_sequence.append(i)

    return fibonacci_sequence


def sum_even_numbers(sequence):

    sum = 0
    for i in sequence:
        if i % 2 == 0:
            sum += i

    return sum


def main():
    print 'Problem 002: {}'.format(sum_even_numbers(generate_fibonacci_sequence(INPUT_NUMBER)))


def test_fibonacci_sequence():
    assert generate_fibonacci_sequence(100)[:10] == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_sum_even_fibonacci():
    assert sum_even_numbers(generate_fibonacci_sequence(100)[:10]) == 44


if __name__ == '__main__':
    main()
