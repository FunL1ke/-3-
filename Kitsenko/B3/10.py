def gipotenuza():
    C = (katet1 ** 2 + katet2 ** 2) ** 0.5
    return(C)

print('Введите первый катет')
katet1 = float(input())
print(f'Введите второй катет')
katet2 = float(input())

print(gipotenuza())