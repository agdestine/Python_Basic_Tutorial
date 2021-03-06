#Import the string library.
import string;

#Create a variable alphabet that consists of the lowercase and uppercase letters in the English alphabet 
# using the ascii_letters data attribute of the string library.
alphabet = string.ascii_letters;

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

#Create a dictionary count_letters with keys consisting of each unique letter in the sentence and values 
# consisting of the number of times each letter is used in this sentence.

count_letters = {}
for char in alphabet:
  count = sentence.count(char)
  if count > 0:
    count_letters.update({char:count})
