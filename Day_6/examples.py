#1.tuples len
fruits = ('apple', 'banana', 'orange')
len(fruits)
print(len(fruits))

#2. items
first_item = fruits[0]
print(first_item)

#3. negative items
print(fruits[-1])
print(fruits[:-1])

last_index = len(fruits) - 1
print(last_index)

#4. Slicing tuples
all_fruits = fruits[0:]
print(all_fruits)

fruits = ('apple', 'banana', 'orange', 'kiwi')
banan_orange = fruits[1:3]
print(banan_orange)

all_fruits = fruits[-4:]
print(all_fruits)

banan_orange = fruits[-3:-1]
print(banan_orange)

#5. Tuples to Lists
fruits = list(fruits)
print(fruits)

fruits = tuple(fruits)
print(fruits)

#6.Checking an Item in a Tuple
print ('banana' in fruits)

#7. Joining Tuples
veges = ('cucumber', 'tomato', 'potato' )
all = fruits+veges
print(all)

#8.Deleting Tuples
del fruits
print(fruits)





