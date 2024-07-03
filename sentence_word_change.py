sentence = input("Please enter a sentence: ")
old_w = input("Please Enter the word to change: ")
new_w = input("Please Enter the new word: ")

x = sentence.replace(old_w, new_w)
print("Updated version is: ", x)