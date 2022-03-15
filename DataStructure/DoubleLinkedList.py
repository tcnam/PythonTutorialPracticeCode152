

from re import search


class Diem:
    def __init__(self,x:float, y:float, z:float ) :
        self.__x=x
        self.__y=y
        self.__z=z
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self,value):
        self.__x=value

    @y.setter
    def y(self,value):
        self.__y=value

    @z.setter
    def z(self, value):
        self.__z=value
    
    def __repr__(self) :
        return f"({self.__x},{self.__y},{self.__z})"

class NodeDiem:
    def __init__(self,info:Diem):
        self.__info=info
        self.__pNext=None
        self.__pPrev=None

    @property
    def info(self):
        return self.__info

    @property
    def pNext(self):
        return self.__pNext

    @property
    def pPrev(self):
        return self.__pPrev

    @info.setter
    def info(self, value):
        self.__info=value

    @pNext.setter
    def pNext(self,value):
        self.__pNext=value

    @pPrev.setter
    def pPrev(self, value):
        self.__pPrev=value

    def __repr__(self) :
        return f"Node diem co toa do:{self.info}"
    
class DoubleLinkedListDiem:
    def __init__(self):
        self.__pHead=None
        self.__pTail=None

    @property
    def pHead(self):
        return self.__pHead

    @property
    def pTail(self):
        return self.__pTail

    @pHead.setter
    def pHead(self, value):
        self.__pHead=value

    @pTail.setter
    def pTail(self, value):
        self.__pTail=value

    def printListOfNodes(self):
        if self.__pHead == None:
            return
        else:
            tempNode=self.__pHead
            while(tempNode!=None):
                print(tempNode)
                tempNode=tempNode.pNext

    def addHead(self,value:NodeDiem):
        if self.__pHead==None:
            self.__pHead=value
            self.__pTail=value
        else:
            value.pNext=self.__pHead
            self.__pHead.pPrev=value
            self.__pHead=value
            

    def addTail(self, value:NodeDiem):
        if self.__pHead==None:
            self.__pHead=value
            self.__pTail=value
        else:
            value.pPrev=self.__pTail
            self.__pTail.pNext=value
            self.__pTail=value

    #defalut addHead node b if node a is None
    def addAfter(self, a:NodeDiem, b:NodeDiem):
        if a!=None:
            b.pPrev=a
            b.pNext=a.pNext
            if a.pNext!=None:           ## in case node a is pTail
                a.pNext.pPrev=b
            a.pNext=b
            if a==self.__pTail:
                self.__pTail=b;
        else:
            self.addHead(b)

    #default addTail node b if node a is None
    def addBefore(self, a:NodeDiem, b:NodeDiem):
        if a!=None:
            b.pNext=a
            b.pPrev=a.pPrev
            if a.pPrev!=None:           ##in case a is pHead
                a.pPrev.pNext=b
            a.pPrev=b
            if a==self.__pHead:
                self.__pHead=b
        else:
            self.addTail(b)
            
    def addAfterSpecificDiem(self,x:Diem,b:NodeDiem):
        self.addAfter(self.search(x),b)

    def addBeforeSpecificDiem(self,x:Diem,b:NodeDiem):
        self.addBefore(self.search(x),b)

    @staticmethod
    def equal(a:Diem, b:Diem):
        if a.x==b.x and a.y==b.y and a.z==b.z:
            return True
        else:
            return False

    def search(self, x:Diem):
        tempNode=self.__pHead
        while tempNode!=None and DoubleLinkedListDiem.equal(tempNode.info,x)==False:
            tempNode=tempNode.pNext
        return tempNode



a=NodeDiem(Diem(1,2,3))
b=NodeDiem(Diem(4,5,6))
c=NodeDiem(Diem(7,8,9))
d=NodeDiem(Diem(10,11,12))
e=NodeDiem(Diem(13,14,15))
f=NodeDiem(Diem(16,17,18))

double_linked_list=DoubleLinkedListDiem()
double_linked_list.addHead(a)
double_linked_list.addHead(b)
double_linked_list.addTail(c)
double_linked_list.addHead(d)
double_linked_list.printListOfNodes()
print("Danh sach sau khi them:")
double_linked_list.addAfterSpecificDiem(Diem(10,11,12),e)
double_linked_list.addBeforeSpecificDiem(Diem(4,5,6),f)
double_linked_list.printListOfNodes()
    