"""
Hash Tables for Speed --> applied on arrays

Algorithm: page 125
Time complexity: O(1)

By converting an array into a hash table in this way, we can go from O(n) 
searches to O(1) searches.
"""

array = [61, 30, 91, 11, 54, 38, 72]

hash_table = {item: True for item in array}

print(hash_table)

print(hash_table.get(61))

# This way will return None if the key is not in the hash table
print(hash_table.get(2))
