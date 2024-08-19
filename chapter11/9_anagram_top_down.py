"""
Anagram Generation with Top-Down Approach

Algorithm: pages 178--179

Permutations: P(n, n) = n!

Time complexity: O(n!) --> factorial time
"""


def anagrams(string):
    if len(string) == 1:  # base case
        return string[0]
    else:
        collection = []
        substring_anagrams = anagrams(string[1:])
        for index in substring_anagrams:
            for j in range(len(index) + 1):
                collection.append(index[:j] + string[0] + index[j:])

    return collection


# For displaying step-by-step execution:
def anagrams_steps(string):
    print(f"string = {string}")
    if len(string) == 1:  # base case
        return string[0]
    else:
        collection = []
        substring_anagrams = anagrams_steps(string[1:])
        print(f"substring_anagrams = {substring_anagrams}")
        for index in substring_anagrams:
            print(f"index = {index}")
            for j in range(len(index) + 1):
                print(
                    f"index[:j] = {index[:j]}; string[0] = {string[0]}; index[j:] = {index[j:]}"
                )
                collection.append(index[:j] + string[0] + index[j:])
            print(f"collection = {collection}")

    return collection


if __name__ == "__main__":
    word = "abcd"
    res = anagrams(word)
    print(res)

    print()

    print(anagrams_steps(word))
