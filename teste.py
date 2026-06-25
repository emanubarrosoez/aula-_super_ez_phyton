cargo = input("Digite o cargo do funcionário: ")
salario = float(input("Digite o salário atual: "))

if cargo == "Programador de Sistemas":
    aumento = salario * 0.30
    novo_salario = salario + aumento
    print("Novo salário: R$", novo_salario)

elif cargo == "Analista de Sistemas":
    aumento = salario * 0.20
    novo_salario = salario + aumento
    print("Novo salário: R$", novo_salario)

elif cargo == "Analista de Banco de Dados":
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print("Novo salário: R$", novo_salario)

else:
    print("Cargo inválido")
