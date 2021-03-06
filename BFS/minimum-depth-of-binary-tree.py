class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue=deque([])
        queue.append(root)
        level=1
        while queue:
            for i in range(len(queue)):
                current=queue.popleft()
                if not current.left and not current.right:
                    return level
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level+=1
