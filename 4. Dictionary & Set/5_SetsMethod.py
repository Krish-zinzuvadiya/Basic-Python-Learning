# Set Methods

collection = {1, 2, 3, 4, 5, 6, 7}

# adds an element
collection.add(8)
print(collection)

# removes the elem an
collection.remove(2)
print(collection)

col1 = {1, 2, 3}
print(col1)

# empties the set
col1.clear()
print(col1)

# removes a random value
collection.pop()
print(collection)

collection2 = {8, 9, 4}
# combines both set values & returns new
print(collection.union(collection2))

# combines common values & returns new
print(collection.intersection(collection2))
