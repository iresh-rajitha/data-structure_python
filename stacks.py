from linkedlist import LinkedList


class LinkedStack:

    def __init__(self):
        self.__stack = LinkedList()

    def size(self):
        return self.__stack.size()

    def is_empty(self):
        return self.__stack.is_empty()

    def top(self):
        return self.__stack.first()

    def push(self, e):
        self.__stack.add_first(e)

    def pop(self):
        return self.__stack.remove_first()

    def __str__(self):
        return self.__stack.__str__()


class ListStack:

    def __init__(self):
        self.__stack = list()

    def size(self):
        return len(self.__stack)

    def is_empty(self):
        return self.size() == 0

    def top(self):
        if self.is_empty():
            return None
        return self.__stack[-1]

    def push(self, e):
        # append e to the list
        self.__stack.append(e)

    def pop(self):
        if self.is_empty():
            return None
        # remove the last element
        return self.__stack.pop()

    def __str__(self):
        return str(self.__stack)

