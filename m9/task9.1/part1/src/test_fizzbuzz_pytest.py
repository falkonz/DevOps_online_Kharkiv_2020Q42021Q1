from fizzbuzz import fizzbuzz


def test_fizz():
    for n in [3, 6, 9, 18]:
        print('testing', n)
        assert fizzbuzz(n) == 'Fizz'


def test_buzz():
    for i in [5, 20, 70]:
        print('testing', i)
        assert fizzbuzz(i) == 'Buzz'


def test_fizzbuzz():
    for i in [15, 30, 75]:
        print('testing', i)
        assert fizzbuzz(i) == 'FizzBuzz'


def test_number():
    for i in [2, 4, 77]:
        print('testing', i)
        assert fizzbuzz(i) == str(i)
