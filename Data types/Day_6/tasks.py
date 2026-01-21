#1. Create an empty tuple
empty_tuple = ()
print(empty_tuple)

empty_tuple = tuple()
print('1.', empty_tuple)

#2-4.Create a tuple containing names of your sisters and your brothers. Join

brothers = ('Jack', 'Mike', 'Dastin')
sisters = ('Jane', 'Mim', 'Lil')
siblings = brothers + sisters
print('2.',siblings)

count = len(siblings)
print('3.',count)

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father_mather = ('Il', 'Lays')
family_members = siblings + father_mather
print('5.',family_members)

#6. Unpack siblings and parents from family_members
print (family_members[:6])
print (family_members[0:6])
print (family_members[:-2])

#7. Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
veges = ('cucumber', 'tomato', 'potato')
animals = ('zebro', 'leo', 'rabbit')
food_stuff_tp = fruits + veges + animals
print('7.',food_stuff_tp)

#8.Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)
print('8.',food_stuff_tp)

#9.Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
print('9.',food_stuff_tp[2:7])

#10. Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_tp[0:4]
last_three = food_stuff_tp[-3:]
all = first_three + last_three
print('10.',all)

#11. Delete the food_staff_tp tuple completely
#del (food_stuff_tp)
#print('11.',food_stuff_tp)

#12. Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print ('12.1', 'Estonia' in nordic_countries)
print ('12.2', 'Iceland' in nordic_countries)







