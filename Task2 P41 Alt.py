#Task 2.3
class Node():
    def __init__(self, Data, LeftPointer, RightPointer):
        self.Data = Data
        self.LeftPointer = LeftPointer  # The null pointer will be used as -1 to show it doesnt branch out
        self.RightPointer = RightPointer  # The null pointer will be used as -1 to show it doesnt branch out


Maroon = Node("Maroon", 1, 2)
Black = Node("Black", 3, 4)
Amber = Node("Amber", -1, -1)
Indigo = Node("Indigo", 7, 8)
Grey = Node("Grey", 13, -1)
Lime_Green = Node("Lime Green", -1, -1)
Blue = Node("Blue", -1, 14)
Fushia = Node("Fushia", -1, -1)
Silver = Node("Silver", 5, 6)
Red = Node("Red", 9, -1)
Pink = Node("Pink", -1, 12)
Purple = Node("Purple", -1, -1)
Violet = Node("Violet", 10, 11)
Yellow = Node("Yellow", -1, -1)
Turquoise = Node("Turquoise", -1, -1)

BinaryTree = [Maroon, Black, Silver, Amber, Indigo, Red, Violet, Grey, Lime_Green, Pink, Turquoise, Yellow, Purple,
              Blue, Fushia]

#Task 2.4
def addToTree(colourname):
    x = 0
    added = False
    while added == False:
        pos = 0
        if colourname > BinaryTree[x].Data:
            if BinaryTree[x].RightPointer == -1:
                BinaryTree.append(Node(colourname, -1, -1))
                pos = len(BinaryTree) - 1

                print("Pos of Right", pos)
                BinaryTree[x].RightPointer = pos
                added = True
            else:
                x = BinaryTree[x].RightPointer
                print("Next Value right", x)
        else:
            if BinaryTree[x].LeftPointer == -1:
                BinaryTree.append(Node(colourname, -1, -1))
                #for i in range(len(BinaryTree)):
                #    print(len(BinaryTree))
                    #if BinaryTree[i] == Node(colourname, -1, -1):
                    #    pos = i
                    #    break
                pos = len(BinaryTree) - 1

                print("Pos of Left", pos)
                BinaryTree[x].LeftPointer = pos
                added = True
            else:
                x = BinaryTree[x].LeftPointer
                print("Next Value left", x)


addToTree("Aan")
addToTree("Ano")

print(BinaryTree[3].LeftPointer)
print(BinaryTree[3].RightPointer)


#Task 2.5
def findInTree(colourName):
    pos = 0
    x = 0
    indexFound = False

    while indexFound == False:
        if colourName == BinaryTree[x].Data:
            return x

        elif colourName > BinaryTree[x].Data:
            x = BinaryTree[x].RightPointer
        elif colourName < BinaryTree[x].Data:
            x = BinaryTree[x].LeftPointer


print("The position is ", findInTree("Purple"))

#Task2.6
def outputTree(index):
    print(BinaryTree.sort(key=lambda node: node.Data))
    for x in range(len(BinaryTree)):
        print(BinaryTree[x].Data)
outputTree(0)