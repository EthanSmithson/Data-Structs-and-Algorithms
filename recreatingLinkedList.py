class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def getCurr(self):
        return self.val
    
    def setCurr(self, val):
        self.val = val

    def getNxt(self):
         return self.next

    def setNxt(self, val):
        self.next = val

class LinkedList():
    def __init__(self, head = None):
        self.head = head
        self.count = 1

    def insert(self, data):
        head = self.head
        newNode = Node(data)
        newNode.setNxt(head)
        self.head = newNode
        self.count += 1         

    def showList(self):
         curr = self.head
         while curr is not None:
              print(curr.data)
              curr = curr.getNxt()

    def remove(self, val):
        curr = self.head
        prev = None
        while curr is not None:
            if curr.data == val:
                break
            prev = curr
            curr = curr.getNxt()

        if curr == None:
            raise ValueError(f'{val} is not in the list!!!')
        
        if prev == None:
            self.head = curr.next
            self.count -= 1
        else:
            prev.setNxt(curr.getNxt())
            self.count -= 1

    def reverseList(self):
        curr = self.head
        prev = None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def get_count(self):
        return self.count
    
    def is_empty(self):
        return self.head == None
    
    def find(self, val):
        item = self.head
        while item != None:
            if item.get_data() == val:
                return item.val
            else :
                item = item.get_next()
        return None

    

list = LinkedList()
list.insert(15)
list.insert(25)
list.insert(35)
list.reverseList()
list.showList()
        