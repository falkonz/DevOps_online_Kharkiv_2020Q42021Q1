def fizzbuzz(n):
    if n % 15 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)


def main():
    for n in range(1, 101):
        print(fizzbuzz(n))


if __name__ == '__main__':
    main()
