
"""
Practical project: Write python code in order to find all the anagrams in a dictionary of english words.
The dictionary of words was provided as a list in a file called 'words'

Aim of exercise: Applying previously qcquired knowledge on lists, dictionaries and comprehensions
"""

#Code used to obtain objective:

path = 'Exercise Files/Ch3/03_02/words'

try:
    f = open(path, 'r')
    s = f.readlines()
except:
    print('error')
    
