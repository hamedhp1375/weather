from idlelib.mainmenu import menudefs

numbers = int(input("number food"))
menu = {}
for i in range(numbers):
    food = (input("food"))
    number = int(input("number food"))
    menu[food] = number

max = 0
for item in menu:

    if menu[item] > max:
        max = menu[item]
        name = item
print(name, max)
