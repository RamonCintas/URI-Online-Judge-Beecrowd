a,b,c,d = input().split(' ')
c1 = a
c2 = b
c3 = c
c4 = d
if c1 > c2 and c3 and c4:
    print(1)
elif c2 > c1 and c3 and c4:
    print(2)
elif c3 > c1 and c2 and c4:
    print(3)
else:
    print(4)