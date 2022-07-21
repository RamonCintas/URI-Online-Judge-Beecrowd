V = int(input())

FalaNoel = ''
for i in range(V):
    FalaNoel +='Ho'
    if i == V-1:
        FalaNoel +='!'
    else:
        FalaNoel += ' '
print(FalaNoel)