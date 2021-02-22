# # Inicialice the list pizzas
pizzas = ["jamón", "4 quesos", "picante"]

# Printing the sentence with the pizzas

for pizza in pizzas:
    print("La pizza de " + pizza + " está que te cagas.")

print("Joer, me encanta la pizza. Tanto la de " + pizzas[0] + " como la de " + pizzas[1] + ", o incluso a la de " + pizzas[2] + " están que te cagas.")

# Make a copy of the list pizzas
friends_pizzas = pizzas[:]

# Add a new pizza to the original list
pizzas.append("anchoas")
friends_pizzas.append("champiñones")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
