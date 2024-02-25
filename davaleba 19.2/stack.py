class Node:
    def __init__(self, data):
        # Create a new node with some data.
        self.data = data
        # Point to the next node, initially no next node.
        self.next = None

# Stack class definition.
class Stack:
    def __init__(self):
        # Initialize an empty stack.
        # It has no top node and its length is 0.
        self.top_node = None
        self.length = 0

    # Check if the stack is empty.
    def empty(self):
        # Return True if the stack has no elements, False otherwise.
        return self.length == 0

    # Get the number of elements in the stack.
    def size(self):
        # Return the number of elements in the stack.
        return self.length

    # Get the data of the top element in the stack.
    def top(self):
        # If the stack is not empty, return the data of the top node.
        if not self.empty():
            return self.top_node.data
        else:
            # If the stack is empty, raise an error.
            raise IndexError("Stack Is Empty")

    # Add a new element to the top of the stack.
    def push(self, data):
        # Create a new node with the given data.
        new_node = Node(data)
        # Make the new node the new top node.
        new_node.next = self.top_node
        self.top_node = new_node
        # Increase the length of the stack.
        self.length += 1

    # Remove and return the top element from the stack.
    def pop(self):
        # If the stack is not empty, remove and return the top node's data.
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        else:
            # If the stack is empty, raise an error.
            raise IndexError("Stack Is Empty")


# Create a stack object.
stack = Stack()

# Print the size of the stack.
print(stack.size())

# Add some elements to the stack.
stack.push(1)
stack.push(5)
stack.push(10)

# Print the size of the stack after adding elements.
print(stack.size())

# Remove and print the top element from the stack.
print(stack.pop())

# Print the top element in the stack.
print(stack.top())
