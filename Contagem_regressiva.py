
for segundos in range(10, 0, -1):
    if segundos % 2 == 0:
        print(f'Faltam apenas {segundos} segundos - Não perca essa oportunidade!')
    else:
        singular = 'segundo' if segundos == 1 else 'segundos'
        print(f'A contagem continua: {segundos} {singular} restantes')
print('Aproveite a promoção agora!')

print()

