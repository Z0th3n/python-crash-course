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

# Table is not enough
print("\nMalas noticias. Sólo caben dos personas en la mesa. Muchos que quedan fuera.")

# Removing invitations and sending messages
print("\n" + lista_invitados.pop(0) + ", lo siento, pero no estás a invitado.")
print(lista_invitados.pop(0) + ", lo siento, pero tú tampoco estás invitado.")
print(lista_invitados.pop(3) + ", tú también te quedas fuera.")
print(lista_invitados.pop(2) + ", a tí también te toca irte fuera.")

# Sending final messages
print(lista_invitados[0] + ", finalmente tú si vienes.")
print(lista_invitados[1] + ", tú también vienes.")

# Remove all the invitations
lista_invitados.remove('maikel')
lista_invitados.remove('medio')

# Print final lista_invitados
print(lista_invitados)
