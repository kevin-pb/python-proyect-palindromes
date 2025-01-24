print("Enter a word or a sentence and I'll tell you if it's a palindrome: ")

data_enter = input("- ")

def palindrome_verify(word):
          
    characters = []

    for i in str(word.lower()):
        
        if i == " ":
            
            characters.append(i)
        
        elif i.isalnum():
            
            characters.append(i)
            
        else:
            
            print(f"You have not entered an alphanumeric value \n \nPlease enter an alphanumeric value:") 
            
            return palindrome_verify(input("- "))

    if characters[0:len(characters)] == list(reversed(characters)):
        
        return "It is a palindrome"

    else:
        
        return "It is not a palindrome"

print(palindrome_verify(data_enter))