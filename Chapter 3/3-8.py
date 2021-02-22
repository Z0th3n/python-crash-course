# Inicialize the list variable
lugares = ["cantabria", "asturias", "fiordos", "canadá", "américa"]

# Print the list
print(lugares)
print("\n")

# Print the list orderer and check if it has modified
print(sorted(lugares))
print(lugares)
print("\n")

# Print again ordered but reverse
print(sorted(lugares,reverse=True))
print(lugares)

# Using reverse
lugares.reverse()
print(lugares)

# Using sort
lugares.sort()
print(lugares)

# Using sort reversed
lugares.sort(reverse=True)
print(lugares)
