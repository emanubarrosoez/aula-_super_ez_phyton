e1 = float(input("Digite a primeira estatura: "))
e2 = float(input("Digite a segunda estatura: "))
e3 = float(input("Digite a terceira estatura: "))

if e1 == e2 or e1 == e3 or e2 == e3:
    print("Há, pelo menos, 2 pessoas com a mesma estatura")

else:
    if e1 > e2 and e1 > e3:
        print("A maior estatura é:", e1)
    elif e2 > e1 and e2 > e3:
        print("A maior estatura é:", e2)
    else:
        print("A maior estatura é:", e3)
