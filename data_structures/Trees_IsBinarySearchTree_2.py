def check_binary_search_tree_(root, lower=None, upper=None):
    if root is None or root.data is None:
        return False

    if lower is not None and root.data < lower:
        return False

    if upper is not None and root.data > upper:
        return False

    if root.left is not None:
        if root.left.data >= root.data or not check_binary_search_tree_(root.left, lower, root.data - 1):
            return False

    if root.right is not None:
        if root.right.data <= root.data or not check_binary_search_tree_(root.right, root.data + 1, upper):
            return False

    return True