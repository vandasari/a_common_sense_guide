"""
Implementing a Linked List

Algorithm: Page 227
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


if __name__ == "__main__":
    # Create a chain of 4 nodes containing strings:
    node_1 = Node("once")
    node_2 = Node("upon")
    node_3 = Node("a")
    node_4 = Node("time")

    # The next_node refers to another Node instance
    node_1.next_node = node_2
    node_2.next_node = node_3
    node_3.next_node = node_4

    # Access nodes contents:
    print(node_1.data)
    print(node_2.data)
    print(node_3.data)
    print(node_4.data)

    print()

    # Test memory location
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    # The next_node refers to another Node instance
    n1.next_node = n2
    n2.next_node = n3
    n3.next_node = n4

    print("--- Memory location of nodes ---")
    nloc1 = id(n1)
    nloc2 = id(n2)
    nloc3 = id(n3)
    nloc4 = id(n4)
    print(f"node: {n1.data} -> address: id(n1) = {nloc1}")
    print(f"node: {n2.data} -> address: id(n2) = {nloc2}")
    print(f"node: {n2.data} -> address: id(n1.next_node) = {id(n1.next_node)}")
    print(f"node: {n3.data} -> address: id(n3) = {nloc3}")
    print(f"node: {n3.data} -> address: id(n2.next_node) = {id(n2.next_node)}")
    print(f"node: {n4.data} -> address: id(n4) = {nloc4}")
    print(f"node: {n4.data} -> address: id(n3.next_node) = {id(n3.next_node)}")
    # print(id(n1.next_node))
    print(f"{n2.data} is {nloc2-nloc1} bytes from {n1.data}")
    print(f"{n3.data} is {nloc3-nloc2} bytes from {n2.data}")
    print(f"{n4.data} is {nloc4-nloc3} bytes from {n3.data}")

    print()

    arr = [1, 2, 3, 4]

    print("--- Memory location of array elements ---")
    loc1 = id(arr[0])
    loc2 = id(arr[1])
    loc3 = id(arr[2])
    loc4 = id(arr[3])
    print(f"element: {arr[0]} -> address: {loc1}")
    print(f"element: {arr[1]} -> address: {loc2}")
    print(f"element: {arr[2]} -> address: {loc3}")
    print(f"element: {arr[3]} -> address: {loc4}")
    print(f"{arr[1]} is {loc2-loc1} bytes from {arr[0]}")
    print(f"{arr[2]} is {loc3-loc2} bytes from {arr[1]}")
    print(f"{arr[3]} is {loc4-loc3} bytes from {arr[2]}")
