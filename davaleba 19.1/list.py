class Node:
    def __init__(self, data):
        # Each node stores some data.
        self.data = data
        # It also has a reference to the next node, initially set to None.
        self.next = None

# This class represents a linked list.
class LinkedList:
    def __init__(self):
        # It starts with no nodes.
        self.head = None

    # This method adds a new node at the end of the list.
    def append(self, data):
        new_node = Node(data)

        # If the list is empty, the new node becomes the head.
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse the list to find the last node and append the new node.
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # This method inserts a new node with given data at the specified index.
    def insert(self, data, index):
        new_node = Node(data)

        # If the index is 0, insert the new node at the beginning of the list.
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Otherwise, traverse the list to find the node at the specified index,
        # then insert the new node after that node.
        current_node = self.head
        current_index = 0
        while current_node.next and current_index < index - 1:
            current_node = current_node.next
            current_index += 1

        new_node.next = current_node.next
        current_node.next = new_node

    # This method removes the node at the specified index.
    def remove(self, index):
        # If the index is 0, remove the first node.
        if index == 0:
            self.head = self.head.next
            return

        # Otherwise, traverse the list to find the node just before the specified index,
        # then adjust the pointers to remove the node.
        current_node = self.head
        current_index = 0
        while current_index < index - 1 and current_node.next:
            current_index += 1
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    # This method displays the data stored in the list.
    def display_info(self):
        current_node = self.head

        # Traverse the list and print the data of each node.
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()

# Create a linked list object.
linked_list = LinkedList()

# Add some elements to the list.
linked_list.append(5)
linked_list.append(10)
linked_list.append(2)

# Display the list.
linked_list.display_info()

# Insert new elements at specific positions.
linked_list.insert(11, 1)
linked_list.insert(15, 2)

# Display the list again.
linked_list.display_info()  

# Remove an element from the list.
linked_list.remove(2)

# Display the modified list.
linked_list.display_info() 
