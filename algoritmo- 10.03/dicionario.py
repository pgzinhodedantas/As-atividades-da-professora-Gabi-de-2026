matricula1 = 2026001
nome1 = "paulo guilherme"
telefone = "8762-1945"

aluno = {
     "matricula": 2026001,
     "nome" : "paulo guilherme",
     "telefone" : "8762-1945"
}

print(aluno)

contato = {
   "@camilaqueiroz" : "camila queiroz",
   "@brunamarquezine" : " bruna M.",
   "@sheronmenezes" : "sheron M.",
   "@paolaoliveira" : "paola O."
}

print(contato)
print(type(contato))

print(contato["@camilaqueiroz"])

print(contato.get("@paolaoliveira"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "não encontrado"))

contato["@giovanna"] = "giovanna"
print("apos add: ", contato)

contato["@paolaolievira"] = "paola Olievira"
print("apos add: ", contato)

contato.update({
     "@brunamarquezine" : "bruna marquezine",
     "@camilaqueiroz": "camila Q."
})

print("apos atualização:", contato)


removido = contato.pop("paolaolievira")
print(f"removido: {removido}")
print("apos o pop:", contato)

del contato["@camilaqueiroz"]
print("apos o del:", contato)

copia = dict(contato)
contato.clear()
print("apos clear:", contato)
print("copia:", copia)


print("número de contato: ", len(contato))

if "@joao" in contato:
    print(f"encontrado: {contato['@joao']}")

if  "@inexistente" in contato:
    print("existe")
else:
    print("não existe.")

  