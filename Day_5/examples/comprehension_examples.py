fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [] # empty box (Ilya taught)
for i in fruits:
    if "a" in i:
        newlist.append(i)
print('1.', newlist)

#comprehension case:
fruits_1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [i for i in fruits if "a" in i]
print('2.',newlist1)

newlist = [x for x in fruits if x != "apple"]
print('3.',newlist)

newlist = [x for x in fruits]
print('4.',newlist)

newlist = [x for x in range(10)]
print('5.',newlist)

newlist = [x for x in range(10) if x<5]
print('6.',newlist)

newlist = [x.upper() for x in fruits]
print('7.',newlist)

#comprehension case of 7
newlist=[]
for x in fruits:
    newlist.append(x.upper())
print('8.',newlist)

newlist = ['hello' for x in fruits]
print('9.',newlist)

#comprehension case of 9
newlist=[]
for x in fruits:
    newlist.append('hello')
    print(x)
    print('10.',newlist)

newlist=[x if x!="banana" else "orange" for x in fruits]
print('11.',newlist)





