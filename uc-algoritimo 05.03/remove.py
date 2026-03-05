nomes =[ "alvaro", "thiago", "fabrcio", "caio"]
print("nomes:", nomes )

nomes.remove("thiago")
print("lista atualizada: ", nomes)

removido = nomes.pop(1)
print(f"removido : {removido}")
print("apos pop(): ", nomes)

del nomes [0]
print("apos del nomes [0]", nomes)

nomes.clear()
print("lista atualizada: ", nomes)

