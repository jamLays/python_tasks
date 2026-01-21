it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1.Find the length of the set it_companies
print('1.',len(it_companies))

#2. Add 'Twitter' to it_companies
add_task = it_companies.add('Twitter')
print('2.',it_companies)

#3. Insert multiple IT companies at once to the set it_companies
for_multi = {'Sber', 'Intel', 'Cisco', 'Oracle' }
new_set = it_companies.update(for_multi)
print('3.',it_companies)

#4. Remove one of the companies from the set it_companies
it_companies.pop()
print('4. case of deleting randomly\n',it_companies)

it_companies = {'Apple', 'Cisco', 'Google', 'IBM', 'Twitter', 'Intel', 'Sber', 'Microsoft', 'Oracle', 'Amazon', 'Facebook'}
#4.1 deleting certain item
it_companies.remove('Twitter')
print('5. case of deleting certain\n',it_companies)

#Exercises: Level 2
#1. Join A and B
print('1.', A.union(B))
update_set = A.update(B)
print('1.1', A)

#2. Find A intersection B
print('2.', A.intersection(B))

#3. Is A subset of B
print('3.', A.issubset(B))

#4. Are A and B disjoint sets
print('4.', A.isdisjoint(B))

#5. Join A with B and B with A
A_union_B = A | B
print('5.', A_union_B)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#6. What is the symmetric difference between A and B
print ('6.', A.symmetric_difference(B))

#7. Delete the sets completely
#del A
#del B
#print('7.', A, B)

#Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
set_age = set(age)
print('1.', set_age)
print (len(set_age))
print(len(age))

#3. I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence? Use the split methods and set to get the unique words

sent = {'I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people'}
print('3.', len(sent))








