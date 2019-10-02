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

    def insert(self,new_data,index):
        if (index <= 0):
            return
        temp = Node()
        temp = self.head
        counter = 0
        while(counter < index-1 and temp != None):
                temp = temp.next
                counter = counter + 1
        if(temp == None or temp.next == None):
            return
        else:
            new_Node = Node(data = new_data)
            new_Node.next = temp.next
            new_Node.pref = temp
            temp.next.pref = new_Node
            temp.next = new_Node

    def erase(self,index):
        if(index < 0 or self.head == None):
            return
        temp_pref = Node()
        temp_pref = self.head
        if (index == 0):
            self.head.next.pref = None;
            self.head = temp_pref.next
            del(temp_pref)#free()need to be defined
            return
        for i in range(index-1):
            if (temp_pref != None):
                temp_pref = temp_pref.next
        if(temp_pref == None or temp_pref.next == None):
            return
        after = Node()
        after = temp_pref.next.next
        if (after == None):
            self.tail = temp_pref
            self.tail.next = None
            del(temp_pref.next)#free()need to be defined
        else:
            del(temp_pref.next)#free()need to be defined
            temp_pref.next = after
            after.pref = temp_pref

    def print_Forward(self):
        if (self.head == None):
            print ("It's an empty list")
        else:
            Node = self.head
            while(Node != None):
                print("%s - Wind Speed: %d  MPH; Month Formed: %s; Category %d" % (Node.data.name,Node.data.maxWind,Node.data.monthFormed,Node.data.category))
                last = Node
                Node = Node.next
            print("finish Forward printing\n...........")

    def print_Reverse(self):
        if (self.head == None):
            print ("It's an empty list")
        else:
            Node = self.tail
            while(Node != None):
                print("%s - Wind Speed: %d  MPH; Month Formed: %s; Category %d" % (Node.data.name,Node.data.maxWind,Node.data.monthFormed,Node.data.category))
                Node = Node.pref
            print("finish Reverse printing\n............")

    # def print_ReverseChan(self):
    #     # self.reverse(self.tail)
    #     Node = self.tail
    #     while Node != None:
    #         print("%s - Wind Speed: %d  MPH; Month Formed: %s; Category %d" % (Node.data.name,Node.data.maxWind,Node.data.monthFormed,Node.data.category))
    #         Node = Node.pref
    #
    # def reverse(self, next_node):
    #     if next_node == None:
    #         return
    #     print("%s - Wind Speed: %d  MPH; Month Formed: %s; Category %d" % (next_node.data.name,next_node.data.maxWind,next_node.data.monthFormed,next_node.data.category))
    #     return self.reverse(next_node.pref)
