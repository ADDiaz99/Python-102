numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)

numbers_v2 = [i for i in range(1, 11)]
print(numbers_v2)

semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
nuevasemana = []
for i in semana:
    if 'a' in i:
        nuevasemana.append(i)

print(nuevasemana)