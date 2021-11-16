class Node:

    def __init__(self, element=None):
        self.__element = element
        self.__next = None

    def get_element(self):
        return self.__element

    def get_next(self):
        return self.__next

    def set_element(self, elem):
        self.__element = elem

    def set_next(self, nxt):
        self.__next = nxt


class LinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.__head is None:
            return None
        return self.__head.get_element()

    def last(self):
        if self.__tail is None:
            return None
        return self.__tail.get_element()

    def add_first(self, e):
        # create a node
        newest = Node()
        # set its element to e
        newest.set_element(e)
        # have this node point at the head
        newest.set_next(self.__head)
        # update the head
        self.__head = newest
        # special case, if empty, tail is also the head
        if self.__size == 0:
            self.__tail = self.__head
        # update size
        self.__size += 1

    def add_last(self, e):
        # create a node
        newest = Node()
        # set its element to e
        newest.set_element(e)
        # have this node point at None
        newest.set_next(None)
        # special case, if empty, head is also the tail
        if self.__size == 0:
            self.__head = newest
        else:
            self.__tail.set_next(newest)
        # update the tail
        self.__tail = newest
        # update size
        self.__size += 1

    def remove_first(self):
        # special case, if empty, remove nothing
        if self.__size == 0:
            return None
        # get the head's element
        ans = self.__head.get_element()
        # the second node becomes the new head
        self.__head = self.__head.get_next()
        # update the size
        self.__size -= 1
        # if size becomes 0, this is also the tail
        if self.__size == 0:
            self.__tail == None
        return ans

    def __str__(self):
        # traverse the linked list
        ans = '('
        cursor = self.__head
        while cursor:
            ans += str(cursor.get_element()) + ', '
            cursor = cursor.get_next()
        ans = ans.rstrip(', ')
        ans += ')'
        return ans

    def __iter__(self):
        # traverse the linked list
        cursor = self.__head
        while cursor is not None:
            yield cursor.get_element()
            cursor = cursor.get_next()
