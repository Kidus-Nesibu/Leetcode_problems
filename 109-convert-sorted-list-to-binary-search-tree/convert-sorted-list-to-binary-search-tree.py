class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def getSize(node):
            size = 0
            while node:
                size += 1
                node = node.next
            return size
        
        size = getSize(head)
        self.current = head
        
        def build(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            leftChild = build(left, mid - 1)
            
            root = TreeNode(self.current.val)
            root.left = leftChild
            
            self.current = self.current.next
            
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, size - 1)
