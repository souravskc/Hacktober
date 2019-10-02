def count_vowels(s):
   '''
   >>> count_vowels('happy')
   1'''
   count=0
   for char in s:
       if char in 'aeiouAEIOU':
          count = count + 1

   return count     
def collect_vowels(s):
    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char

    return vowels
