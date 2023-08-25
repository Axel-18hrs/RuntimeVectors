
words = input("// Write your name or paste a text: ").split(' ')
print(words)

n = int(input("\nIngrese el tamaño del vector (numerico): "))


vector = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    vector.append(element)

print("Entered vector:", vector)
