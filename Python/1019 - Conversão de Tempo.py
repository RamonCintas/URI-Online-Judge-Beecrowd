Total= int(input())
Horas = Total // 60 ** 2
Total = Total - Horas * 60 ** 2
Minutos = Total // 60
Total = Total - Minutos * 60
Segundos = Total
print('{}:{}:{}'.format(Horas,Minutos,Segundos))