"""
Queues in Action

Algorithm: Page 146

A simple interface for a printer that can accept printing jobs from various
computers across a network.
"""

import time


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


class PrintManager(Queue):
    def __init__(self):
        super().__init__()

    def queue_print_job(self, document):
        self.enqueue(document)

    def printing(self, document):
        print(document)

    def run(self):
        while not self.isEmpty():
            self.printing(self.dequeue())
            time.sleep(0.7)


if __name__ == "__main__":
    doc1 = "First Document"
    doc2 = "Second Document"
    doc3 = "Third Document"
    doc4 = "Fourth Document"
    doc5 = "Fifth Document"

    print("--- Printing ---")

    q = PrintManager()

    q.queue_print_job(doc1)
    q.queue_print_job(doc2)
    q.queue_print_job(doc3)
    q.queue_print_job(doc4)
    q.queue_print_job(doc5)

    q.run()
