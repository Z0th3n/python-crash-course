# List declaration with people
lista_invitados = ["juan", "pedro", "antonio"]

# Print invitations
print(lista_invitados[0] + " está invitado a la cena.")
print(lista_invitados[1] + " está invitado a la cena.")
print(lista_invitados[2] + " está invitado a la cena.")

# A guest cannot assint

print("\n" + lista_invitados[1] + " no puede asistir a la cena.")

# Replace the person in the list who cannot attend
lista_invitados[1] = "maikel"

# Second set of invitations
print("\n" + lista_invitados[0] + " viene a la cena.")
print(lista_invitados[1] + " viene también a la cena.")
print(lista_invitados[2] + " se apunta a la cena.")

# We found a bigger table
print("\nChicos, hemos encontrado una mesa mayor.")

# Adding new guest in the beginning
lista_invitados.insert(0, 'principio')

# Adding a guest in the middle
lista_invitados.insert(2, 'medio')

# Adding a guest at the end
lista_invitados.append('final')

# New set of invitations
print("\n" +lista_invitados[0] + " está invitado a la cena.")
print(lista_invitados[1] + " está invitado a la cena.")
print(lista_invitados[2] + " está invitado a la cena.")
print(lista_invitados[3] + " está invitado a la cena.")
print(lista_invitados[4] + " está invitado a la cena.")
print(lista_invitados[5] + " está invitado a la cena.")
