notas = [7.5, 8.0, 9.5, 6.0, 8.5]
print("notas: ", notas)

print("menor:", min(notas))
print("maior:", max(notas))
print("soma:", sum(notas))
print("media:", sum(notas)) / len((notas))

nomes = ["caio", "paulo", "thiago", "fabricio"]

print("usando FOR simples:")
for nome in nomes:
    print(f"ola,  {nome} !")

print("\n usando enumerate:")
for indice, nome in enumerate(nomes):
    print(f"posicao {indice}: {nome}")

orginal = ["a", "b", "c"]
copia = list(orginal)

print("origanal:", orginal)
print("copia: ", copia)
print("sao iguais: ", orginal == copia)

copia.append("D")
print("origanal:", orginal)
print("copia: ", copia)
print("sao iguais: ", orginal == copia)
