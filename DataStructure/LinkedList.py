from pickle import FALSE, TRUE
from re import X, search
from tkinter import Y
from tkinter.messagebox import NO
from tokenize import Double


class HinhTron:
    def __init__(self,x:float,y:float,r:float)->None:
        self.__x=x
        self.__y=y
        self.__r=r

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def r(self):
        return self.__r

class NodeHinhTron:
    def __init__(self, info:HinhTron) -> None:
        self.__info=info
        self.__pNext=None

    @property
    def info(self):
        return self.__info

    @property
    def pNext(self):
        return self.__pNext

    @pNext.setter
    def pNext(self,value):
        self.__pNext=value

    def __repr__(self):
        return f"Node hình tròn có tâm:({self.__info.x},{self.__info.y}) và bán kính: {self.__info.r}"
    
    


class LinkedListHinhTron:
    def __init__(self) -> None:
        self.__pHead=None
        self.__pTail=None

    def addHead(self, node:NodeHinhTron):
        if self.__pHead == None:
            self.__pHead=node
            self.__pTail=node
        else:
            node.pNext=self.__pHead
            self.__pHead=node

    def addTail(self,node:NodeHinhTron):
        if self.__pHead == None:
            self.__pHead=node
            self.__pTail=node
        else:
            self.__pTail.pNext=node
            self.__pTail=node

    # insert node b behind node a in linked list
    def addAfter(self,a:NodeHinhTron, b: NodeHinhTron):
        if a!=None:                         #  if can't find a in linked list, insert head by default
            b.pNext=a.pNext
            a.pNext=b
            if self.__pTail==a:
                self.addTail(b)
        else:
            self.addHead(self,b)

    @staticmethod
    def equal(a:HinhTron, b:HinhTron):
        if a.r==b.r and a.x==b.x and a.y==b.y:
            return TRUE
        else:
            return FALSE
    
    def search(self, a:HinhTron):
        if self.__pHead==None:
            return
        else:
            tempNode=self.__pHead
            while tempNode!=None and self.equal(tempNode.info,a)==FALSE:
                tempNode=tempNode.pNext
            return tempNode
    
    def addAfterSpecificValue(self, a:HinhTron,b:NodeHinhTron):
        search_result=self.search(a)
        if search_result==None:
            return
        else:
            self.addAfter(search_result,b)
            
    def printListOfNodes(self):
        if self.__pHead == None:
            return
        else:
            tempNode=self.__pHead
            while tempNode !=None:
                print(tempNode)
                tempNode=tempNode.pNext

    def __repr__(self):
        return f"DS Hinh Tron có pHead:{self.__pHead}, pTail:{self.__pTail})"

DSHInhTron= LinkedListHinhTron()
DSHInhTron.addHead(NodeHinhTron(HinhTron(1,1,2)))
DSHInhTron.addTail(NodeHinhTron(HinhTron(2,2,3)))
DSHInhTron.addTail(NodeHinhTron(HinhTron(3,3,4)))
DSHInhTron.addAfterSpecificValue(HinhTron(1,1,2),NodeHinhTron(HinhTron(4,4,5)))

DSHInhTron.printListOfNodes()


    
        


