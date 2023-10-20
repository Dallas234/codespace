
# ask user for name captialize and remove space

name = input("Whats's your name? " ).strip().title()

#split user name into first and last name
first, last = name.split("")


#print users name
print(f"Hello, {name}")