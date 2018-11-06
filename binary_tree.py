
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    # A function to do inorder tree traversal 
    def printInorder(self, root): 
    
        if root: 
            # First recur on left child 
            self.printInorder(root.left) 
            print(root.val)
            # now recur on right child 
            self.printInorder(root.right) 
    def maxDepth(self, root):
        if root is None:
            print("none")
            return 0
        else:
            print("not")
        #left
        left = self.maxDepth(root.left)
        #right
        right = self.maxDepth(root.right)
        print (left)
        return max(left, right) + 1

    def binaryTreePaths(self, root):
        #print(root.val)
        # write your code here
        if root is None:
            return []
        if root.left is None and root.right is None:
            return str(root.val)
        #1.defination
        result = []
        #split
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        

        #merge
        for path in left_paths:
            #print(type(left_paths))
            path_str = str(root.val) + "->" + str(path)
            result.append(path_str)
        for path in right_paths:
            path_str = str(root.val) + "->" + str(path)
            result.append(path_str)
        return result

    def BFS_level_of_order(self, root):
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            queue_size = len(queue)
            element_in_curr_layer = []
            for item in queue:
                element_in_curr_layer.append(item.val)
            result.append(element_in_curr_layer)
            for i in range(queue_size):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return result

    def serialize(self, root):
        # write your code here
        elements_in_curr_layer = []
        queue = [root]
        if root is None:
            return []
        while queue:
            for item in queue:
                print item
                if item == "#":
                    elements_in_curr_layer.append("#")
                else:
                    elements_in_curr_layer.append(item.val)
            queue_size = len(queue)
            for i in range(queue_size):
                node = queue.pop(0)
                if node == "#":
                    continue
                if node.left is not None:
                    queue.append(node.left)
                else: 
                    queue.append("#")
                if node.right is not None:
                    queue.append(node.right)
                else: 
                    queue.append("#")
            while elements_in_curr_layer[-1] == '#':
                elements_in_curr_layer.pop()
        return elements_in_curr_layer
 
    def deserialize(self, data):
        root = data[0]
        tree = TreeNode(root)
        index = 1
        data_len = len(data)
        while index < data_len:
            if data[index] == "#":
                pass
        return tree


if __name__ == '__main__':
    # Driver code 
    root = TreeNode(1) 
    root.left      = TreeNode(2) 
    root.right     = TreeNode(3) 
    root.left.left  = TreeNode(None) 
    root.left.right  = TreeNode(5)
    root.right.left  = TreeNode(6) 
    root.right.right  = TreeNode(7) 
    solution = Solution()

    #solution.printInorder(root)
    print solution.BFS_level_of_order(root)
    #result = solution.serialize(root)
    #print result

    #solution.printInorder(root)
    #solution.binaryTreePaths(root)
    #print result
    #max_depth = solution.maxDepth(root)
    #print "max_depth: " + str(max_depth)