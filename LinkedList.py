#coding:utf-8

#Coding a Singly Linked List
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def addNode(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = node 
   
    def get_size(self):
        curr_head = self.head
        count = 0
        while curr_head != None:
            count +=1
            curr_head = curr_head.next
        return count    

    """
    1.head 为none :head-->node
    2.tail.nex-->node
    :param data:
    :return:
    """
    def traverse(self):
        node = self
        while node != None:
            print node.value
            node = node.next
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.addNode(1)
    ll.addNode(2)
    print ll.get_size() 