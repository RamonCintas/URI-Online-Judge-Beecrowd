linha = input().split(" ")
q1 = int(linha[1])
v1 = float(linha[2])

linha = input().split(" ")
q2 = int(linha[1])
v2 = float(linha[2])

vp = q1*v1 + q2*v2
print("VALOR A PAGAR: R$ %.2f"%vp)