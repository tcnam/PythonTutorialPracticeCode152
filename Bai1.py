# List example
from tkinter import X


mylist=["banana","cherry","apple"]
print(id(mylist))

mylist[0]="cucumber"
print(id(mylist))

#Tuple example
mytuple=(28,5,"Nam")
print(id(mytuple))
mytuple=(30,5,"Tran")
print(id(mytuple))

#Dictionary example
mydict={"name":["Nam","Tran"],"age":22,"city":"HCMCity"}
print(mydict["name"][1])

def partiionLabels(s:str):
    newList=[]
    for char in s:
        newList.append(char)
    while newList:
        temp=newList[0]
        for i in range(len(newList)):
            print(newList[i])

    print(newList)
    print(len(newList))

partiionLabels("")
newlist=[1,4,5]
sum=0
for i in range(len(newlist)):
    print(i)
    sum=sum+newlist[i]*pow(10,i)
print(sum)


print(res)