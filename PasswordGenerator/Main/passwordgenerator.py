import random
import string


def split(word):
    return [char for char in word]


def generate_password(numOfLowLetters, numOfUpLetters, numOfDigits, numOfSpecials):
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    specials = string.punctuation
    password = ''.join(random.choice(lower_letters) for i in range(numOfLowLetters))
    password += ''.join(random.choice(upper_letters) for i in range(numOfUpLetters))
    password += ''.join(random.choice(digits) for i in range(numOfDigits))
    password += ''.join(random.choice(specials) for i in range(numOfSpecials))
    split_password = split(password)
    for i in range(2):
        random.shuffle(split_password)
    ready_password = ''.join(split_password)
    print(ready_password)


generate_password(5, 7, 4, 4)
