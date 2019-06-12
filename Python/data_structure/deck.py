# deque - double-ended queue - fila de duas pontas
# https://www.geeksforgeeks.org/deque-in-python/

class Deck:
    def __init__(self):
        self.len = 0
        self.deck = []
    
    def empty(self):
        if self.len == 0:
            return True
        return False
    
    def push_front(self, e):
        self.deck.insert(0, e)
        self.len += 1
    
    def push_back(self, e):
        self.deck.append(e)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deck.pop(0)
            self.len -= 1
    
    def pop_back(self):
        if not self.empty():
            self.deck.pop()
            self.len -= 1
    
    def front(self):
        if not self.empty():
            return self.deck[0]

    def back(self):
        if not self.empty():
            return self.deck[-1]

d = Deck()
d.push_front(10) # 10
d.push_front(5) # 5 10
d.push_back(15) # 5 10 15 
d.push_back(20) # 5 10 15 
print(d.deck)
d.pop_back()
print(d.deck)
d.pop_front()
print(d.deck)
