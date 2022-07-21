Nome = input()
SalFixo = float(input())
TotalVendas = float(input())
Com = TotalVendas * 0.15
Res = Com + SalFixo
print("TOTAL = R$ %.2f" % Res)