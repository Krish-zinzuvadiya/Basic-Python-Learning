# Dictionary Methods
info = {
    "name": "Krish",
    "subjects": ["Python", "Java", "HTML"],
    "topics": ("dictionary", "set"),
    "learning": "Coding",
    "age": 19,
    "is_adult": True,
    "marks": 86
}

# returns all keys
print(info.keys())
print("Length of dict : ", len(info))


# returns all values
print(info.values())

# returns all (key, val) pairs as tuples
print(info.items())

# returns the key according to value
print(info.get("marks"))

# inserts the specified items to the dictionary
info.update({"city ": "Gujrat"})
print(info)
