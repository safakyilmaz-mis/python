#Palindrome checker app
print("Palindrome checker")
i = 0
a = -1
word = input("Enter value: ")
for i in range(len(word)):
    if word[i] != word[a]:
            print(word + " is not Palindrome")
            break
        
    if word[i] == word[a]:
        if len(word) == i+1:
            print(word + " is Palindrome")
            break
        
    i += 1; a -= 1
