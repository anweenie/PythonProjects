dict = {'Green Beans': '2 pounds', 'Olive Oil': '1 tablespoon', 'Butter': '3 tablespoons', 'Garlic': '2 large cloves minced', 'Red pepper': '1 tablespoon', 'Lemon Zest': '1 tablespoon', 'Salt and Pepper': 'a pinch'}
myList=['Blanch green beans in a large stock pot of well salted boiling water until bright green in color and tender crisp, roughly 2 minutes', 'Drain and shock in a bowl of ice water to stop from cooking', 'Heat a large heavy skillet over medium heat', 'Add the oil and the butter', 'Add the garlic and red pepper flakes and saute until fragrant, about 30 seconds', 'Add the beans and continue to saute until coated in the butter and heated through, about 5 minutes', 'Add lemon zest and season with salt and pepper']

for item in range(len(myList)):
    print(myList[item])

#for item in myList:
#    print (item)

for item in dict:
    print(item, ":" , dict[item])
