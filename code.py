import string
alphabets = string.ascii_lowercase+string.ascii_uppercase
words=input("enter a word (enter to decode): ")
def encrypt(word,number):
  encrypted_word=""
  for letter in word:
    if letter.lower() in alphabets:
      original_position = alphabets.index(letter)
      new_position = original_position + number
      if new_position >= 26:
        new_position=  new_position - 26
      encrypted_word+=alphabets[new_position]
      if letter.isupper():
        encrypted_word=encrypted_word.upper()
    else:
      encrypted_word+=letter
  print(f" the encrtpted word is :  {encrypted_word}")
def orignal(word,number):
  encrypted_word=""
  for letter in word:
    if letter.lower() in alphabets:
      original_position = alphabets.index(letter)
      new_position = original_position - number
      if new_position >= 26:
        new_position=  new_position - 26
      encrypted_word+=alphabets[new_position]
      if letter.isupper():
        encrypted_word=encrypted_word.upper()
    else:
      encrypted_word+=letter
  print(f" the orignal word is :  {encrypted_word}")
if words:
 
  numbers=int(input("enter a number: "))
  encrypt(words,numbers)
else:
  words=input("enter encryted word : ")
  numbers=int(input("enter a number: "))
  orignal(words,numbers)
