class Storm():
    def __init__(self, name, maxWind, monthFormed, category):
        self.name = name
        self.maxWind = maxWind
        self.monthFormed = monthFormed
        self.category = category


class Node():
    def __init__(self, next=None, pref=None, data=None):
        self.data = data
        self.next = next
        self.pref = pref


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.pref = None
        if (self.head != None):
            self.head.pref = new_node
        if (self.head == None):
            self.tail = new_node
        self.head = new_node

    def push_back(self, new_data):
        new_node = Node(data=new_data)
        new_node.pref = self.tail
        new_node.next = None
        if (self.tail != None):
            self.tail.next = new_node
        if (self.tail == None):
            self.head = new_node
        self.tail = new_node

    def insert(self, new_data, index):
        if index <= 0:
            return
        temp = Node()
        temp = self.head
        counter = 0
        while counter < index - 1 and temp is not None:
            temp = temp.next
            counter = counter + 1
        if temp is None or temp.next is None:
            return
        else:
            new_Node = Node(data=new_data)
            new_Node.next = temp.next
            new_Node.pref = temp
            temp.next.pref = new_Node
            temp.next = new_Node

    def erase(self, index):
        if index < 0 or self.head is None:
            return
        temp_pref = Node()
        temp_pref = self.head
        if index == 0:
            self.head.next.pref = None;
            self.head = temp_pref.next
            del temp_pref
            return
        for i in range(index - 1):
            if temp_pref is not None:
                temp_pref = temp_pref.next
        if temp_pref is None or temp_pref.next is None:
            return
        after = Node()
        after = temp_pref.next.next
        if after is None:
            self.tail = temp_pref
            self.tail.next = None
            del temp_pref.next
        else:
            del temp_pref.next
            temp_pref.next = after
            after.pref = temp_pref

    def print_Node(self, Node):
        print("%s - Wind Speed: %d  MPH; Month Formed: %s; Category %d" % (
            Node.data.name, Node.data.maxWind, Node.data.monthFormed, Node.data.category))

    def print_Forward(self):
        if self.head is None:
            print("It's an empty list")
        else:
            Node = self.head
            while Node is not None:
                self.print_Node(Node)
                last = Node
                Node = Node.next
            print("finish Forward printing\n...........")

    def print_Reverse(self):
        if self.head is None:
            print("It's an empty list")
        else:
            Node = self.tail
            while Node is not None:
                self.print_Node(Node)
                Node = Node.pref
            print("finish Reverse printing\n............")

    def get_size(self):
        count = 0
        temp = self.head
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def bubble_sort_list(self):
        size = self.get_size()
        for i in range(size - 1):
            temp = self.head
            for j in range(size - 1):
                t1 = temp
                t2 = temp.next
                if t1.data.maxWind > t2.data.maxWind:
                    t = t2.data
                    t2.data = t1.data
                    t1.data = t
                temp = temp.next

    def linear_search_month(self, search_value):
        temp = self.head
        size = self.get_size()
        count = 0
        if temp is None:
            return None
        for i in range(size - 1):
            if temp.data.monthFormed == search_value:
                self.print_Node(temp)
                count = count + 1
            temp = temp.next
        if count == 0:
            print("No storms found.")

    def linear_search_category(self, search_value):
        if 0 <= search_value <= 5:
            temp = self.head
            size = self.get_size()
            count = 0
            if temp is None:
                return None
            for i in range(size - 1):
                if temp.data.category == search_value:
                    self.print_Node(temp)
                    count = count + 1
                temp = temp.next
            if count == 0:
                print("No storms found.")
        else:
            print("Invalid category.")

    def linear_search_name(self, search_value):
        temp = self.head
        size = self.get_size()
        count = 0
        if temp is None:
            return None
        for i in range(size - 1):
            if temp.data.name == search_value:
                self.print_Node(temp)
                count = count + 1
            temp = temp.next
        if count == 0:
            print("No storms found.")

    # def insertionSort(self):
    #     if (self.head == None):
    #         return
    #     size = self.get_size()
    #     sort = self.head.next
    #     temp = Node()
    #     for i in range (size):
    #         temp = sort.pref
    #         sort_value = sort.data.maxWind
    #         while (temp != None and temp.data.maxWind > sort_value):
    #             t = temp.data.maxWind
    #             temp.next.data.maxWind = t
    #             temp = temp.pref
    #         sort = sort.next

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
