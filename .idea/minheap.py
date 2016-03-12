#! /usr/bin/env python


from __future__ import print_function, division


class Node(object):
    """
    This class creates Node with two parameters: item(eny object)
     and priority(integer number)
     :type _item: any
     :type _priority: int
    """
    def __init__(self, item, priority):
        self._item = item
        self._priority = priority

    @property
    def item(self):
        return self._item

    @property
    def priority(self):
        return self._priority

    def __str__(self):
        return str((self.item, self.priority))

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
        return self.priority == other.priority

    def __gt__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.priority > other.priority

    def __ge__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.priority >= other.priority

    def __lt__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.priority < other.priority

    def __le__(self, other):
        """
        :type other: Node
        :return: True or False
        """
        return self.priority <= other.priority


class MinHeap(object):
    """
    This class creates binary MinHeap object realized on list. Parent of node
    have idx = (idx of node) // 2.
    Children of node have idxs = (idx of node) * 2 and ((idx of node) * 2) + 1.
    Priority of child node can't be more then priority of the parent node.
    Parent node can have only two children
    :type _heap: list
    """
    def __init__(self):
        self._heap = [0] # 0 in heap nided for nodes numeration begining with 1

    def __len__(self):
        return len(self._heap) - 1 # len must not count first "0"

    def __nonzero__(self):
        return bool(len(self)) # heap with only "0" inside must be "False"

    def _exchange(self, i, j):
        """
        Exchange two nodes in heap verticaly
        :type i: int
        :param i: index of node in list
        :type j: int
        :param j: index of node in list
        :return: None
        """
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _percolate_up(self):
        """
        This prosidure percolate up last added node
        :return: None
        """
        cur_pos = len(self)
        while cur_pos // 2 > 0:
            parent_idx = self._parent_idx(cur_pos)
            if self._heap[cur_pos] >= self._heap[parent_idx]:
                break
            self._exchange(cur_pos, parent_idx)
            cur_pos //= 2

    def _percolate_down(self):
        """
        This prosidure percolate down head node of the heap after pop_min
        :return: None
        """
        i = 1
        while (i * 2) <= len(self):
            min_child_index = self._min_child_idx(i)
            if self._heap[i] > self._heap[min_child_index]:
                self._exchange(i, min_child_index)
            i = min_child_index

    def _min_child_idx(self, i):
        """
        Return indrx of the child node with minimum priority
        :type i: int
        :param i: idx of the node in heap
        :return: idx of the child node with minimum priority
        """
        children_indices = self._children_indices(i)
        if not children_indices:
            return None
        children = [self._heap[idx] for idx in children_indices]
        return sorted(zip(children, children_indices))[0][1]

    @staticmethod
    def _parent_idx(i):
        """
        Return index of the parent node of the node with index "i"
        :type i: int
        :param i: idx of the node
        :return: idx of the parent node
        """
        return i // 2

    def _children_indices(self, i):
        """
        Return tuple with indices of cildren inside
        :type i: int
        :param i: index of node in heap
        :return: (indices of children)
        """
        possible_children = [i * 2, (i * 2) + 1]
        return tuple(idx for idx in possible_children if idx <= len(self))

    def get_min(self):
        """
        Return hed node of the heap
        :return: hed node of the heap
        :raise ValueError when heap is empty
        """
        if not self:
            raise ValueError("The heap is empty")
        return self._heap[1]

    def pop_min(self):
        """
        This function pop head of heap
        :return: head of the heap
        """
        min_val = self.get_min()
        self._exchange(1, len(self))
        self._heap.pop()
        self._percolate_down()
        return min_val

    def push(self, item):
        """
        Add new node in heap
        :type item: Node
        :param item: new node
        :return None
        :raise ValueError when item is not Node
        """
        if not isinstance(item, Node):
            raise ValueError("`item` should be a `Node` instance")
        self._heap.append(item)
        self._percolate_up()



def test_heap():
    heap = MinHeap()
    nodes = [Node(val, val) for val in xrange(9, -1, -1)]
    for node in nodes:
        heap.push(node)
    while heap:
        print(heap.pop_min())


def main():
    test_heap()

if __name__ == "__main__":
    main()