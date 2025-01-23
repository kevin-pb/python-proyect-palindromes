print("Enter a word and I'll tell you if it's a palindrome: ")

data_enter = input("- ")

characters = []

for i in str(data_enter.lower()):
    characters.append(i)

if characters[0:len(characters)] == list(reversed(characters)):
    print("It is a palindrome")

else:
    print("It is not a palindrome")