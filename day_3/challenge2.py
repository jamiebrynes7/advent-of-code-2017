import sys
import math

def main():

    # Get input arguments.
    try:
        target_value = int(sys.argv[1])
    except IndexError:
        print("Usage: python challenge1.py <target_value>")
        exit(1)

    nodes = [Node(0, 0)]
    nodes[0].value = 1
    square_size = 1

    while True:
        coords = getListOfCoords(square_size)
        for coord in coords:
            x, y = coord
            node = Node(x, y)
            node.findAdjacentNodes(nodes)
            value = node.calculateNodeValue()
            if value > target_value:
                print("The answer is: " + str(value))
                return
            print("Calculated value of node at {0},{1} to be {2}.".format(x,y,value))
            nodes.append(node)
        square_size += 1

def getListOfCoords(square_size):
    coords = []
    x = square_size
    y = -square_size + 1

    # Go along right edge
    for i in range(y,square_size):
        coords.append((x,i))
    y = square_size

    # Go along top edge
    for i in range(x, -square_size, -1):
        coords.append((i,y))
    x = -square_size

    # Go along left edge
    for i in range(y, -square_size, -1):
        coords.append((x,i))
    y = -square_size

    # Go along bottom edge
    for i in range(x, square_size + 1):
        coords.append((i,x))

    return coords


class Node :

    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        self.adjacent_nodes = []
        self.value = 0
    
    def findAdjacentNodes(self, node_list):
        for node in node_list:
            if abs(node.x_coord - self.x_coord) <= 1 and abs(node.y_coord - self.y_coord) <= 1:
                self.adjacent_nodes.append(node)

    def calculateNodeValue(self):
        self.value = sum(node.value for node in self.adjacent_nodes)
        return self.value


if __name__ == "__main__":
    main()
