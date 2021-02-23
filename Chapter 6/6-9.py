# Favorite places exercise

favorite_places = {
    'peter': ["londres", "paris", "torremolinos"],
    'juanjo': ["cataluña", "paris", "júpiter"],
    'rodri': ["infierno", "zeneta", "camberra"],
    }

for nombre in favorite_places:
    print("\nNombre: " + nombre.title())
    for lugares in favorite_places[nombre]:
        print("\tLugar: " + lugares.title())
