class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")


# Example usage:
stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

print("Current stack size:", stack.size())
print("Top item of the stack:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)

print("Current stack size:", stack.size())
print("Top item of the stack:", stack.peek())