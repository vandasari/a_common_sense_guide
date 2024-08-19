"""
Exercise 3 - Finding a Needle in the Haystack
Time complexity: O(n*m)
"""

def find_needle(needle, haystack):
    needle_index = 0
    haystack_index = 0
    
    while haystack_index < len(haystack):
        
        if needle[needle_index] == haystack[haystack_index]:
            found_needle = True
            
            while needle_index < len(needle):                
                if needle[needle_index] != haystack[haystack_index + needle_index]:
                    found_needle = False
                    break
                
                needle_index += 1
                
            if found_needle:
                return True
            
            needle_index = 0
            
        haystack_index += 1
        
    return False


if __name__ == '__main__':    
    n = 'xyz' # worst-case scenario
    # n = 'def' # average-case scenario
    h = 'abcdefghij'
    
    res = find_needle(n, h)
    print(f'{res}')
  