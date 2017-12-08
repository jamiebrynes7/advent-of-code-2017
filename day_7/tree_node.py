class TreeNode:

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = None
        self.netWeight = 0
    
    def attachParent(self, parent):
        self.parent = parent
