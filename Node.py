class Storm():
    def __init__(self,name,maxWind,monthFormed,category):
        self.name = name
        self.maxWind = maxWind
        self.monthFormed = monthFormed
        self.category = category

class Node():
    def __init__(self,next = None,pref = None,data = None):
        self.data = data
        self.next = next
        self.pref = pref

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, new_data):
        new_node = Node(data = new_data)
        new_node.next = self.head
        new_node.pref = None
        if (self.head != None):
            self.head.pref = new_node
        if (self.head == None):
            self.tail = new_node
        self.head = new_node

    def push_back(self,new_data):
        new_node = Node(data = new_data)
        new_node.pref = self.tail
        new_node.next = None
        if (self.tail != None):
            self.tail.next = new_node
        if (self.tail == None):
            self.head = new_node
        self.tail = new_node

    def print_forward(self):
        if (self.head == None):
            print ("It's an empty list")
        else:
            Node = self.head
            while(Node != None):
                print("%s - Wind Speed: %d  MPH; Month Formed: %s; Category %d" % (Node.data.name,Node.data.maxWind,Node.data.monthFormed,Node.data.category))
                last = Node
                Node = Node.next
            print("finish printing")

    def print_Reverse(self):
        if (self.head == None):
            print ("It's an empty list")
        else:
            Node = self.tail
            while(Node != None):
                print("%s - Wind Speed: %d  MPH; Month Formed: %s; Category %d" % (Node.data.name,Node.data.maxWind,Node.data.monthFormed,Node.data.category))
                last = Node
                Node = Node.pref
            print("finish printing")
