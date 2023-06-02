mylist = ["apple", "banana", "cherry", "apple", "cherry"]
print(mylist)

print("\n")

# panjang list
print(len(mylist))

print("\n")

# check type
print(type(mylist))

print("\n")

# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)

print("\n")

# acccess list items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:3])

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Append Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items
# To insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print(type(thislist))

# Remove Specified Item
# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Clear the List
# The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop Through a List
# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(i)

# Using a While Loop
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
# A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)

# Set all values in the new list to 'hello':
newlist = [x for x in fruits]
print(newlist)

# SORT LIST
# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)


# Customize Sort Function
# Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# COPY A LISTS
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# JOIN A LISTS
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
