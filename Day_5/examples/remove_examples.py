thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print('1.', thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print('2.',thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print('3.',thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print('4.',thislist)
#pop deletes last

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print('5.',thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist
# print('6.',thislist)
# #this will cause an error because you have succsesfully deleted "thislist"

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print('7.',thislist)
#clear - items, but remains list


