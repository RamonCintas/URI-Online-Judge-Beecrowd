A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())

Contador = 0

if A % 2 == 0:
    Contador += 1
if B % 2 == 0:
    Contador += 1
if C % 2 == 0:
    Contador += 1
if D % 2 == 0:
    Contador += 1
if E % 2 == 0:
    Contador += 1
print(Contador,'valores pares')