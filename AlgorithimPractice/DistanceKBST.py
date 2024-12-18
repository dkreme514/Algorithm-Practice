class BSTreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def distanceK(self, root, targetVal, k):

    parent = dict()
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        if node.val == targetVal:
            target = node
        if node.left:
            stack.append(node.left)
            if not node.left in parent:
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                if not node.right in parent:
                    parent[node.right] = node

    visited = dict()
    worklist = []
    worklist.append((target, k))
    visited[target]= True
    answer = []

    while worklist:
        node,distance = worklist.pop()
        if distance == 0:
            answer.append(node.val)
            continue
        else:
            if node.left and not node.left in visited:
                visited[node.left] = True
                worklist.append((node.left, distance - 1))
            if node.right and not node.right in visited:
                visited[node.right] = True
                worklist.append((node.right, distance -1))
            if node in parent and not parent[node] in visited:
                visited[parent[node]] = True
                worklist.append((parent[node], distance - 1))
    return sorted(answer)