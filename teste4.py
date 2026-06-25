idade = int(input("Digite a sua idade: "))
habilitacao = input("Você tem habilitação? (sim/nao): ")

if idade >= 18 and habilitacao == "sim":
    print("Pode dirigir")
else:
    print("Não pode dirigir")
