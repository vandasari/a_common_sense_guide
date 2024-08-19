"""
String Reversal with Top-Down Approach

Algorithm: page 171
"""


def reverse(string):
    # base caseL only one element in the string
    if len(string) == 1:
        return string[0]
    return reverse(string[1 : len(string)]) + string[0]


# For displaying step-by-step execution:
def reverse_steps(string):
    # base caseL only one element in the string
    if len(string) == 1:
        print(f"Base case. Returning {string[0]}")
        return string[0]
    else:
        print(f"Reversing: {string}, top = {string[0]}")
        temp = reverse_steps(string[1 : len(string)]) + string[0]
        print(f"Returning: {temp}")
        return temp


if __name__ == "__main__":
    word = "abcdef"

    print(f"String: {word}")

    print(f"Reverse: {reverse(word)}")

    print()

    res = reverse_steps(word)
    print(f"Reverse: {res}")
