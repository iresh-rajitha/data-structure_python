from linkedlist import LinkedList
from doubly_linkedlist import DoublyLinkedList
from stacks import LinkedStack, ListStack
from queues import LinkedQueue, ListQueue


def diff(list1: LinkedList, list2: LinkedList):
    full_list = []
    for x in list1:
        full_list.append(x)
    for x in list2:
        full_list.append(x)

    output = []
    for f in full_list:
        if f not in output:
            output.append(f)

    new_list = LinkedList()
    for e in output:
        new_list.add_last(e);
    return new_list


def remove_max(stack: LinkedStack):
    numbers = []
    for i in range(stack.size()):
        numbers.append(stack.pop())
    numbers.remove(max(numbers))
    # print(numbers)
    new_num = LinkedStack()
    for n in reversed(numbers):
        new_num.push(n)
    return new_num


def copy_queue(queue: LinkedQueue):
    list_queue = ListQueue()
    for i in range(queue.size()):
        list_queue.enqueue(queue.dequeue())
    return list_queue


def swap(dl: DoublyLinkedList):
    temp_head = dl.first()
    temp_tail = dl.last()
    dl.remove_first()
    dl.remove_last()
    dl.add_first(temp_tail)
    dl.add_last(temp_head)
    return dl


def compare(list1: LinkedList, list2: LinkedList):
    return list1.size() == diff(list1, list2).size()


def merge(q1: ListQueue, q2: ListQueue):
    new_nums = []
    for x in range(q1.size()):
        new_nums.append(q1.dequeue())
    for x in range(q2.size()):
        new_nums.append(q2.dequeue())
    new_nums.sort()
    new_q = ListQueue()
    for e in new_nums:
        new_q.enqueue(e)
    return new_q


if __name__ == '__main__':
    print("================ 1 =====================")
    list1 = LinkedList()
    list1.add_last(1)
    list1.add_last(2)
    list1.add_last(3)
    list1.add_last(4)
    list1.add_last(5)
    print(list1)

    list2 = LinkedList()
    list2.add_last(3)
    list2.add_last(4)
    list2.add_last(5)
    list2.add_last(6)
    list2.add_last(7)
    print(list2)
    print("unique list", diff(list1, list2))

    print("================ 2 =====================")
    list1 = LinkedStack()
    list1.push(2)
    list1.push(1)
    list1.push(9)
    list1.push(8)
    list1.push(7)
    list1.push(4)
    list1.push(5)
    list1.push(6)
    print(list1)
    print("max removed list", remove_max(list1))

    print("================ 3 =====================")
    list_queue = LinkedQueue()
    list_queue.enqueue('A')
    list_queue.enqueue('B')
    list_queue.enqueue('C')
    list_queue.enqueue('D')
    list_queue.enqueue('E')
    list_queue.enqueue('F')
    list_queue.enqueue('G')
    list_queue.enqueue('H')
    print(list_queue)
    print("copy queue", copy_queue(list_queue))

    print("================ 4 =====================")
    dl = DoublyLinkedList()
    dl.add_last('A')
    dl.add_last('B')
    dl.add_last('C')
    dl.add_last('D')
    dl.add_last('E')
    dl.add_last('F')
    print(dl)
    print("swap head and tail", swap(dl))

    print("================ 5 =====================")
    list1 = LinkedList()
    list1.add_last(1)
    list1.add_last(2)
    list1.add_last(3)
    list1.add_last(4)
    list1.add_last(5)

    list2 = LinkedList()
    list2.add_last(5)
    list2.add_last(4)
    list2.add_last(3)
    list2.add_last(2)
    list2.add_last(1)

    print("Compare 2 list", compare(list1, list2))

    print("================ 6 =====================")
    q1 = ListQueue()
    q2 = ListQueue()
    q1.enqueue(2)
    q1.enqueue(11)
    q1.enqueue(19)
    q1.enqueue(21)
    q1.enqueue(23)
    q1.enqueue(24)

    q2.enqueue(3)
    q2.enqueue(9)
    q2.enqueue(15)
    q2.enqueue(16)
    q2.enqueue(22)

    print("q1", q1)
    print("q2", q2)
    print("merge", merge(q1, q2))
