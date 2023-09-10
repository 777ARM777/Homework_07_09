class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'value: {self.value}, left: {self.left}, right: {self.right}'

    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.__len = 0

    def insert_value(self, value):
        self.__len += 1
        node = Node(value)
        if self.root is None:
            self.root = node
        elif value > self.root.value:
            if self.root.right is None:
                self.root.right = node
            tmp = BinarySearchTree()
            tmp.root = self.root.right
            tmp.insert_value(value)
        elif value < self.root.value:
            if self.root.left is None:
                self.root.left = node
            tmp = BinarySearchTree()
            tmp.root = self.root.left
            tmp.insert_value(value)

    def search_value(self, value):
        if self.root is None:
            return False
        elif self.root.value == value:
            return True
        elif self.root.value > value:
            tmp = BinarySearchTree()
            tmp.root = self.root.left
            return tmp.search_value(value)
        elif self.root.value < value:
            tmp = BinarySearchTree()
            tmp.root = self.root.right
            return tmp.search_value(value)

    def __eq__(self, other):
        if self.root is None or other.root is None:
            return self.root is None and other.root is None
        return self.root == other.root

    def __hash__(self):
        return hash(id(self.root))

    def __len__(self):
        return self.__len

    def __bool__(self):
        return self.root is not None

    def in_order(self):
        if self.root is not None:
            tmp = BinarySearchTree()
            tmp.root = self.root.left
            tmp.in_order()
            print(self.root.value, end=' ')
            tmp.root = self.root.right
            tmp.in_order()

    def pre_order(self):
        if self.root is not None:
            tmp = BinarySearchTree()
            print(self.root.value, end=' ')
            tmp.root = self.root.left
            tmp.pre_order()
            tmp.root = self.root.right
            tmp.pre_order()

    def post_order(self):
        if self.root is not None:
            tmp = BinarySearchTree()
            tmp.root = self.root.left
            tmp.post_order()
            tmp.root = self.root.right
            tmp.post_order()
            print(self.root.value, end=' ')



bst = BinarySearchTree()
bst.insert_value(12)
bst.insert_value(10)
bst.insert_value(20)
bst.insert_value(13)
bst.insert_value(7)
bst.insert_value(25)
bst.insert_value(11)

bst1 = BinarySearchTree()
bst1.insert_value(12)
bst1.insert_value(11)
bst1.insert_value(20)
bst1.insert_value(13)
bst1.insert_value(7)
bst1.insert_value(15)

print(bst.search_value(7))
print(bst == bst1)
print(bst.root)
print(bool(bst))

bst.in_order()
print()
bst.pre_order()
print()
bst.post_order()

