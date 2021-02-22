# Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

lista = ['pedro', 'sarah', 'antonio', 'fernando', 'edward']

# looping through the list to find people who didn't take the poll
for nombre in lista:
    if nombre in favorite_languages.keys():
        print(nombre + ", gracias por realizar el cuestionario")
    else:
        print(nombre + ", debes hacer la encuesta.")
