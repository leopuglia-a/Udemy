class Node:
    """docstring for Node."""

    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def empty(self):
        if self.root == None:
            return True
        return False

    # mostra em pre ordem (raiz -> esquerda -> direita)
    def show(self, curr_node):

        if curr_node != None:
            print('%d ' % curr_node.getLabel(), end='')
            self.show(curr_node.getLeft())
            self.show(curr_node.getRight())

    def getRoot(self):
        return self.root

    def searchNode(self, label):

         dad_node = None
         curr_node = self.getRoot()

         while curr_node.getLabel() != label:
             pass
    def insert(self, label):

        # cria novo nó
        node = Node(label)

        if self.empty():
            self.root = node
        else:

            dad_node = None
            curr_node = self.root

            while True:

                if curr_node != None:

                    dad_node = curr_node

                    if node.getLabel() < curr_node.getLabel():
                        curr_node = curr_node.getLeft()
                    else:
                        curr_node = curr_node.getRight()
                else:
                    # encontrou o nó a inserir

                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)

                    break


    def remove(self, label):

        '''
        3 casos

        Caso 1:
        nó a ser removido não possui filhos, só setar o pai para NONE

        Caso 2:
        nó a ser removido tem somente 1 filho, basta colocar o seu filho no lugar

        Caso 3:
        nó a ser removido possui 2 filhos, pegar o menor elemento da
        sub arvore à direita
        '''

        dad_node = None
        curr_node = self.getRoot()

        while curr_node != None:

            if label == curr_node.getLabel():

                # caso 1 nó folha
                if curr_node.getRight() == None and curr_node.getLeft() == None:
                    # se é raiz
                    if dad_node == None:
                        self.root = None
                    else:
                        # se é filho à esquerda ou à direita
                        if dad_node.getLeft() == curr_node:
                            dad_node.setLeft(None)
                        elif dad_node.getRight() == curr_node:
                            dad_node.setRight(None)

                #caso 2

                elif (curr_node.getLeft() == None and curr_node.getRight() != None) or \
                        (curr_node.getLeft() != None and curr_node.getRight() == None):

                        if dad_node == None:
                            if curr_node.getLeft() != None:
                                self.root = curr_node.getLeft()
                            else:
                                self.root = curr_node.getRight()

                        else:
                            if curr_node.getLeft() != None:
                                if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                                    dad_node.setLeft(curr_node.getLeft())
                                else:
                                    dad_node.setRight(curr_node.getLeft())
                            else: # senao o filho de curr_node é filho à direita
                                if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                                    dad_node.setLeft(curr_node.getRight())
                                else:
                                    dad_node.setRight(curr_node.getRight())

                # caso 3: 2 filhos
                elif curr_node.getLeft() != None and curr_node.getRight() != None:

                    dad_smaller_node = curr_node
                    smaller_node = curr_node.getRight()
                    next_smaller = curr_node.getRight().getLeft()

                    while next_smaller != None:
                        dad_smaller_node = smaller_node
                        smaller_node = next_smaller
                        next_smaller = smaller_node.getLeft()

                    if dad_node == None:
                        if self.root.getRight().getLabel() == smaller_node.getLabel():
                            smaller_node.setLeft(self.root.getLeft())
                        else:
                            '''
                            verifica se o smaller_node é o filho à esquerda ou à direita
                            para setar para None o smaller_node
                            '''
                            if dad_smaller_node.getLeft() and dad_smaller_node.getLeft().getLabel() == \
                                    smaller_node.getLabel():
                                dad_smaller_node.setLeft(None)
                            else:
                                dad_smaller_node.setRight(None)

                            # seta os filhos à direta e esquerda de smaller_node
                            smaller_node.setLeft(curr_node.getLeft())
                            smaller_node.setRight(curr_node.getRight())

                        #smaller_node vira raiz
                        self.root = smaller_node

                    else: #caso quando o nó não é raiz
                        '''
                        verifica se curr_node é filho à esquerda ou à direita
                        para setar o smaller_node como filho do pai do curr_node (dad_node)
                        '''
                        if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                            dad_node.setLeft(smaller_node)
                        else:
                            dad_node.setRight(smaller_node)

                        '''
                        verifica se o smaller_node é filho à esquerda ou à direita
                        para setar para None o smaller_node
                        '''
                        if dad_smaller_node.getLeft() and dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
                            dad_smaller_node.setLeft(None)
                        else:
                            dad_smaller_node.setRight(None)

                        # seta os filhois à direita e esquerda de smaller_node
                        smaller_node.setLeft(curr_node.getLeft())
                        smaller_node.setRight(curr_node.getRight())
                break
            dad_node = curr_node

            # percorre a arvore
            if label < curr_node.getLabel():
                curr_node = curr_node.getLeft()
            else:
                curr_node = curr_node.getRight()

t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)

t.remove(3)
t.show(t.getRoot())
print()
