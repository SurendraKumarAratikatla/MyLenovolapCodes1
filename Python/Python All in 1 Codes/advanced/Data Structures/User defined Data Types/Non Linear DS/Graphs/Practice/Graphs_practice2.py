class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " "*self.get_level()*3
        prefix = spaces + str("|___") if self.parent else ""
        print(prefix + str(self.data))
        for child in self.children:
            child.print_tree()


def built_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Lenovo"))
    laptop.add_child(TreeNode("MacNoteBook"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Vivo"))
    cellphone.add_child(TreeNode("Samsung"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("MI"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

root = built_product_tree()
root.print_tree()


