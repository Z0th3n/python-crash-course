# Cities
# Declaring the dictionary cities
cities = {
    'logroño': {
        'país': 'españa',
        'población': 'unos cuantos',
        'hechos': 'hace fresco',
        },
    'lepanto': {
        'país': 'grecia',
        'población': 'un puñao',
        'hechos': 'allí se liaron a palos',
        },
    'roma': {
        'país': 'italia',
        'población': 'demasiados',
        'hechos': 'hay cosas muy bonicas',
        }
    }

# Printing the information about cities dictionary
for ciudad in cities:
    print("\n" + ciudad + ": ")
    for llave, datos in cities[ciudad].items():
        print("\t" + llave + ": " + str(datos) + ".")
