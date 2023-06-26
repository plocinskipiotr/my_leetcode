class TreeNode():

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree():

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, head: TreeNode, node: TreeNode):
        if head is None:
            head = node

        if head.val > node.val:
            if head.left is None:
                head.left = node
            else:
                self.insert(head.left, node)

        if head.val < node.val:
            if head.right is None:
                head.right = node
            else:
                self.insert(head.right, node)

    def traverse_in_order(self, node: TreeNode, res: list[int]):
        if node != None:
            self.traverse_in_order(node.left, res)
            res.append(node.val)
            self.traverse_in_order(node.right, res)

        return res

    def traverse_in_order_stack(self, root: TreeNode):
        stack: list[TreeNode] = list()
        res: list[int] = list()

        while root is not None or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res
