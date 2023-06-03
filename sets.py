# Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicates Not Allowed
# Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Get the Length of a Set
# To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# Add Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets
# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Join Two Sets
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
