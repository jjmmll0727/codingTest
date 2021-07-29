## 전위순회 후위순회 
## key point -> make a tree and insert to array
## must review!!!

from sys import stdin

class Node:
    def __init__(self, head, left, right):
        self.data = head
        self.left = left
        self.right = right

def preorder(root):
    print(root.data, end = '')
    if root.left != '.':
        preorder(tree[root.left])
    if root.right != '.':
        preorder(tree[root.right])

def inorder(root):
    if root.left != '.':
        inorder(tree[root.left])
    print(root.data, end = '')
    if root.right != '.':
        inorder(tree[root.right])

def postorder(root):
    if root.left != '.':
        postorder(tree[root.left])
    if root.right != '.':
        postorder(tree[root.right])
    print(root.data, end = '')

if __name__ == "__main__":
    tree = {}
    count = int(stdin.readline())
    for i in range(count):
        nodes = stdin.readline().split()
        tree[nodes[0]] = Node(nodes[0], nodes[1], nodes[2])
    
    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])
