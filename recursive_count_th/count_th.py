'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
   num_of_words = 0 
   if isinstance(word, int) == True: 
      return word 
   else: 
      if len(word) > 0: 
         num_of_words = word.count('th') 
         count_th(num_of_words)   
      return num_of_words 

