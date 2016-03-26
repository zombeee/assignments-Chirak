#! /usr/bin/env python


from __future__ import print_function, division
import random


class Node(object):
    """
    This class creates Node with 4 attributes: number (integer number),
    parent (default = None), left and right children (default = None)
     :type _number: int
     :type _parent: Node
     :type _l_child: Node
     :type _r_child: Node
    """
    def __init__(self, number, parent=None, l_child=None, r_child=None):
        """
        Initiate node
        :type number: int
        :param number:  each Node hold one number
        :type parent: Node
        :param parent: Parent Node
        :type l_child: Node
        :param l_child: child Node with number less or equal to Node number
        :type r_child: Node
        :param r_child: child Node with number greater then Node number
        """
        self._number = number
        self._parent = parent if parent else None
        self._l_child = l_child if l_child else None
        self._r_child = r_child if r_child else None

    @property
    def number(self):
        """
        This function applies to call parameter "number" not through function
        :return: Parameter "number"
        """
        return self._number

    @property
    def parent(self):
        """
        This function applies to call parameter "parent" not through function
        :return: Parameter "parent"
        """
        return self._parent

    @property
    def l_child(self):
        """
        This function applies to call parameter "l_child" not through function
        :return: Parameter "l_child"
        """
        return self._l_child

    @property
    def r_child(self):
        """
        This function applies to call parameter "r_child" not through function
        :return: Parameter "r_child"
        """
        return self._r_child

    def __str__(self):
        """
        Applies to represent node as the string
        :return: str "(item, priority)"
        """
        return str((self.number, self.parent, [self.l_child, self.r_child]))

    def __ne__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return not self == other

    def __eq__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.number == other.number

    def __gt__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.number > other.number

    def __ge__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.number >= other.number

    def __lt__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.number < other.number

    def __le__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.number <= other.number


class SearchTree(object):
    """
    This class creates binary search tree object implemented on tree.
    This tree consists of Nodes
    Each left child must be less or equal to his parent
    Each right child must be greater then his parent
    Parent node can have only two children
    :type _tree: list
    """
    def __init__(self, sequence):
        """
        Initiate tree
        :type sequence: iterable
        :param sequence: list of numbers
        """
        random_head_idx = random.randint(0, len(sequence))
        self._tree = [Node(sequence[random_head_idx])]
        for idx in xrange(len(sequence)):
            if idx != random_head_idx:
                self.push(sequence[idx])
            else:
                continue

    def __contains__(self, item):
        pass

    def push(self, number):
        """
        :type number: int
        :param number: Eny input value
        """
        new_node = Node(number)
        self._tree.append(new_node)
        current_node = self._tree[0]
        while current_node.l_child or current_node.r_child:
            if new_node > current_node and current_node.r_child:
                current_node = current_node.r_child
                continue
            if new_node <= current_node and current_node.l_child:
                current_node = current_node.l_child
                continue
            if new_node > current_node:
                current_node._r_child = new_node
                new_node._parent = current_node
                break
            if new_node <= current_node:
                current_node._l_child = new_node
                new_node._parent = current_node
                break
        if not current_node.l_child and not current_node.r_child:
            if new_node > current_node:
                current_node._r_child = new_node
                new_node._parent = current_node
            if new_node <= current_node:
                current_node._l_child = new_node
                new_node._parent = current_node

    @staticmethod
    def exchange(node_1, node_2):
        """
        Exchange two nodes
        :type node_1: Node
        :param node_1:
        :type node_2: Node
        :param node_2:
        """
        node_1._parent, node_2._parent = node_2._parent, node_1._parent
        node_1._l_child, node_2._l_child = node_2._l_child, node_1._l_child
        node_1._r_child, node_2._r_child = node_2._r_child, node_1._r_child



    def pop(self, number, default = None):
        pass






