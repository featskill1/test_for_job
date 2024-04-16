class CircularBufferList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.capacity

    def enqueue(self, item):
        if self.is_full():
            self.buffer.pop(0)
        self.buffer.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        return self.buffer.pop(0)


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    @staticmethod
    def count_index(ind, cap):
        return (ind + 1) % cap

    def enqueue(self, item):
        if self.is_full():
            self.dequeue()
        self.buffer[self.tail] = item
        self.tail = count_index(self.tail, self.capacity)
        if self.tail == self.head:
            self.head = count_index(self.head, self.capacity)
        else:
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = count_index(self.head, self.capacity)
        self.size -= 1
        return item

#Опять же в первом случае код проще и лаконичнее, во втором лучше быстродействие.
#В обоих случаях все операции имеют сложность O(1), кроме enqueue, которая в первом случае имеет O(capacity),
#т.к. операция удаления из начала массива вызывает сдвиг всех элементов массива, поэтому при частом добавлении
#элементов сверх capacity первая функция будет отрабадывать значительно дольше.

