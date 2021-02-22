# Declare the list
lista = ["uno", "dos", "tres", "cuatro"]

# Using all the functions involved in lists
lista.append("cinco")
print(lista)

lista.insert(0, "cero")
print(lista)

del lista[0]
print(lista)

lista.pop(0)
print(lista)

lista.remove("cinco")
print(lista)

lista.sort()
print(lista)

print(sorted(lista))

lista.reverse()
print(lista)

print(len(lista))
print(lista[-1])
