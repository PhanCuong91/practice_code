"""
define stack class to use for stack problem
"""


class Stack(object):
    def __init__(self):
        self.stack_size = 0
        self.stack = [0] * self.stack_size

    def size(self):
        return self.stack_size

    def isEmpty(self):
        if self.stack_size == 0:
            return True
        else:
            return False

    def peek(self):
        if self.stack_size == 0:
            raise ValueError('The stack is empty.')
        else:
            return self.stack[self.stack_size-1]

    def push(self, value):
        self.stack.append(value)
        self.stack_size += 1

    def pop(self):
        if self.stack_size != 0:

            self.stack_size -= 1
            return self.stack.pop()
        else:
            raise ValueError('The stack is empty.')


"""
define queue class to use for queue problem
"""


class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        # print(self.queue)

    def dequeue(self):
        if len(self.queue) == 0:
            raise ValueError('The queue is empty.')
        i = 1
        while i < len(self.queue):
            self.queue[i-1] = self.queue[i]
            i += 1
        return self.queue.pop()
        # print(self.queue)

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

if __name__ == "__main__":
    queue = Queue()
    print(queue.size())
    print(queue.isEmpty())
    # print(queue.dequeue())
    print(queue.enqueue('a'))
    print(queue.size())
    print(queue.isEmpty())
    print(queue.enqueue(20))
    print(queue.size())
    print(queue.isEmpty())
    print(queue.dequeue())
    print(queue.size())
    print(queue.isEmpty())


    # stack = Stack()
    # print(stack.size())
    # print(stack.isEmpty())
    # #print(stack.peek())
    # #print(stack.pop())
    # stack.push(10)
    # print(stack.peek())
    # print(stack.size())
    # print(stack.isEmpty())
    # print(stack.pop())
    # print(stack.size())
    # print(stack.isEmpty())
    # stack.push(20)
    # print(stack.peek())
    # print(stack.size())
    # print(stack.isEmpty())
    # print(stack.pop())
    # print(stack.size())
    # print(stack.isEmpty())
