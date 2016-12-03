# waht is the problem with MyQueue?
class MyQueue:
    def __init__(self):
        self._head = None
        self._tail = None

    def put(self, item):
        if self._head is None:
            self._head = QueueObject(item)
            self._tail = self._head
        else:
            self._tail.set_next(QueueObject(item))
            self._tail = self._tail.get_next()

    def get(self):
        if not self.empty():
            temp = self._head.get_value()
            self._head = self._head.get_next()
            if self._head is None:
                self._tail = None
            return temp

    def empty(self):
        return self._head is None

class QueueObject:
    def __init__(self, value):
        self._value = value
        self._next = None

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_next(self, nextQ):
        self._next = nextQ

class GoodQueue:
    def __init__(self):
        self._data = []

    def put(self, item):
        self._data.append(item)

    def get(self):
        if not self.empty():
            return self._data.pop(0)

    def empty(self):
        return len(self._data) == 0