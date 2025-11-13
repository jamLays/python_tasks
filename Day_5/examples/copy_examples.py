thislist = ["apple", "banana", "cherry"]
mylist = thislist
print('1.',mylist)

thistuple = ("apple", "banana", "cherry")
mylist = list(thistuple)
print('2.', mylist)

mylist = list(thislist)
print('3.', mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print('4.', mylist)

x=thislist.copy()
print ('5.', x)









