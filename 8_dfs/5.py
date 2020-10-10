class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return count_paths_r(root, S, [])


def count_paths_r(root, S, paths):
    if root is None:
        return 0

    count = 0
    cur_sum = 0
    paths.append(root.val)

    for i in range(len(paths) - 1, -1, -1):
        cur_sum += paths[i]
        if cur_sum == S:
            count += 1
    count += count_paths_r(root.left, S, paths)
    count += count_paths_r(root.right, S, paths)

    del paths[-1]

    return count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
