class BSTNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def distaceK(self, root, targetVal, K):

    parent = dict()
    stack = []
    stack.append(root)
    # 1. Find where the target BST node is
    # &
    # 2. How to locate the BST node
    while stack:
        node = stack.pop()
        if node == targetVal:
            target = node
        if node.left:
            stack.append(node.left)
            if not node.left in parent:
                parent[node.left] = node
        if node.right:
            stack.append(node.right)
            if not node.right in parent:
                parent[node.right] = node
    # 3. Ho2 to walk the BSTree starting from the target BST node
    visited = dict()
    worklist = []
    worklist.append(target, K)
    visited[target]=True
    answer = []

    while worklist:
        node,dist = worklist.pop(0)
        if dist == 0:
            answer.append(node.val)
            continue
        else:
            if node.left and not node.left.left in visited:
                visited[node.left] = True
                worklist.append((node.left, dist-1))
            if node.right and not node.right in visited:
                visited[node.right] = True
                worklist.append((node.right, dist-1))
            if node in parent and not parent[node] in visited:
                visited[parent[node]] = True
                worklist.append((parent[node],dist-1))

    return sorted(answer)