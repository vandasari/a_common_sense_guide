"""
Algorithm: pages 97 & 98
Time complexity: O(n^2) & O(n^3)

This algorithm collects every combination of two-character strings built from 
an array of single characters.
"""

# Time complexity: O(n^2)
def wordBuilderTwoCharacters(array):
    collection = []
    
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                collection.append(array[i] + array[j])
                
    return collection


# Time complexity: O(n^3)
def wordBuilderThreeCharacters(array):
    collection = []
    
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if i != j and j != k and i != k:
                    collection.append(array[i] + array[j] + array[k])
                    
    return collection


if __name__ == '__main__':
    arr = ['a', 'b', 'c', 'd']
    
    res2c = wordBuilderTwoCharacters(arr)
    
    print(res2c)
    
    print()
    
    res3c = wordBuilderThreeCharacters(arr)
    
    print(res3c)

"""
Returns:
    
['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']

['abc', 'abd', 'acb', 'acd', 'adb', 'adc', 
 'bac', 'bad', 'bca', 'bcd', 'bda', 'bdc', 
 'cab', 'cad', 'cba', 'cbd', 'cda', 'cdb', 
 'dab', 'dac', 'dba', 'dbc', 'dca', 'dcb']
"""