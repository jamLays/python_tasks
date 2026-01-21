fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort()
print('1.', fruits)
# "sort" sorts ASC by default

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print('2.',thislist)

fruits.reverse() # /thislist.sort(reverse = True)
print('3.', fruits)

def myfunc(n):
    return abs(n-50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print('4.', thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print('5.', thislist)
#sort - case sensitive, resulting in all capital letters being sorted before lower case letters


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print('6.', thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print('7.', thislist)
#reverses the current sorting order of the elements out of alphabet




