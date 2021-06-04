## tree
## inorder, postorder to preorder

from sys import stdin
from collections import deque

if __name__ == "__main__":
    nodes = int(stdin.readline())
    inorder = list(map(int, stdin.readline().split()))
    postorder = list(map(int, stdin.readline().split()))
    