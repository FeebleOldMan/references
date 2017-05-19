letter = input("Enter a letter from the alphabet: ")[0]

if letter in ['a', 'e', 'i', 'o', 'u']:
    print("Letter '{}' is a vowel.".format(letter))
elif letter == 'y':
    print("Letter '{}' is sometimes a vowel and sometimes a consonant.".format(
        letter
        ))
else:
    print("Letter '{}' is a consonant.".format(letter))
