# Favorite Numbers
# Favorite numbers exercise
favorite_numbers = {
    'julian' : [10, 5],
    'perico' : [7],
    'johnny' : [2, 5, 3],
    'mariano' : [19, 3],
    'julianchi' : [2],
    }

print(favorite_numbers)

for nombre in favorite_numbers.keys():
    print("\nEstos son los favoritos de " + nombre + " :")
    for favoritos in favorite_numbers[nombre]:
        print(favoritos)
