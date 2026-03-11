aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
aluno["nota1"] = float(input("Digite a nota da prova 1: "))
aluno["nota2"] = float(input("Digite a nota da prova 2: "))

media = (aluno["nota1"] + aluno["nota2"]) / 2

aluno["media"] = media

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\n dados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave} : {valor}")
    print("situação:", situacao)