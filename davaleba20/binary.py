class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Function to print the data of leaf nodes in the binary tree.
    def printLeafNodes(self, node):
        # If the current node exists:
        if node:
            # If the current node has no children (left and right):
            if not node.left and not node.right:
                # Print the data of the leaf node.
                print(node.data)
            # Recursively call the function for the left subtree.
            self.printLeafNodes(node.left)
            # Recursively call the function for the right subtree.
            self.printLeafNodes(node.right)

    # Function to count the number of edges in the binary tree.
    def countEdges(self, node):
        # If the current node is None, there are no edges.
        if not node:
            return 0
        else:
            # Count edges in the left subtree.
            left_edges = self.countEdges(node.left)
            # Count edges in the right subtree.
            right_edges = self.countEdges(node.right)
            # Total edges in the current subtree are edges in left + edges in right + 1 (for current node).
            return left_edges + right_edges + 1

# Example usage:
# Create a binary tree.
tree = BinaryTree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

# Print the leaf nodes of the binary tree.
print("Leaf Nodes:")
tree.printLeafNodes(tree.root)

# Count and print the number of edges in the binary tree.
print("Number of Edges in the Tree:", tree.countEdges(tree.root))
