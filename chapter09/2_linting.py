"""
Algorithm: pages 140-141
"""


class Stack:
    def __init__(self):
        # Whenever a stack is initiated, we automatically build an empty array with data:
        self.data = []

    def __len__(self):
        return len(self.data)

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.data.pop()

    def read(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return "Stack is empty"

    def isEmpty(self):
        return len(self.data) == 0


class Linter:
    def __init__(self):
        self.stack = Stack()

    def lint(self, text):
        for char in text:
            if self.is_opening_brace(char):
                self.stack.push(char)
            elif self.is_closing_brace(char):
                popped_opening_brace = self.stack.pop()

                if not popped_opening_brace:
                    print(f"{char} does not have opening brace")

                if self.is_not_a_match(popped_opening_brace, char):
                    print(f"{char} has mismatched opening brace")

        if self.stack.isEmpty() == False:
            temp = []
            if len(self.stack) > 1:
                for j in range(len(self.stack)):
                    temp.append(self.stack.pop())
                print(f"{temp} do not have closing brace")
            else:
                print(f"{self.stack.read()} does not have closing brace")
        else:
            print("Everying is in order")

    def is_opening_brace(self, char):
        if char == "(":
            return True
        elif char == "[":
            return True
        elif char == "{":
            return True
        else:
            return False

    def is_closing_brace(self, char):
        if char == ")":
            return True
        elif char == "]":
            return True
        elif char == "}":
            return True
        else:
            return False

    def is_not_a_match(self, opening_brace, closing_brace):
        if opening_brace != "[" and closing_brace != "]":
            return True
        elif opening_brace != "{" and closing_brace != "}":
            return True
        elif opening_brace != "(" and closing_brace != ")":
            return True
        else:
            return False


if __name__ == "__main__":

    # string = '(var x = {y: [1, 2, 3] })'
    string = "{{a( b]4[d )"
    # string = 'a( b]4[d )'

    print(string)

    print()

    test = Linter()
    test.lint(string)
