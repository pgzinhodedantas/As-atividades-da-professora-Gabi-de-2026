
numero = int(input("digite um numero inteiro positivo: "))

if numero % 2 == 0:
    resultado = numero ** 2
    print("O numero é par. Seu quadrado é:", resultado)
else:
    resultado = numero ** 3
    print("O numero é impar. Seu cubo é:", resultado)