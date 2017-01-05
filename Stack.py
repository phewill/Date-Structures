class Stack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, n):
        self.stack.append(n)
        self.length += 1

    def remove(self):
        if not self.empty():
            self.stack.pop(self.length - 1)
            self.length -= 1

    def top(self):
        if not self.empty():
            return self.stack[-1]
        print('Empty stack !')

    def empty(self):
        if self.length == 0:
            return True
        return False

    def length(self):
        return self.length

x = Stack()

x.push(2)
x.push(3)
x.push(4)
x.push(7)
print("Top ",x.top())
x.remove()
print("Top ",x.top())
print(x.length)
print(x.empty())