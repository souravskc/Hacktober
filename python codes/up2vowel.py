def up_to_vowel(s):
    '''(str) -> str
    return a substring of s from index 0 up to but not including the first vowel in s.
    '''
    i=0
    before_vowel =''
    while i < len(s) and not(s[i] in 'aeiouAEIOU'):
         before_vowel= before_vowel + s[i]
         i = i + 1

    return before_vowel
    
def remove_vowel(s):
    i=0
    before=''
    while i<len(s) and not(s[i] in 'aeiouAEIOU'):
        before=before + s[i]
        i = i + 1


    return before    

def flush_digits():
    i=0
    
         
