linha = input().split()
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

delta = b * b - 4 * a * c

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)