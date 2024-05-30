class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)


# Example usage:
queue = Queue()

queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

print("Current queue size:", queue.size())
print("Front item of the queue:", queue.peek())

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

print("Current queue size:", queue.size())
print("Front item of the queue:", queue.peek())