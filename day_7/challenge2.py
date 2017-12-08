from tree_node import TreeNode
from collections import Counter

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

    # Traverse graph to find root
    node = nodes[list(nodes.keys())[0]]
    while node.parent != None:
        node = node.parent
    
    calculateNetWeight(node, nodes)
    print(findIncorrectWeight(node, nodes))

def createNode(data):

    name = data[0]
    weight = int(data[1].strip("()"))
    children = []
    if len(data) > 3:
        for i in range(3, len(data)):
            children.append(data[i].strip(","))
    return TreeNode(name, weight, children)

def calculateNetWeight(root, nodes):

    net_weight = root.weight
    for child_name in root.children:
        net_weight += calculateNetWeight(nodes[child_name], nodes)
    root.netWeight = net_weight
    return net_weight

def findIncorrectWeight(root, nodes):

    children_weight = [nodes[child_name].netWeight for child_name in root.children]

    # Find the wrong child
    counter = Counter(children_weight)
    wrong_child = [nodes[child_name] for child_name in root.children if nodes[child_name].netWeight == min(counter, key=counter.get)]

    if len(wrong_child) > 1:
        # We are the incorrect one, need to be the same as our siblings
        sibling_weight = [nodes[sibling_name] for sibling_name in root.parent.children if sibling_name != root.name][1].netWeight
        total_child_weight = sum(children_weight)
        return sibling_weight - total_child_weight
    else:
        return findIncorrectWeight(wrong_child[0], nodes)

if __name__ == "__main__":
    main()