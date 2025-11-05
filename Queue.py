class queue:
    def __init__(self, size):
        self.queue = [None]*size
        self.front = 0
        self.rear = 0
        self.size = size
        self.availability = size
    def enqueue(self, item):
        if self.availability == 0:
            print("Queue Overflow")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size
            self.availability = self.availability -1
    def dequeue(self):
        if self.availability == self.size:
            print("Queue Underflow")
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.availability = self.availability +1
    def peek(self):
        print(self.queue[self.front])
    def getRear(self):
        print(self.queue[self.rear])
    def print_queue(self):
        print(self.queue)
orbital_1 = queue(6)
orbital_1.enqueue(4)
orbital_1.print_queue()
orbital_1.enqueue(7)
orbital_1.print_queue()
orbital_1.enqueue(9)
orbital_1.print_queue()
orbital_1.enqueue(1)
orbital_1.print_queue()
orbital_1.dequeue()
orbital_1.print_queue()
orbital_1.peek()
orbital_1.getRear()
