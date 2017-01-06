class Deck:

    def __init__(self):
        self.deck = []
        self.length = 0

    def empty(self):
        if self.length == 0:
            return True
        return False

    def push_front(self, n):
        self.deck.insert(0, n)
        self.length += 1

    def push_back(self, n):
        self.deck.insert(self.length, n)
        self.length += 1

    def remove_front(self):
        if not self.empty():
            self.deck.pop(0)
            self.length -= 1

    def remove_back(self):
        if not self.empty():
            self.deck.pop(self.length - 1)
            self.length -= 1

    def front(self):
        if not self.empty():
            return self.deck[0]
        print("Deck is empty !")

    def back(self):
        if not self.empty():
            return self.deck[-1]
        print("Deck is empty !")

    def show_deck(self):
        for i in self.deck:
            print(i, end=' ')

d = Deck()

#insertion test
print(d.empty())
d.push_front(10) # 10
d.push_front(5) # 5 10
d.push_back(20) # 5 10 20
d.push_front(7) # 7 5 10 20
d.push_back(40) # 7 5 10 20 40
d.show_deck()

print("\nFront:", d.front())
print("Back:", d.back())

#remove test

d.remove_back() #7 5 10 20
d.remove_back() # 7 5 10
d.remove_front() # 5 10
d.show_deck()

print("\nFront:", d.front())
print("Back:", d.back())





