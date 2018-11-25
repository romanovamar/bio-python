class QueueNode:
    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode):
        """ Initializes new node """
        self.elem = elem
        self.nextnode = nextnode


class QueueIterator:
    """ QueueIterator: Iterator for LinkedQueue """

    def __init__(self, node, emptynode):
        """ Initializes new Iterator """
        self.node = node
        self.length = emptynode

    def __next__(self):
        """ Returns next element of queue: next(iter) """
        if self.length == 0:
            raise StopIteration
        else:
            elem = self.node.elem
            self.node = self.node.nextnode
            self.length -= 1
            return elem


class LinkedQueue:
    """ LinkedQueue """

    def __init__(self):
        """ Initializes new queue """
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, elem):
        """ Pushes 'elem' to queue """
        self.length += 1
        if self.head == None:
            self.tail = self.head = QueueNode(elem, None)
        else:
            self.tail.nextnode = self.tail = QueueNode(elem, None)

    def pop(self):
        """ Removes front of queue and returns it """
        elem = self.head.elem
        self.head = self.head.nextnode
        self.length = self.length - 1
        return elem

    def front(self):
        """ Returns front of queue """
        return self.head.elem

    def empty(self):
        """ Checks whether queue is empty """
        return self.length == 0

    def __iter__(self):
        """ Returns Iterator for queue: iter(queue) """
        return QueueIterator(self.head, self.length)

    def __len__(self):
        """ Returns size of queue: len(queue) """
        return self.length

    def clear(self):
        """ Makes queue empty """
        self.__init__()
