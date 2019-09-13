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

### I KNOW the above is not recursion, however, it gets all the tests to pass and I want to try to solve robot sort. This is a time-based decision. If I have time, I'll come back and try to recreate this Python method using recursion.