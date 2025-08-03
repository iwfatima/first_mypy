print("Chocolate = 15$")
print("Nutella = 17$")
print("Blueberry = 13$")
print("Strawberry = 12$")
print("Lemon = 7$")

ice1 = input("Person 1: choose ice cream: ")
ice2 = input("Person 2: choose ice cream: ")
ice3 = input("Person 3: choose ice cream: ")

if ice1 == "chocolate":
    price1 = 15
elif ice1 == "nutella":
    price1 = 17
elif ice1 == "blueberry":
    price1 = 13
elif ice1 == "strawberry":
    price1 = 12
elif ice1 == "lemon":
    price1 = 7
else:
    price1 = 0

if ice2 == "chocolate":
    price2 = 15
elif ice2 == "nutella":
    price2 = 17
elif ice2 == "blueberry":
    price2 = 13
elif ice2 == "strawberry":
    price2 = 12
elif ice2 == "lemon":
    price2 = 7
else:
    price2 = 0

if ice3 == "chocolate":
    price3 = 15
elif ice3 == "nutella":
    price3 = 17
elif ice3 == "blueberry":
    price3 = 13
elif ice3 == "strawberry":
    price3 = 12
elif ice3 == "lemon":
    price3 = 7
else:
    price3 = 0

total = price1 + price2 + price3
print("Total price: $", total)