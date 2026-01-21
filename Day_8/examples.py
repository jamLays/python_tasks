#Dictionaries are used to store data values in key:value pairs
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates
# v.3.7 - dictionaries are ordered, 3.6 and earlier - dictionaries are unordered

this_dict = {
    "type": "Bug",
    "severity": "High",
    "id": 123,
    "platform": "iOS"
}

print(this_dict["severity"])
print(len(this_dict))

#Dictionaries cannot have two items with the same key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))

#there are can be lists in Dictionary
bb_dict = {
    "type": "Bug",
    "severity": ["High", "Medium", "Low"],
    "id": 123,
    "platform": "iOS"
}
print(bb_dict)
print(type(bb_dict))

#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

#dict() function for construction
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#there are can be objects(dicts) in Dictionary
me_dict = {
    "sec": "Female",
    "skills": ["qa","PostgteSQL", "Postman"],
    "address":{
        "street": "123 Main St.",
        "city": "New York",
    }
}
print(me_dict)
print(me_dict["address"])

print(me_dict.get("sec"))
print(me_dict.get("skills"))
print(me_dict.get("address"))

#Adding item to Dictionary
me_dict["hobby"] = "Fitness"
#Adding item to list into Dictionary
me_dict["skills"].append("Charles")
print(me_dict)

#Changing items
me_dict["hobby"] = "Jogging"
print(me_dict)

#Checking Keys in a Dictionary
print("hobby" in me_dict.keys())
print("city" in me_dict.keys())

#Removing Key and Value Pairs from a Dictionary
#for removing certain item
me_dict.pop("sec")
print(me_dict)

del me_dict["address"]
print(me_dict)

#for removing the last item
me_dict.popitem()
print(me_dict)

me_dict = {
    "sec": "Female",
    "skills": ["qa","PostgteSQL", "Postman"],
    "address":{
        "street": "123 Main St.",
        "city": "New York",
    }
}

#Changing Dictionary to a List of tuples - items()
print(me_dict.items())

#Clearing a Dictionary
print(me_dict.clear())

#Deleting a Dictionary
me_dict = {
    "sec": "Female",
    "skills": ["qa","PostgteSQL", "Postman"],
    "address":{
        "street": "123 Main St.",
        "city": "New York",
    }
}

#del me_dict
#print(me_dict)

#copy() Dictionaries
me_dict_copy = me_dict.copy()
print(me_dict_copy)

#Getting Dictionary Keys as a List
keys = me_dict.keys()
print(keys)

#Getting Dictionary Values as a List
values = me_dict.values()
print(values)


















