def countvowels(string):
    count = 0
    for char in string:
        if char in "aeiouAEIOU":
            count += 1
    return count


def main():
    sent = input("Please type a sentence: ")

    print("count_vowels(", sent, ")=", countvowels(sent))


if __name__ == '__main__':
    main()
