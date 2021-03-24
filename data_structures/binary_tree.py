class TreeNode:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def set_left(self, value):
        self.right_child = TreeNode(value, self)
        return self.right_child


class BinaryTree:
    def __init__(self, example=False):
        self.root = None
        if example:
            self.root = TreeNode(1, None)
            self.root.left_child = TreeNode(2, self.root)
            self.root.right_child = TreeNode(3, self.root)
            node4 = TreeNode(4, self.root.right_child)
            self.root.right_child.left_child = node4

    def get_root(self):
        return self.root

    def print_tree_preorder(self, node):
        if node is None:
            return
        print(node.value)
        # if node.left_child is not None:
        self.print_tree_preorder(node.left_child)
        # if node.right_child is not None:
        self.print_tree_preorder(node.right_child)
        return

    def print_tree_inorder(self, node):
        if node is None:
            return
        self.print_tree_inorder(node.left_child)
        print(node.value)
        self.print_tree_inorder(node.right_child)
        return

    def print_tree_postorder(self, node):
        if node is None:
            return
        self.print_tree_postorder(node.left_child)
        self.print_tree_postorder(node.right_child)
        print(node.value)
        return

    def search_preorder_in_without_rule(self, node, goal):
        if node is None:
            return None
        if node.value == goal:
            return node
        # left = self.search_preorder(node.right_child, goal)
        # right = self.search_preorder(node.right_child, goal)
        # if left is not None:
        #     return left
        # elif right is not None:
        #     return right
        # return None
        return self.search_preorder_in_without_rule(node.left_child, goal) or \
               self.search_preorder_in_without_rule(node.right_child, goal)

    def search_preorder_in_rule(self, node, goal):
        if node is None:
            return None
        if node.value == goal:  # TODO: Remember the difference between "is" and "==".
            return node  # TODO: Also remember function "id()" in python and "id(5) - id(4)".
        elif goal < node.value:
            return self.search_preorder_in_rule(node.left_child, goal)
        return self.search_preorder_in_rule(node.right_child, goal)

    def insert(self, node, value, parent=None, child=None):
        if node is None:
            if self.root is None:
                self.root = TreeNode(value, None)
                return self.root
            node = TreeNode(value, parent)
            if child == "left":
                parent.left_child = node
            else:
                parent.right_child = node
            return node
        if value <= node.value:  # Remember the "=" in "<=".
            return self.insert(node.left_child, value, node, child="left")
        else:
            return self.insert(node.right_child, value, node, child="right")

    def insert_opt(self, node, value):
        # if node.value == value     # If we wanted to make a tree without \
        #     return node               # redundant nodes.
        if node is None:
            self.root = TreeNode(value, None)
            return self.root
        if value <= node.value:
            if node.left_child is None:
                node.left_child = TreeNode(value, node)
                return node.left_child
            return self.insert_opt(node.left_child, value)
        if node.right_child is None:
            node.right_child = TreeNode(value, node)
            return node.right_child
        return self.insert_opt(node.right_child, value)

    def delete(self, node):
        if node is None:
            raise Exception("There is no such node exits.")

        has_parent = False
        is_left_child = False
        is_right_child = False
        if node.parent is not None:
            has_parent = True
            is_left_child = node.parent.left_child is node

        has_left = node.left_child is not None
        has_right = node.right_child is not None

        if not has_left and not has_right:
            if has_parent is False:
                self.root = None
                del node
                return
            if is_left_child:
                node.parent.left_child = None
            else:
                node.parent.right_child = None
            del node
            return

        elif has_left is False:
            if has_parent is False:
                self.root = node.right_child
                node.right_child.parent = None
                del node
                return
            if is_left_child:
                node.parent.left_child = node.right_child
            else:
                node.parent.right_child = node.right_child
            del node
            return

        elif has_right is False:
            if has_parent is False:
                self.root = node.left_child
                node.left_child.parent = None
                del node
                return
            if is_left_child:
                node.parent.left_child = node.left_child
            else:
                node.parent.right_child = node.left_child
            del node
            return

        left_of_right_node = node.right_child.left_child
        last_right_of_left_node = node.left_child.right_child

        node.left_child.parent = node.parent
        if has_parent is not False:
            if is_left_child:
                node.parent.left_child = node.left_child
            else:
                node.parent.right_child = node.left_child

        if last_right_of_left_node is None:
            node.left_child.right_child = node.right_child
            node.right_child.parent = node.left_child
            del node
            return

        while last_right_of_left_node.right_child is not None:
            last_right_of_left_node = last_right_of_left_node.right_child

        last_right_of_left_node.right_child = left_of_right_node
        if left_of_right_node is not None:
            left_of_right_node.parent = last_right_of_left_node

        node.right_child.left_child = last_right_of_left_node
        last_right_of_left_node.parent = node.right_child
        node.left_child.right_child = node.right_child
        node.right_child.parent = node.left_child
        del node
        return

    def delete_opt(self, node):
        if node is None:
            raise Exception("There is no such node.")

        has_parent = False
        is_left_child = False
        is_right_child = False
        if node.parent is not None:
            has_parent = True
            is_left_child = node.parent.left_child is node
            is_right_child = node.parent.right_child is node

        has_left = node.left_child is not None
        has_right = node.right_child is not None

        if not has_left and not has_right:
            if has_parent is False:
                self.root = None
                del node
                return
            if is_left_child:
                node.parent.left_child = None
            else:
                node.parent.right_child = None
            del node
            return

        elif has_left is False:
            if has_parent is False:
                self.root = node.right_child
                node.right_child.parent = None
                del node
                return
            if is_left_child:
                node.parent.left_child = node.right_child
            else:
                node.parent.right_child = node.right_child
            del node
            return

        elif has_right is False:  # With one check we avoid Tetha(log(n)) to find the last right of the left.
            if has_parent is False:
                self.root = node.left_child
                node.left_child.parent = None
                del node
                return
            if is_left_child:
                node.parent.left_child = node.left_child
            else:
                node.parent.right_child = node.left_child
            del node
            return

        if node.left_child.right_child is None:
            node.left_child.right_child = node.right_child
            node.right_child.parent = node.left_child
            del node
            return

        last_right_of_left_node = node.left_child
        while last_right_of_left_node.right_child is not None:
            last_right_of_left_node = last_right_of_left_node.right_child

        node.value = last_right_of_left_node.value

        # self.delete_opt(last_right_of_left_node)
        if last_right_of_left_node.left_child is not None:
            last_right_of_left_node.left_child.parent = last_right_of_left_node.parent
        last_right_of_left_node.parent.right_child = last_right_of_left_node.left_child
        del last_right_of_left_node
        return

    def delete_clean(self, node):
        if node is None:
            raise Exception("Node does not exist.")

        if node.right_child is None:
            self.replace(node, node.lef_child)

        elif node.left_child is None:
            self.replace(node, node.right_child)

        else:
            max_of_left = node.left_child
            while max_of_left.right_child is not None:
                max_of_left = max_of_left.right_child

            node.value = max_of_left.value
            self.delete_clean(max_of_left)

    def replace(self, parent, child):
        if self.root == parent:  # Or we can use this statement: "if parent.parent is None:"
            self.root = child

        elif parent.parent.left_child is parent:
            parent.parent.left_child = child

        else:
            parent.parent.right_child = child

        if child is not None:
            child.parent = parent.parent  # Warning: Do not forget to do this.
        del parent
        return

    def least_common_ancestor(self, candidate, node1, node2):
        if candidate == node1 or candidate == node2:  # This is for when we have redundant values.
            return candidate

        if node1.value <= candidate.value and node2.value <= candidate.value:
            return self.least_common_ancestor(candidate.left_child, node1, node2)

        elif node1.value > candidate.value and node2.value > candidate.value:
            return self.least_common_ancestor(candidate.right_child, node1, node2)

        return candidate
