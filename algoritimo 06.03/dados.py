quadrados = [x**2 for x in range(1,11)]
print("quadrados:", quadrados)

pares = [x for x in range(1,21) if x % 2 == 0]
print("pares:", pares)

vogais = [letra for letra in "programacao" if letra in "aeiou"]
print("vogais: ", vogais)
