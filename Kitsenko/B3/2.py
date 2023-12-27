A, B = int(input()), int(input())
count = 0

for i in range(A, B + 1):
    print(i, end=" ")
    count += 1
print()
print(f'Между числами {A} и {B} расположено {count - 2} чисел')
