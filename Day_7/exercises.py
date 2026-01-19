fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))
print ('Does banana in set?', 'banana' in fruits)
#To add one item to a set use the add() method
fruits.add('kiwi')
print(fruits)

#To add items from another set into the current set, use the update() method
veges = {'cucumber', 'tomato', 'potato'}
fruits.update(veges)
print(fruits)

fruits.remove('potato')
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)

#fruits = {'banana', 'orange', 'mango', 'lemon'}
#del fruits
#print(fruits)


fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(dragon.intersection(python))

# issubset() - Returns True if all items of this set is present in another set;
# Returns True if all items of this set is present in another, larger set
#issuperset() - Returns True if all items of another set is present in this set
# Returns True if all items of another, smaller set is present in this set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issuperset(even_numbers))
print(even_numbers.issuperset(whole_numbers))

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))
print(even_numbers.symmetric_difference(whole_numbers))
# print(even_numbers.difference(whole_numbers)) возвращает пустой set(), так как мы спрашиваем нам вернуть
# те элементы even_numbers,которых нет в whole_numbers, а они все есть!

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))
print(dragon.difference(python))
#It returns the symmetric difference between two sets. It means that it returns a set that contains all items from both sets,
# except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
print(dragon.symmetric_difference(python))

#If two sets do not have a common item or items we call them disjoint sets.
# We can check if two sets are joint or disjoint using isdisjoint() method

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))










