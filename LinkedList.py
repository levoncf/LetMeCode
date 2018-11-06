#coding:utf-8

#Coding a Singly Linked List
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)

    def addNode(self, value):
        new_node = Node(value)
        curr_node = self.head
        if curr_node is None:
            pass
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def get_length(self):
        curr_head = self.head
        count = 0
        while curr_head != None:
            count +=1
            curr_head = curr_head.next
        return count  
    def print_ll(self):
        curr_head = self.head
        count = 0
        while curr_head!= None:
            print("node: {} is {}".format(count, curr_head.value))
            curr_head = curr_head.next
            count += 1
            

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
        while curr_node != None:
            tmp_next = curr_node.next
            curr_node.next = pre
            pre = curr_node
            curr_node = tmp_next
        self.head = pre

class Solution:
    def reverse_kth_element(self, head, k):
        dummy = LinkedList(0)
        dummy.next = head.next
        prev = dummy
        while prev:
            prev = self.reverse_k(prev, k)
        return dummy.next

    def reverse(self, head):
        pre = None
        curr_node = head
        while curr_node != None:
            tmp_next = curr_node.next
            curr_node.next = pre
            pre = curr_node
            curr_node = tmp_next
        return pre

    def reverse_k(self, head, k):
        n1 = head.next
        nk = self.find_kth(head, k)
        if nk == None:
            return
        nk_plus = nk.next
        nk.next = None
        nk = self.reverse(n1)
        head.next = nk
        n1.next = nk_plus
        return n1

    def find_kth(self, head, k):
        curr = head
        for i in range(k):
            if curr == None:
                return None
            curr = curr.next
        return curr

    def print_curr_node(self, head):
        print(head.value)

    def print_LL(self, head):
        curr_head = head
        count = 0
        while curr_head!= None:
            print("node: {} is {}".format(count, curr_head.value))
            curr_head = curr_head.next
            count += 1
            
        return None
            
if __name__ == '__main__':
    ll = LinkedList()
    ll.addNode(1)
    ll.addNode(2)
    ll.addNode(3)
    ll.addNode(4)
    ll.addNode(5)
    ll.addNode(6)
    ll.addNode(7)
    #ll.print_ll()
    sol = Solution()
    new_ll = sol.reverse_kth_element(ll.head, 2)
    sol.print_LL(new_ll)
    
    #print ll.get_size() 
    #print ll.traverse()
    #print ll.get_value_by_index(1)
    #ll.reverse()
    #print ll.traverse()
