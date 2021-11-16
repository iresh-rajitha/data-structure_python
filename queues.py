from linkedlist import LinkedList


class LinkedQueue:

    def __init__(self):
        self.__queue = LinkedList()

    def size(self):
        return self.__queue.size()

    def is_empty(self):
        return self.__queue.is_empty()

    def first(self):
        return self.__queue.first()

    def enqueue(self, e):
        self.__queue.add_last(e)

    def dequeue(self):
        return self.__queue.remove_first()

    def __str__(self):
        return self.__queue.__str__()


class ListQueue:

    def __init__(self):
        self.__queue = list()

    def size(self):
        return len(self.__queue)

    def is_empty(self):
        return self.size() == 0

    def first(self):
        if self.is_empty():
            return None
        return self.__queue[0]

    def enqueue(self, e):
        self.__queue.append(e)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.__queue.pop(0)

    def __str__(self):
        return str(self.__queue)


