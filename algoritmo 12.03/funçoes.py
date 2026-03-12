print("python é facil")
print("python é facil")
print("python é facil")

def exibirmensagem():
    print("ola, mundo!")

exibirmensagem()

def saudar(nome):
    print(f"Ola, {nome} !")

saudar("paulo")
saudar("fabricio")

def exibirmensagem(nome, mensagem ):
    print(f"{mensagem}, {nome}")

exibirmensagem("paulo, Bom Dia")

exibirmensagem(nome = "fabricio", mensagem = "Bom Noite" )


def calcularMedia(nota1, nota2):
       media = (nota1 + nota2) / 2
       return media

resultado = calcularMedia(8.0, 9.0)
print(f"media: {resultado}")
