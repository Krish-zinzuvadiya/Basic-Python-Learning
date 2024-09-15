# Dictionary :- Dictionaries are used to store data values in key:value pairs
# --> They are unordered, mutable(changeable) & don’t allow duplicate keys

info = {
    "name": "Krish",
    "subjects": ["Python", "Java", "HTML"],
    "topics": ("dictionary", "set"),
    "learning": "Coding",
    "age": 19,
    "is_adult": True,
    "marks": 86
}

print(info)
print(type(info))
print(info["name"])  # get value

info["name"] = "KrishZinzuvadiya"
print(info["name"])  # to assign or add new


# Null Dictionary
null_dict = {}
null_dict["name"] = "Krish"
print(null_dict)
