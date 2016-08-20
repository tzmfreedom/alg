#!/usr/bin/env python


class Queue(object):
    def __init__(self):
        self.enq_stack = []
        self.deq_stack = []

    def enqueue(self, elem):
        self.enq_stack.append(elem)
        return elem

    def dequeue(self):
        if len(self.deq_stack) == 0:
            while(len(self.enq_stack) > 0):
                self.deq_stack.append(self.enq_stack.pop())
        if len(self.deq_stack) == 0:
            return None
        return self.deq_stack.pop()

if __name__ == '__main__':
    q = Queue()
    q.enqueue("hoge1")
    q.enqueue("hoge2")
    q.enqueue("hoge3")
    q.enqueue("hoge4")

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
