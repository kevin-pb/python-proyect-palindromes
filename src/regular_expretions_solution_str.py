import re

print("Enter a word or a sentence and I'll tell you if it's a palindrome: ")

data_enter = input("- ")

def is_valid(word):
    if (
        re.search("^\w+[\w|\s]*$", word)
    ):
        return True
    else:
        return False


def palindrome_verify(characters):

    if is_valid(characters) == False:
        print(
            f"You have not entered an alphanumeric value \n \nPlease enter an alphanumeric value:"
        )
        return palindrome_verify(input("- "))

    reversed_list = characters[::-1]
    if characters == reversed_list:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"


print(palindrome_verify(data_enter))


print(ord("9"))
