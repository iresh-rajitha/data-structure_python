class Node:

    def __init__(self, element=None):
        self.__element = element
        self.__prev = None
        self.__next = None

    def get_element(self):
        return self.__element

    def get_prev(self):
        return self.__prev

    def get_next(self):
        return self.__next

    def set_element(self, elem):
        self.__element = elem

    def set_prev(self, prv):
        self.__prev = prv

    def set_next(self, nxt):
        self.__next = nxt


class DoublyLinkedList:

    def __init__(self):
        self.__size = 0
        self.__header = Node()
        self.__trailer = Node()
        # link header and trailer
        self.__header.set_next(self.__trailer)
        self.__trailer.set_prev(self.__header)

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.__size == 0:
            return None
        return self.__header.get_next().get_element()

    def last(self):
        if self.__size == 0:
            return None
        return self.__trailer.get_prev().get_element()

    def __add_between(self, e, p, s):
        # create a new node
        newest = Node(e)
        # link the new node to predecessor and successor
        # p <--> newest <--> s
        newest.set_prev(p)
        newest.set_next(s)
        p.set_next(newest)
        s.set_prev(newest)
        # update size
        self.__size += 1

    def add_first(self, e):
        # header <--> e <--> header.next
        self.__add_between(e, self.__header, self.__header.get_next())

    def add_last(self, e):
        # trailer.prev <--> e <--> trailer
        self.__add_between(e, self.__trailer.get_prev(), self.__trailer)

    def __remove(self, node):
        # prv <--> node <--> nxt
        prv = node.get_prev()
        nxt = node.get_next()
        # link the predecessor and the successor
        # prv <--> nxt
        prv.set_next(nxt)
        nxt.set_prev(prv)
        # update size
        self.__size -= 1
        # have the node point at itself to help garbage collection
        node.set_next(node)
        node.set_prev(node)
        return node.get_element()

    def remove_first(self):
        if self.__size == 0:
            return None
        # remove header.next
        return self.__remove(self.__header.get_next())

    def remove_last(self):
        if self.__size == 0:
            return None
        # remove trailer.prev
        return self.__remove(self.__trailer.get_prev())

    def __str__(self):
        ans = '('
        cursor = self.__header.get_next()
        while cursor is not self.__trailer:
            ans += str(cursor.get_element()) + ', '
            cursor = cursor.get_next()
        ans = ans.rstrip(', ')
        ans += ')'
        return ans

    def __iter__(self):
        cursor = self.__header.get_next()
        while cursor is not self.__trailer:
            yield cursor.get_element()
            cursor = cursor.get_next()
