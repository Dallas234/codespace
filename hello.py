
# ask user for name

name = input("Whats's your name? " )

#remove whitespace from string
name = name.strip()

#Capitalize users name
name = name.title()

#print users name
print(f"Hello, {name}")