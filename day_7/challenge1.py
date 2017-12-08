from tree_node import TreeNode
import re

def main():
    # Parse input
    nodes = dict()
    with open('./input.txt', 'r') as input_file:
        for line in input_file:
            line = line.replace("\n", "")
            data = line.split(" ")

            node = createNode(data)
            nodes[node.name] = node

    # Construct graph
    for _, node in nodes.items():
        for child in node.children:
            nodes[child].attachParent(node)

    # Traverse graph.
    node = nodes[list(nodes.keys())[0]]
    while node.parent != None:
        node = node.parent
    
    print("The answer is: " + str(node.name))

def createNode(data):

    name = data[0]
    weight = int(data[1].strip("()"))
    children = []
    if len(data) > 3:
        for i in range(3, len(data)):
            children.append(data[i].strip(","))
    return TreeNode(name, weight, children)



if __name__ == "__main__":
    main()