import random
sides = ['nachos', 'mashed potatoes', 'macaroni and cheese', 'guacamole', 'broccoli']
mainDishes = ['pizza', 'hamburger', 'sandwich', 'ribs', 'chicken']
dessert = ['custard', 'cheesecake', 'apple pie', 'chocolate brownie', 'ice cream']
print(sides[random.randint(0,4)] + " " + mainDishes[random.randint(0,4)] + " " + dessert[random.randint(0,4)])
