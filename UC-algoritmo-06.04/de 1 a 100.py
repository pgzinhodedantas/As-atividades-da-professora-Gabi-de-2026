import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print(" adivinhar o número entre 1 e 100!")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("maior")
    elif palpite > numero_secreto:
        print("menor")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break