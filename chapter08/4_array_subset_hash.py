"""
Algorithm: page 129-130
Time complexity: O(n)
"""


def isSubset(array1, array2):

    largerArray = []
    smallerArray = []

    # Determine which array is smaller and which is larger
    if len(array1) > len(array2):
        largerArray = array1
        smallerArray = array2
    else:
        largerArray = array2
        smallerArray = array1

    # Create a hash table (dictionary) whose keys are largeArray items and all values are set to True
    hashTable = {item: True for item in largerArray}

    # For each value in smaller array, iterate through the hash table
    for value in smallerArray:
        if hashTable.get(value) != True:  # See Ref [1]
            return False

    return True


if __name__ == "__main__":
    arr1 = ["a", "b", "c", "d", "e", "f", "g", "i", "l", "m", "n"]
    arr2 = ["p", "d", "e", "j", "k"]

    res = isSubset(arr1, arr2)
    print("Not a subset" if res == False else "A subset")


"""
References:
[1] https://stackoverflow.com/questions/6130768/return-a-default-value-if-a-dictionary-key-is-not-available
"""
