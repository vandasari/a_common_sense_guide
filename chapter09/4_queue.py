"""
Algorithm: page 145
"""


class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.data.pop(0)

    def read(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.data[0]

    def isEmpty(self):
        return len(self.data) == 0


if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(9)
    q.enqueue(100)

    print(f"queue length = {len(q)}")
    print(q.read())
    q.dequeue()
    print(f"queue length after dequeueing = {len(q)}")
    print(q.read())
