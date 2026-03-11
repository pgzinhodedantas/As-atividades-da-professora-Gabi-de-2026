contato = {
    "@camila" : "camila", 
    "@paolla" : "paolla",
    "@sheron" : "sheron",
    "@bruna"  : "bruna"
}

print("chaves:")
for insta in contato.keys():
    print(insta)

print("\n valores: ")
for nome in contato.values():
    print(nome)

print("\n pares: ")
for insta, nome in contato.items():
     print(f"{insta} --> {nome}")

contato = {
    "@camila" : 1.70,
    "@paolla" : 1.80,
    "@sheron" : 1.55,
    "@bruna"  : 1.60
}

print("ordenada por chave:")
for insta in sorted(contato.keys()): 
    print(f"{insta} --> {contato[insta]:.2f}m")

from operator import itemgetter
print("\n ordenado por valor (altura):")
for insta, estatura in sorted(contato.items(), key = itemgetter(1)):
   print(f"{insta} --> {estatura: .2f}m")

