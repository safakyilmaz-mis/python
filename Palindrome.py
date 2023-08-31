# Palindrome checker app

print("Palindrome checker")

i = 0
# We will use it to get the first letter
a = -1
# We will use it to get the last letter

word = input("Enter value: ")
for i in range(len(word)):
    # We will define i in for loop, and i long as "word"
    if word[i] != word[a]:
        # checking first and last letter is the same or different
            print(word + " is not Palindrome")
            break
        
    if word[i] == word[a]:
        # checking loop ended or not 
        # If ended and all letters same this variable is Palindrome
        print(word + " is Palindrome")
        break
        
    i += 1; a -= 1
    # Increase the i value and decrease the a value for checking variable letters
