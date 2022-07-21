N = int(input())
N100 = int(N // 100)
resto = N % 100
N50 = int(resto // 50)
resto = resto % 50
N20 = int(resto // 20)
resto = resto % 20
N10 = int(resto // 10)
resto = resto % 10
N5 = int(resto // 5)
resto= resto % 5
N2 = int(resto // 2)
resto = resto % 2
N1 = int(resto // 1)
print(N)
print(N100,"nota(s) de R$ 100,00")
print(N50,"nota(s) de R$ 50,00")
print(N20,"nota(s) de R$ 20,00")
print(N10,"nota(s) de R$ 10,00")
print(N5,"nota(s) de R$ 5,00")
print(N2,"nota(s) de R$ 2,00")
print(N1,"nota(s) de R$ 1,00")