sentence = input("Please Enter a Sentece: ")
low_sentence = ''
up_sentence = ''

for i in sentence :
    if(i>='A' and i<='Z'):
        low_sentence = low_sentence + chr((ord(i)+32))
    else :
        low_sentence = low_sentence + i

for i in sentence :
    if(i>='a' and i<='z'):
        up_sentence = up_sentence + chr((ord(i)-32))
    else :
        up_sentence = up_sentence + i



print("\nOriginal sentence: ", sentence)
print("\nLowercase: ", low_sentence)
print("\nUppercase: ", up_sentence)
print("\nWords splitted: ", sentence.split())
print("\nLength of sentence: ", len(sentence))
