class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lnode = None
        self.rnode = None


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.lnode)
    preOrderTraversal(rootNode.rnode)


bt = TreeNode("Drinks")
leftchild = TreeNode("hot")
rightchild = TreeNode("cold")
hotchild = TreeNode("Tea")
coldchild = TreeNode("Cola")
leftchild.lnode = hotchild
rightchild.rnode = coldchild
bt.lnode = leftchild
bt.rnode = rightchild
preOrderTraversal(bt)
