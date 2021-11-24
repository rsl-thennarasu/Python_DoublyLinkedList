class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
  
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
           
        else:
            new_node = Node(data)
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node
            new_node.next = None
            
 
    def prepend(self, data):
    
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
    def DeleteAtStart(self):
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None;

    def delete_at_end(self):
  
        if self.head is None:
            print("The Linked list is empty, no element to delete")
            return 
        if self.head.next is None:
            self.start_node = None
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.prev.next = None

    def Display(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            curr_node = self.head
            while curr_node is not None:
                print(curr_node.data , end=" ")
                curr_node = curr_node.next
    def search(self, data):
        i=0
        if self.head is None:
            print("The list is empty")
            return
        else:
            curr_node = self.head
            if curr_node.data == data:
                print(i)
            else:
                i+=1
            while curr_node.next is not None:
                curr_node = curr_node.next
                if curr_node.data == data:
                    print(data," is present in the position : ",i)
                    return
                i+=1
            
        

NewDoublyLinkedList = doublyLinkedList()

NewDoublyLinkedList.append(10)
NewDoublyLinkedList.append(20)
NewDoublyLinkedList.append(30)
NewDoublyLinkedList.append(40)
NewDoublyLinkedList.prepend(50)
NewDoublyLinkedList.prepend(60)
NewDoublyLinkedList.delete_at_end()
NewDoublyLinkedList.search(20)


NewDoublyLinkedList.Display()

