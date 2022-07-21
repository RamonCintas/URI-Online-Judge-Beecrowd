a,b,c,= input().split(' ')
a = int(a)
b = int(b)
c = int(c)
Bloqueio_De_Passagem = a + b + c
if (a-b == 0) or (a-c == 0) or (b-c == 0):
    print('S')
elif (a+b-c == 0) or (b-a+c == 0) or (c-a+b == 0):
    print('S')
elif (a-b-c == 0) or (b-a-c == 0) or (c-a-b == 0):
    print('S')
elif a - b -  c - Bloqueio_De_Passagem < 0:
    print('N')