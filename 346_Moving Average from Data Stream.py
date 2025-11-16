class Node:
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class MovingAverage:
    """
    Maintaining a window of numbers -> calculating the mean of elements inside the window
    """

    def __init__(self, size: int):
        """
        Atributes:
            - size(int): The size of the window
            - head(Node): Dummy start of the linked list
        """

        # Initialize a linked list, wired dummy head and tail together first
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head

        # Initialize size and total length of linked list -> Know length of linked list in O(1), no need to traverse in O(N)
        self.size = size
        self.length = 0

        # Avoiding recaculating sum by keep track of it in a variable
        self.total = 0
        

    def next(self, val: int) -> float:

        del_node_val = 0
        if self.length == self.size:
            del_node_val = self.head.right.val
            self.head.right = self.head.right.right
            self.length -= 1
        
        prev, nxt = self.tail.left, self.tail
        node = Node(val=val, left=prev, right=nxt)
        prev.right = node
        nxt.left = node

        self.total += val - del_node_val
        self.length += 1

        return self.total / self.length


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
