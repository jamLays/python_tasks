#1.Declare an empty list
lst = list() #= lst=[]
print(lst)

#2-4. Some operations
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(len(ages))
print(ages[0])

#6.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print(len(it_companies))
print(it_companies[0])

#12. Insert an IT company in the middle of the companies list
it_companies.insert(4,'Sber')
print(it_companies)

#13.Change one of the it_companies names to uppercase (IBM excluded!)
for_upper = it_companies[6]
print(for_upper.upper())

#14. Join the it_companies with a string '#;  '
string_for_join = '#;  '
#it_companies.extend(string_for_join)
print(it_companies)

#15. Check if a certain company exists in the it_companies list
does_exists = 'Apple'in it_companies
print(does_exists)

#16. Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

#18. Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print(it_companies[3:7])

#19. Slice out the last 3 companies from the list
print(it_companies[:3])

#20. Slice out the middle IT company or companies from the list







