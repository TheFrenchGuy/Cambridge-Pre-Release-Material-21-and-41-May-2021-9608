myArray = [None] * 15 #Create 15 empty arrays for the tree which holds 50 elemetns

def is_root(val):
    if myArray[0] == None:
        myArray[0] = val
    else:
        print("Val of the first root node is: " + myArray[0])
def insertLeft(val, parent):
    if (myArray[parent] == None ):
        print("Parent is not existed")
    else:
        myArray[(parent * 2) + 1] = val

def insertRight(val, parent):
    if (myArray[parent] == None ):
        print("Parent is not existed")
    else:
        myArray[(parent * 2) + 2] = val ##SO it will double it and add two, no values should overlap

def printTree(Array):
    for x in range(12):
        if myArray[x] != None:
            print(myArray[x], " ", end ="")
        else:
            print("-", ",", end =" ")

def findPos(color):
    if color in myArray:
        b = 1
        s = 0
        getIndex = myArray.index(color)
        for level in range(10):
            s= s + b
            b = b * 2

            if (getIndex < s):
                print(color, "is on level = ", level)
                break

def get_right_child(index):
    if myArray[index] != None and ((2 * index) + 2) <= 15:
        return (2* index)+2
    return -1

def get_left_child(index):
    if myArray[index] != None and ((2 * index) + 1) <= 15:
        return (2* index)+1
    return -1

def get_parent(index):
    if myArray[index] != None and index/2 != None:
        return index//2
    return -1

def inorder(index):
    if index>=0 and myArray[index] != None:
        inorder(get_left_child(index))
        print(" " + myArray[index] + " ")
        inorder(get_right_child(index))

is_root("maroon")
insertLeft("black", 0)
insertRight("silver", 0)
insertLeft("amber", 1)
insertRight("indigo", 1)
insertLeft("red", 2)
insertRight("violet", 2)
insertLeft("grey", 4)
insertRight("lime green", 4)
printTree(myArray)
print("\n")


findPos("lime green")

print("\n")

inorder(0)
