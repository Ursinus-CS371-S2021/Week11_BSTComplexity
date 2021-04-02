import numpy as np
import matplotlib.pyplot as plt

class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def __str__(self):
        return "{}".format(self.key)

    def maxnode(self):
        res = self
        if self.right:
            res = self.right.maxnode()
        return res
    
    def _swapwith(self, other):
        self.key, other.key = other.key, self.key

    def remove(self, key):
        if key == self.key:
            # We've found the node to remove
            ## Step 1: Handle the case with one or no children
            if not self.left:
                return self.right
            if not self.right:
                return self.left
            ## Step 2: Handle the case with two children
            # Step 2a: Find the maximum node in the left
            # subtree, then swap that node's key with this
            # node's key
            self._swapwith(self.left.maxnode())
            # Step 2b: Remove the node from the left subtree
            # where it now resides
            self.left = self.left.remove(key)
        elif key < self.key:
            if self.left:
                self.left = self.left.remove(key)
            else:
                print("No key {}".format(key), end='.')
        elif key > self.key:
            if self.right:
                self.right = self.right.remove(key)
            else:
                print("No key {}".format(key), end='.')
        return self
        
    def add(self, key):
        if key < self.key:
            if self.left:
                return self.left.add(key)
            else:
                self.left = TreeNode(key)
                return self.left
        elif key > self.key:
            if self.right:
                return self.right.add(key)
            else:
                self.right = TreeNode(key)
                return self.right

    def contains(self, key):
        res = False
        if self.key == key:
            res = True
        else:
            if self.left:
                res = self.left.contains(key)
            if not res and self.right:
                res = self.right.contains(key)
        return res

    def compute_coords(self, x = [0], y = 0):
        if self.left:
            self.left.compute_coords(x, y-1)
        self.x = x[0]
        self.y = y
        x[0] += 1
        if self.right:
            self.right.compute_coords(x, y-1)

    def draw(self):
        # Draw a dot
        plt.scatter(self.x, self.y, 50, 'k')
        # Draw some text indicating what the key is
        plt.text(self.x+0.1, self.y+0.1, "{}".format(self.key))
        # Offset in x
        if self.left:
            # Draw a line segment from my node to this left child
            plt.plot([self.x, self.left.x], [self.y, self.left.y])
            self.left.draw()
        if self.right:
            # Draw a line segment from my node to this right child
            plt.plot([self.x, self.right.x], [self.y, self.right.y])
            self.right.draw()
    
    def inorder(self, res = []):
        if self.left:
            self.left.inorder(res)
        res.append(self.key)
        if self.right:
            self.right.inorder(res)

class BinaryTree(object):
    def __init__(self):
        self.root = None
    
    def remove(self, key):
        if self.root:
            self.root = self.root.remove(key)

    def add(self, key):
        if self.root:
            return self.root.add(key)
        else:
            self.root = TreeNode(key)
            return self.root

    def contains(self, key):
        res = False
        if self.root:
            res = self.root.contains(key)
        return res

    def draw(self):
        if self.root:
            self.root.compute_coords()
            self.root.draw()
        plt.axis("off")
        plt.axis("equal")
    
    def inorder(self):
        res = []
        if self.root:
            self.root.inorder(res)
        return res


def rotateleft(w, lookup):
    assert(w.right)
    u = w.right
    A = w.left
    B = u.left
    C = u.right
    w.key, u.key = u.key, w.key
    w, u = u, w
    lookup[w.key] = w
    lookup[u.key] = u
    w.left = A
    w.right = B
    u.right = C
    u.left = w

def rotateright(u, lookup):
    assert(u.left)
    w = u.left
    ## TODO: Fill this in; save A, B, and C
    w.key, u.key = u.key, w.key
    w, u = u, w
    lookup[w.key] = w
    lookup[u.key] = u
    ## TODO: Fill this in; re-assign children of w and u

def make_tree1():
    T = BinaryTree()
    np.random.seed(2)
    for key in np.random.permutation(40)*5:
        T.add(key)
    return T

def tree_rotation_example():
    T = BinaryTree()
    np.random.seed(3)
    keys = np.random.permutation(20)*5
    keys = keys.tolist() + [6, 100, 56, 34, 84]
    print(len(keys))
    lookup = {}
    for key in keys:
        lookup[key] = T.add(key)
    
    plt.figure(figsize=(15, 6))
    T.draw()
    plt.savefig("1.png", bbox_inches='tight')
    print(T.inorder())
    
    rotateleft(lookup[85], lookup)
    print(T.inorder())
    plt.clf()
    T.draw()
    plt.savefig("2.png", bbox_inches='tight')
    
    rotateleft(lookup[30], lookup)
    print(T.inorder())
    plt.clf()
    T.draw()
    plt.savefig("3.png", bbox_inches='tight')


tree_rotation_example()