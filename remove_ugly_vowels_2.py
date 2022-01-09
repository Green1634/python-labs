word_without_vowels = ""

# Prompt the user to enter a word
words = input("enter a word: ")
# and assign it to the user_word variable.
user_word = words
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the loop.
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)
# Print the word assigned to word_without_vowels.
