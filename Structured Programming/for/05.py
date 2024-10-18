fatorial = int(input('Digite o número que queira saber seu fatorial: '))
calculadora_fatorial = 1

for i in range(1, fatorial + 1):
    calculadora_fatorial *= i
print(f'O resultado final de {fatorial} fatorial é {calculadora_fatorial}')