class node:
    def __init__(self,data):
        self.data = data
        self.next = None
       
class Linkedlist:
    def __init__(self):
        self.head = None
    def add_node_end(self,value):
        a=node(value)
        if self.head is None:
            self.head=a
            return 
        curr=self.head
        while curr.next is not None:
            curr=curr.next
    
        curr.next=a
        
    def add_node_begin(self,val):
        a=node(val)
        temp=self.head
        self.head=a
        self.head.next=temp
        
    def add_node_atIndex(self,val,ind):
        curr=self.head
        a=node(val)
        count=0
        if ind == 0:
            a.next=self.head
            self.head=a
            return
        while curr:
            if count==ind-1:
                temp=curr.next #temp = 2 ,curr = 1
                curr.next=a 
                a.next=temp
                break
            curr=curr.next
            count+=1
    
    def remove_first(self):
        self.head=self.head.next
    def remove_last(self):
        curr=self.head
        while curr.next.next:
            curr=curr.next
        curr.next=None
        
            
    def printLinkedList(self):
        curr=self.head
        while curr is not None:
            print(curr.data)
            curr=curr.next
    

L=Linkedlist()
L.add_node_end(1)
L.add_node_end(2)
L.add_node_end(3)
L.add_node_end(4)
L.add_node_end(5)
L.add_node_end(6)
L.add_node_begin(0)
L.add_node_atIndex(100,1)
L.remove_first()
L.remove_last()
L.printLinkedList()




