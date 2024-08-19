"""
Algorithm: pages 127--128
Time complexity: O(n*m)
"""


def isSubset(array1, array2):
    largerArray = []
    smallerArray = []

    if len(array1) > len(array2):
        largerArray = array1
        smallerArray = array2
    else:
        largerArray = array2
        smallerArray = array1

    for i in range(len(smallerArray)):
        foundMatch = False

        for j in range(len(largerArray)):
            if smallerArray[i] == largerArray[j]:
                foundMatch = True
                break

        if foundMatch == False:
            return False

    return True


if __name__ == "__main__":
    arr1 = ["a", "b", "c", "d", "e", "f"]
    arr2 = ["b", "d", "h"]

    res = isSubset(arr1, arr2)
    print("Not a subset" if res == False else "A subset")
