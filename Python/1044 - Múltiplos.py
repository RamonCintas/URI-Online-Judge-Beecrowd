a,b,= input().split(' ')
a = int(a)
b = int(b)
t1 = a / b
t2 = b / a
t3 = a % b
t4 = b % a
if t1 == 0:
    print('Sao Multiplos')
elif t2 == 0:
    print('Sao Multiplos')
elif t3 == 0:
    print('Sao Multiplos')
elif t4 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')