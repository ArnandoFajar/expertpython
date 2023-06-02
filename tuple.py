# TUPLE
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
# To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))


# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)


# ACCESS TUPLES
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
# Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
