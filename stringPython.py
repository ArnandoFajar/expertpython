a = "Hello"
print(a)
print('\n')

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)
print('\n')

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)
print('\n')

# get karakter
d = "Hello, World!"
print(d[0])
print('\n')

# looping text
for x in "banana":
    print(x)

print('\n')

# String Length
e = "Hello, World!"
print(len(e))
print('\n')

# Check String
txt = "The best things in life are free!"
print("free" in txt)
print('\n')

# check string with if
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
print('\n')

# Check if Not String
txt = "The best things in life are free!"
print("expensive" not in txt)
print('\n')

# Check if Not String with if
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
