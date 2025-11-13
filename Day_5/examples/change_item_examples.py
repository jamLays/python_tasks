thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist_1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist_1[1:3] = ["blackcurrant", "watermelon"]
print(thislist_1)

#If you insert more items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly
thislist_2 = ["apple", "banana", "cherry"]
thislist_2[1:2] = ["blackcurrant", "watermelon"]
print(thislist_2)

#If you insert less items than you replace, the new items will be inserted where you specified,
# and the remaining items will move accordingly
thislist_3 = ["apple", "banana", "cherry"]
thislist_3[1:3] = ["watermelon"]
print(thislist_3)

thislist_4 = ["apple", "banana", "cherry"]
thislist_4.insert(2, "watermelon")
print(thislist_4)

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

thislist_5 = ["apple", "banana", "cherry"]
thislist_5.insert(1, "orange")
print(thislist_5)

list = ["apple", "banana", "cherry"]
tuple = ("kiwi", "orange")
list.extend(tuple)
print(list)
