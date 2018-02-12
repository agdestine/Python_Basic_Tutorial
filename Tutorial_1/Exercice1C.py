#Import the string library.
import string

#Create a variable alphabet that consists of the lowercase and uppercase letters in the English alphabet 
# using the ascii_letters data attribute of the string library.
alphabet = string.ascii_letters

#Create a dictionary count_letters with keys consisting of each unique letter in the sentence and values 
# consisting of the number of times each letter is used in this sentence.
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
for char in alphabet:
  count = sentence.count(char)
  if count > 0:
    count_letters.update({char:count})

#Make a function called counter that takes a string input_string and returns a dictionary of letter counts count_letters
def counter (sentence) :
    count_letters = {}
    for char in alphabet :
        count = sentence.count(char)
        if(count>0):
            count_letters.update({char:count})
    return count_letters
    
counter(sentence)
