class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
head = None
        
def insertNodeAtTheBeginning(data):
    global head
    newNode = Node(data)
    
    if(head == None):
        head = newNode
    else:
        newNode.next = head
        head = newNode
        
def traverseLinkedList():
    current = head
    while(current):
        print(current.data, end=" ->")
        current = current.next
        
def insertNodeAtTheEnd(data):
    newNode = Node(data)
    global head
    
    if(head == None):
        head = newNode
    else:
        current = head
        while(current.next != None):
            current = current.next
        current.next = newNode
        
def insertNodeAfterGivenNode(data, node):
    global head
    newNode = Node(data)
    
    if(head == None):
        head = newNode
    else:
        current = head.next
        prev = head
        
        while(prev.data != node):
            prev = current
            current = current.next
            
            if(prev == None):
                print('The node does not exist')
                return
            
        newNode.next = current
        prev.next = newNode
    
insertNodeAtTheBeginning('Ale by The Bloomfields')
insertNodeAtTheBeginning('Sagada by Cup of Joe')
insertNodeAtTheBeginning('Palagi by TJ Monterde')

insertNodeAtTheEnd('Pantropiko by BINI')
insertNodeAtTheEnd('What by SB19')

insertNodeAfterGivenNode('Multo by Cup of Joe', 'Pantropiko by BINI')
insertNodeAfterGivenNode('Pahina by Cup of Joe', 'Pantropiko by BINI')
    
traverseLinkedList()
