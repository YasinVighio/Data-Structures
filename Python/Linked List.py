class Node:
    data=None
    nextNode=None
    def __init__(self, data=None, nxt=None):
        self.data=data
        self.nextNode=nxt
        


class LinkedList:
    
    def create(self, data):
        self.head=Node(data)
        self.counter=1
        
    def addNode(self, data):
        self.newnode=Node(data)
        self.counter+=1
        if self.head.nextNode is None:
            self.head.nextNode=self.newnode
        else:
            self.temp=self.head.nextNode
            while True:
                if self.temp.nextNode is None:
                    self.temp.nextNode=self.newnode
                    break
                else:
                    self.temp=self.temp.nextNode


    def addAtTop(self, data):
        self.newhead=Node(data, self.head)
        self.head=self.newhead
        self.counter+=1

    def insertAt(self, pos, data):
        if self.head is None:
            raise Exception("Empty List")
        
        if pos == 1:
            self.addAtTop(data)
        elif pos == self.counter:
            self.addNode(data)
        elif pos>self.counter or pos<1:
            raise Exception("Position out of bounds")
        else:
            self.position=1
            self.temp=self.head
            while True:
                if self.position == pos:
                    self.newnode=Node(data, self.temp)
                    self.lastnode.nextNode=self.newnode
                    self.counter+=1
                    break
                else:
                    self.lastnode=self.temp
                    self.temp=self.temp.nextNode
                    self.position+=1
        

    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
        self.temp=self.head
        while True:
            print(self.temp.data)
            if self.temp.nextNode is None:
                break
            self.temp=self.temp.nextNode


    def countNodes(self):
        print("There are " +str(self.counter)+ " nodes in list")


