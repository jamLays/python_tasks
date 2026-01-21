#1. Create an empty dictionary called dog
dog = {}
print('1.', dog)

#2. Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Jack"
dog["color"] = "white"
dog.update({"breed":"jack-rassel"})
dog["legs"] = "short"
dog["age"] = 2
print('2.', dog)

#3. Create a student dictionary and add first_name, last_name, gender,
# age, marital status, skills, country, city and address as keys for the dictionary

stud_dict = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "age": 18,
    "marital status": True,
    "skills": ["python", "c++", "java"],
    "country": "Bali",
    "address": {
        "street": "123 Main St.",
        "city": "San Jose"
    }
}

#4. Get the length of the student dictionary
print('4.', len(stud_dict))

#5. Get the value of skills and check the data type, it should be a list
values = stud_dict.values()
print(values)
print(type(stud_dict.values()))

#6.Modify the skills values by adding one or two skills
stud_dict["skills"].append("kotlin")
print('6.', stud_dict)

#7. Get the dictionary keys as a list
print('7.', stud_dict.keys())

#8. Get the dictionary values as a list
print('8.', stud_dict.values())

#9. Change the dictionary to a list of tuples using items() method
print('9.', stud_dict.items())

#10. Delete one of the items in the dictionary
del stud_dict["last_name"]
print('10.', stud_dict)
stud_dict.pop("gender")
print('10.1', stud_dict)

#11. Delete one of the items in the dictionary
#del dog
#print ('11.', dog)





