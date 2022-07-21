A, B, C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159
triangulo = A * C / 2
circulo = C * C * pi
trapezio = (A + B) * C / 2
quadrado = B * B
retangulo = A * B
print('TRIANGULO: {:.3F}'.format(triangulo))
print('CIRCULO: {:.3F}'.format(circulo))
print('TRAPEZIO: {:.3F}'.format(trapezio))
print('QUADRADO: {:.3F}'.format(quadrado))
print('RETANGULO: {:.3F}'.format(retangulo))