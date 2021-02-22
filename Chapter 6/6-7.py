# Person exercise
people = {
    'julian': {
        'nombre': 'julian',
        'direccion': 'su casa',
        'edad': 23,
        'ciudad': 'torremolinos',
        },
    'pedro': {
        'nombre': 'pedro',
        'direccion': 'casa del campo',
        'edad': 32,
        'ciudad': 'monteperdido',
        }
    }

for persona, ficha in people.items():
    print("\nFicha: " + persona)
    print("\tNombre: " + ficha['nombre'])
    print("\tEdad: " + str(ficha['edad']))
    print("\tDirección: " + ficha['direccion'])
    print("\tCiudad: " + ficha['ciudad'])
