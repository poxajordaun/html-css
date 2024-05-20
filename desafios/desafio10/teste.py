n = 7
cont = 0
for c in range(n-1, 0, -1):
    cont += 1
    if cont == 1:
        f = n * c
    else:
        f = f * c
        
print(f)