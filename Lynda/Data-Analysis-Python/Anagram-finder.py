
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
    
s[0:5]

wordclean = [word.strip().lower() for word in s]

wordclean[10:12]

#get rid of all the duplicates using the set function:

h = list(set(wordclean))
h.sort()

#use the "sorted" function to generate a sorted list of letters from the word. two 'sorted' words that are anagrams should be identical
def signature(word):
    return ''.join(sorted(word))

#create an ID for each word (sorted word). Use the ID as a key in a dictionary
#then where the IDs match for various words, add the words as a values in a list format.
import collections
#create a default value in case of passing an unknown key, in this case the value is a list.
words_byID = collections.defaultdict(list)
for word in h:
    words_byID[signature(word)].append(word)
    
#now we have a dictionary containing lists of all its possible anagrams.
