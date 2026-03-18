# numero x maior que 5; so precisava so botar 2 pontos.
x = 10
if x > 5:
   print("x é maior que 5")

# validar o tamanho de um nome; so adicionar numero no nome possui.
nome = "joão silva"
if len(nome) > 5:
   print("seu nome é grande!")
   print(f"ele possui30 {len(nome)} caracteres.")

# digite o preço de 5 reais como bonus; era so bota o float no input("digite o preço:").
preco = float(input("digite o preço:"))
novo_preco = preco + 5
print("O valor final é: ", novo_preco)

# dizer se a pessoas é maior de idade; era so botar o igual de pois da seta.
idade =18
if idade >= 18:
   print("você é maior de idade")
else:
   print("você é menor de idade")

# imprimir os numero de 1 a 5; esta errado porque ele não imprimir de 1 a 5 e de 0 a 4.
for i in range(1, 6):
   print(i)

# objetivo exibir a ultima atriz da lista; porque a não e de 1 a 4 e sim de 0 a 3.
atrizes = ["adriana", "barbara", "camila", "danielle"]
print(atrizes[3])

# calcular o dobro e soma 10 ao resultado; troca a print para return.
def calcular_dobro(n):
   return n * 2

resultado = calcular_dobro(5) + 10
print(resultado)

# adicionar um nova idade à liata; troca o add para append.
idades = [27, 19, 33]
idades.append(47)
print(idades)

# armazenar e exibir contatos; adicionar contato e =, {}, print mas contato.
contato = {"@camilaquiroz", "camila aquiroz"}
contato = {"@paollaoliveireal", "paolla de oliveira"}
print(contato["@camilaquiroz"])
print(contato["@paollaoliveirael"])

# criar uma função que receba um numero e retorne se ele é positivo ou zero.
def verificar_numero(n):
    if n >= 0:
        return "positivo ou zero"
    else:
        return "negativo"

print(verificar_numero(5))
print(verificar_numero(0))
print(verificar_numero(-3))


# criar uma função que receba uma palavra e retorne quanto letras ela possui no python.
def contar_letras(palavra):
    return len(palavra)


resultado = contar_letras("python")
print(resultado)