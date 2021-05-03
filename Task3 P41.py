class tool:

    def __init__(self, name, cost, image_file_name):
        self.name = name
        self.cost = cost
        self.image_file_name = image_file_name

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_image_file_name(self):
        return self.image_file_name

    def set_name(self, name):
        self.name = name
    def set_cost(self, cost):
        self.cost = cost
    def set_file_name(self, image_file_name):
        self.image_file_name = image_file_name


class shelves(tool):
    def __init__(self, shelf_height, shelf_pos, name, cost, image_file_name):
        tool.__init__(self, name, cost, image_file_name)
        self.shelf_height = shelf_height
        self.shelf_pos = shelf_pos
    def get_shelf_height(self):
        return self.shelf_height

    def get_shelf_pos(self):
        return self.shelf_pos

    def set_shelf_height(self, shelf_height):
        self.shelf_height = shelf_height

    def set_shelf_pos(self, shelf_pos):
        self.shelf_pos = shelf_pos



listarray = []
obj = shelves(0,0 ,"Spade", "$10", "spade.jpeg")
listarray.append(obj)

print(str(listarray[0].get_shelf_height())+ "|" + str(listarray[0].get_shelf_pos()) + "|" + listarray[0].get_name()+ "|" + listarray[0].get_cost() + "|" + listarray[0].get_image_file_name())


def add_Item(name, cost, image):
    nameTest = name
    nameCost = cost
    nameImage = image
    heightTest = 0
    posTest = 0
    for i in range(0, len(listarray)):

        position = 0
        storedHeight = False
        storedPos = False
        while storedHeight == False:
            if int(listarray[i].get_shelf_height()) == heightTest and int(listarray[i].get_shelf_pos()) == 10:
                heightTest = heightTest + 1

            elif heightTest == 4:
                heightTest = -1
                print("No space in the list")
                storedHeight = True
            else:
                print("Height" + str(heightTest))
                storedHeight = True

        while storedPos == False:

            if listarray[i].get_shelf_height() == heightTest:
                if listarray[i].get_shelf_pos() < posTest:
                 storedPos = True
                else:
                    posTest += 1
                    print("StoredPos" + str(posTest))
            elif listarray[i].get_shelf_height() != heightTest:
                posTest = 0
                storedPos = True


    listarray.append(shelves(heightTest, posTest, nameTest, nameCost, nameImage))


def find_tool(height, pos):

    if height == 0:
        arraylocation = height + pos
    else:
        arraylocation = (height * 10) + (pos + 1)

    print(str(listarray[arraylocation].get_shelf_height()) + "|" + str(listarray[arraylocation].get_shelf_pos()) + "|" + listarray[
        arraylocation].get_name() + "|" + listarray[arraylocation].get_cost() + "|" + listarray[arraylocation].get_image_file_name(), end=" ")
#print(str(listarray[1].get_shelf_height())+ "|" + str(listarray[1].get_shelf_pos()) + "|" + listarray[1].get_name()+ "|" + listarray[1].get_cost() + "|" + listarray[1].get_image_file_name(), end = " ")

add_Item("Sword", "120", "sword.jpeg")
add_Item("Sword", "120", "sword.jpeg")
add_Item("Sword", "120", "sword.jpeg")
add_Item("Sword", "120", "sword.jpeg")
add_Item("Sword", "120", "sword.jpeg")
add_Item("Sword", "120", "sword.jpeg")
add_Item("Sword", "121", "sword.jpeg")
add_Item("Sword", "120", "sword.jpeg")
add_Item("Sword", "120", "sword.jpeg")
add_Item("Sword", "120", "sword.jpeg")

add_Item("Sword", "121", "sword.jpeg")
add_Item("Swarm", "120", "sword.jpeg")
add_Item("Sword", "120", "sword.jpeg")


for i in range(0, len(listarray)):
    print(str(listarray[i].get_shelf_height()) + "|" + str(listarray[i].get_shelf_pos()) + "|" + listarray[
        i].get_name() + "|" + listarray[i].get_cost() + "|" + listarray[i].get_image_file_name(), end="\n")

print("\n")
find_tool(0,7)
