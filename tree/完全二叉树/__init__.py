from tree import TreeNode, build_tree, print_tree

def build_complete_tree() -> TreeNode:
    return build_tree([1, 2, 3, 4, None, None, None, None, None])

if __name__ == "__main__":
    print_tree(build_complete_tree())