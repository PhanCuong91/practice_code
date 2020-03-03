import stack_queue


class queue_2_stack(object):
    def __init__(self):
        self.stack_1 = stack_queue.Stack()
        self.stack_2 = stack_queue.Stack()

    def push(self, value):
        self.stack_1.push(value)

    def pop(self):
        if self.stack_2.isEmpty() == True:
            for i in range(self.stack_1.size()):
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()


queue = queue_2_stack()
queue.push(1)
queue.push(2)
print(queue.pop())
queue.push(3)
print(queue.pop())
print(queue.pop())