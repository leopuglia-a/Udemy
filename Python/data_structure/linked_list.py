class Node:
    def __init__(self, label):
        self.label = label
        self.next = None
    
    def getLabel(self):
        return self.label
    
    def setLabel(self, label):
        self.label = label

    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next
    
class LinkedList:
    def __init__ (self):
        self.first = None
        self.last = None
        self.len = 0
    
    def empty(self):
        if self.first == None:
            return True
        return False

    def length(self):
        return self.len
    
    def show(self):
        current_node = self.first

        while current_node != None:
            print(current_node.getLabel(), end=' ')
            current_node = current_node.getNext()
        print('')


    def push(self, label, index):

        if index >= 0:
            node  = Node(label)

            if self.empty():
                self.first = node
                self.last = node
            else:

                if index == 0:
                    node.setNext(self.first)
                    self.first = node
                elif index >= self.len:
                    self.last.setNext(node)
                    self.last = node
                else:
                    prev_node = self.first
                    current_node = self.first.getNext()
                    current_index = 1

                    while current_index != index:
                        prev_node = current_node
                        current_node = current_node.getNext()
                        current_index += 1

                    node.setNext(current_node)
                    prev_node.setNext(node)

        self.len += 1

    def pop(self, index):

        if not self.empty() and index >= 0 and index < self.len:
            
            flag_remove = False

            if self.first.getNext() == None:
                # so um elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                self.first = self.first.getNext()
                flag_remove = True
            else:

                prev_node = self.first
                current_node = self.first.getNext()
                current_index = 1

                while current_index != index:
                    prev_node = current_node
                    current_node = current_node.getNext()
                    current_index += 1
                
                prev_node.setNext(current_node.getNext())
                flag_remove = True
        
        if flag_remove:    
            self.len -= 1

lista = LinkedList()

lista.push('Marcos', 0)
lista.show()
lista.push('Maria', 1)
lista.show()
lista.push('Yankee', 0)
lista.show()
lista.push('Catarina', 2)
lista.show()
lista.push('Lilica', 4)
lista.show()
print(lista.len)

lista.pop(0)
lista.show()
lista.pop(2)
lista.show()