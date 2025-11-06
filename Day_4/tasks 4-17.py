from http.cookiejar import uppercase_escaped_char

company_name = "Coding For All"
#6.Change all the characters to uppercase letters using upper() method.
print(company_name.upper())
#7.Change all the characters to lowercase letters using lower() method.
print(company_name.lower())
#8.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company_name.capitalize())
print('title ', company_name.title())
print(company_name.swapcase())
#9.Cut(slice) out the first word of Coding For All string.
slice_example=company_name[7:]
print(slice_example)
#10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
look_for='Coding'
print(company_name.index(look_for))
print(company_name.find(look_for))
print(company_name.startswith(look_for))
#11. Replace the word coding in the string 'Coding For All' to Python
print(company_name.replace('Coding', 'Python'))
#12. Change Python for Everyone to Python for All using the replace method or other methods.
print(company_name.replace('All', 'Everyone'))
#13. Split the string 'Coding For All' using space as the separator
print(company_name.split())
#14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
string_for_split = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(string_for_split.split(','))
zero_index = company_name[0]
print(zero_index)
#15. What is the last index of the string Coding For All.
last_index = company_name[-1]
print(last_index)
#16. What character is at index 10 in "Coding For All" string
tenth_index = company_name[10:11]
print(tenth_index)
#17.Create an acronym or an abbreviation for the name 'Python For Everyone'
python_string = 'Python For Everyone'
first_symb = python_string[0]
second_symb = python_string[7]
third_symb = python_string[11]
print(first_symb, second_symb, third_symb)





