valores = [1, 5, 19, 2]
maior_valor = valores[0]  

for i in valores:
    if i > maior_valor:
        maior_valor = i  

print(f'O maior valor é {maior_valor}')
