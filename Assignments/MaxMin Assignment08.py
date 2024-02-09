
import random
mylist = []

def mymax(list):
    maxnum = 0
    for i in list:
        if i > maxnum:
            maxnum=i
    return maxnum

def mymin(list):
    minnum = list[0]
    for i in list:
        if i < minnum:
            minnum=i    
    return minnum


def MakeList(number):
    
    for i in range(0, number):
        radnumb = random.randrange(100)
        mylist.append(radnumb)
    



usernum = int(input("Please input a number: "))
MakeList(usernum)
print(mylist)
print("My max number: \t\t", mymax(mylist))
print("Python's max number: \t", max(mylist))
print("My min number: \t\t", mymin(mylist))
print("Python's min number: \t", min(mylist))