entrada = input().split()

codigo = int(entrada[0])
quantidade = int(entrada[1])
valor = 0.0

if codigo == 1:
    valor = 4.00 * quantidade
elif codigo == 2:
    valor = 4.50 * quantidade
elif codigo == 3:
    valor = 5.00 * quantidade
elif codigo == 4:
    valor = 2.00 * quantidade
elif codigo == 5:
    valor = 1.50 * quantidade
    
print("Total: R$ %0.2f" %valor)