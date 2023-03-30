'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return True
        elif AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        else:
            left = AVLTree._balance_factor(node.left) in [-1, 0, 1]
            right = AVLTree._balance_factor(node.right) in [-1, 0, 1]
            return left and right and AVLTree._is_avl_satisfied(node.left) and AVLTree._is_avl_satisfied(node.right)

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        return a copy of a new tree with new structure
        '''
        # old root - old right child
        # old right becomes parent
        # old root becomes left child of old right
        # all right children of old right stay right children
        # all left children of old root stay left children
        # all left children of old right become right children of old root
        # BF: -2 -> [0, 1, 2]
        # have separate case for root
        if node.right:
            new_root = Node(node.right.value)
            new_root.left = Node(node.value)
            new_root.right = node.right.right
            new_root.left.left = node.left
            new_root.left.right = node.right.left
            return new_root
        return node

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node.left:
            new_root = Node(node.left.value)  # old left becomes parent
            new_root.right = Node(node.value)  # old root becomes right child
            new_root.left = node.left.left  # left_child
            new_root.right.right = node.right
            new_root.right.left = node.left.right
            return new_root
        return node
        # old left child - old root
        # old left becomes parent
        # old root becomes right child of old left
        # all left children of old left stay left children
        # all right children of old root stay right children
        # all right children of old left become left children of old right
        # BF: 2 -> [-2, -1, 0]
        # have separate case for root
        # print(str(new))
        # print(str(new))
        # left_child = node.left.left # all left children of old left
        # print("left_child=", left_child)
        # print(str(new))
        # location = new.root
        # print("location=", location)
        # while left_child:
        #  location.left = left_child
        #  left_child = left_child.left
        #  print("left_child=", left_child)
        #  location = location.left
        #  print("location=", location)
        #  print(str(new))
        # print(str(new))
        # right_child = node.right
        # print("right_child=", right_child)
        # location = new.root.right
        # print("location=", location)
        # while right_child:
        #  location.right = right_child
        #  right_child = right_child.right
        #  print("right_child=", right_child)
        #  location = location.right
        #  print("location=", location)
        # print(str(new))
        # weird_child = node.left.right
        # location = new.root.right
        # while weird_child:
        #    location.left = weird_child
        #    weird_child = weird_child.left
        #   location = location.left
        #   print(str(new))

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self._insert(value, self.root)
            self.root = AVLTree._rebalance(self.root)
        else:
            self.root = Node(value)
        # BST insert by trolling down the tree and sticking it where it goes
        # for each ancestor node check bf
        # if any of the ancestor nodes became +/= 2, rebalance
        # if BF = +2, right rotation old left child - old root

    @staticmethod
    def _insert(value, node):
        if value < node.value:
            if node.left:
                AVLTree._insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                AVLTree._insert(value, node.right)
            else:
                node.right = Node(value)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        # if root +2
        #    if left node -1
        #        left rot left node - left right node
        #    right rot root left node
        # elif root -2
        #    if left node 1
        #        rot right left node - right node
        #    left rot root - right node
        if AVLTree._balance_factor(node) > 1:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
            node = AVLTree._right_rotate(node)
        elif AVLTree._balance_factor(node) < -1:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
            node = AVLTree._left_rotate(node)
        while not AVLTree._is_avl_satisfied(node):
            if node.left:
                node.left = AVLTree._rebalance(node.left)
            if node.right:
                node.right = AVLTree._rebalance(node.right)
        else:
            return node
