linha = input().split(" ")
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
d = int(linha[3])
testar = b>c and d>a
testar = testar and c+d>a+b
testar = testar and c>0 and d>0
testar = testar and a%2 == 0
if (testar): 
    print("Valores aceitos")
else: 
    print("Valores nao aceitos")