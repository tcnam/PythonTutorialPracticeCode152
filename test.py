

def ktranguyento(number):
    dem=0;
    for i in range(number):
        if number % (i+1)==0:
            dem=dem+1
        if dem>2:
            return False
    if dem==2:
        return True
    else:
        return False


def simosaphy(first_number:float, second_number:float, number:int):
    list=[]
    list.append(first_number)
    list.append(second_number)
    for i in range(number):
        temp=list[-1]+list[-2]
        list.append(temp)
    return list

def convertNumberFromList(list):
    result=0
    for i in range(len(list)):
        result=result+list[i]*(len(list)-i)*10
    return result

def reverse(number:int):
    list=[]
    while number>=1:
        temp=number%10
        list.append(temp)
        print(temp)
        number=(number-temp)/10
    print(list)




print((reverse(356)))
list=[1,2,3]
print(len(list))
x=convertNumberFromList(list)