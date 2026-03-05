import random


numeros =[45, 12, 78, 23, 56]
print("lista original: ", numeros)

numeros.sort()
print("apos sort():", numeros)

numeros.sort(reverse=True)
print("apos sort():", numeros)

random.shuffle(numeros)
print("lista embralhada: ", numeros)

