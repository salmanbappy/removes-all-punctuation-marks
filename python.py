# A python program to remove all the puncuation marks from a line.
import string
txt = input('Enter your line = ')
txt_cleaned = txt.translate(str.maketrans("", "", string.punctuation))
print(txt_cleaned)
