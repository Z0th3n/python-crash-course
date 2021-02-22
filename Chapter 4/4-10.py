# Declaring a list with all cubes from 1 to 10
cubos = [valor ** 3 for valor in range(1,11)]

print(cubos)

# Print some messages to do the exercise

print("The first three itmes in the lista are:")
print(cubos[:3])
print("Three items from the middle of the list are:")
print(cubos[int((len(cubos)/2)-(len(cubos)/4)):int((len(cubos)/2)+(len(cubos)/4)n)])
print("The last three items in the list are:")
print(cubos[-3:])
