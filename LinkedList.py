#coding:utf-8

#Coding a Singly Linked List
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def get_value(self):
        return self.value

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
        curr_head = self.head
        node_list = []
        while curr_head != None:
            node_list.append(curr_head.get_value())
            curr_head = curr_head.next
        return node_list

    def get_value_by_index(self, index):
        curr_head = self.head
        i = 0
        while i < index:
            curr_head = curr_head.next
            i +=1
        return curr_head.get_value()

    def get_next_node(self):
        return self.head.next

    def set_next_node(self, value):
        self.next = value

    def reverse(self):
        pre = None
        curr_node = self.head
        next = None
        while curr_node != None:
            next = curr_node.next
            curr_node.next = pre
            pre = curr_node
            curr_node = next
        self.head = pre
            
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.addNode(1)
    ll.addNode(2)
    ll.addNode(8)
    print ll.get_size() 
    print ll.traverse()
    print ll.get_value_by_index(1)
    ll.reverse()
    print ll.traverse()