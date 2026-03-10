paciente = {}

paciente["nome"] = input("Qual o seu nome:")
paciente["idade"] = input("Qual a sua idade:")
paciente["peso"] = input("digite o seu peso(kg) :")
paciente["altura"] = input("digite a sua altura(m):")

imc = paciente["peso"] / (paciente["altura"] ** 2)

paciente["imc"] = imc

print("\n dados")
print("nome:", paciente["nome"])
print("idade:", paciente["idade"])
print("peso:", paciente["peso"])
print("altura:", paciente["altura"])
print("imc:", round(paciente["altura"], 2))