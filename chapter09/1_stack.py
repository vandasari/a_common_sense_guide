"""
Algorithm: page 136

Since Python doesn't have a built-in data type of stack, we have to implement it
ourselves. Here is an example.
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


if __name__ == "__main__":
    test = Stack()
    test.push(2)
    test.push(5)
    test.push(7)
    test.push(-6)

    print(f"length of stack: {len(test)}")

    print(f"the last element of stack: {test.read()}")

    test.pop()

    print(f"after popping, the last element of stack now: {test.read()}")

    print(f"length of stack now: {len(test)}")
