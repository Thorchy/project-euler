INPUT_NUMBER = 1000


def list_natural_multiples_of_3_or_5(top_number):

    if top_number <= 1:
        return []

    numbers = []
    for number in range(1, top_number):
        if number % 3 == 0 or number % 5 == 0:
            numbers.append(number)

    return numbers


def sum_of_multiples_of_3_or_5(top_number):
    return sum(list_natural_multiples_of_3_or_5(top_number))


def main():
    print 'Problem 001: {}'.format(sum_of_multiples_of_3_or_5(INPUT_NUMBER))


def test_multiples():
    assert list_natural_multiples_of_3_or_5(10) == [3, 5, 6, 9]


def test_sum_of_multiples():
    assert sum_of_multiples_of_3_or_5(10) == 23


if __name__ == '__main__':
    main()
