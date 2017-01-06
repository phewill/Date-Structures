class Queue:

    def __init__(self):
        self.queue = []
        self.length = 0

    def push(self, n):
        self.queue.append(n)
        self.length += 1

    def remove(self):
        self.queue.pop(0)
        self.length -= 1

    def final(self):
        if not self.empty():
            return self.queue[-1]
        print("Empty !")

    def front(self):
        if not self.empty():
            return self.queue[0]
        print("Empty !")

    def empty(self):
        if self.length == 0:
            return True
        return False

    def length(self):
        return self.length


x = Queue()

x.push(10)
x.push(20)
x.push(30)
print(x.final())
print(x.front())
x.remove()
print(x.length)
print(x.final())
print(x.front())
print(x.empty())
x.remove()
x.remove()
print(x.empty())