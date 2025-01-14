class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, val):
        newVal = Node(val)
        if self.rear == None:
            self.front = self.rear = newVal
            self.length += 1
            return
        self.rear.next = newVal
        self.rear = newVal
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty!!!"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data


    def isEmpty(self):
        return self.length == 0
    
    def showQueue(self):
        front = self.front
        while front:
            print(front.data)
            front = front.next

    def peek(self):
        if self.isEmpty():
            return "Queue is empty!!!"
        return self.front.data

        


queue = Queue()
queue.enqueue(15)
queue.enqueue(25)
queue.enqueue(35)
queue.dequeue()
queue.dequeue()
queue.dequeue()
# queue.showQueue()
print(queue.peek())

