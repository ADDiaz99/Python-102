'''
dict = {}
for i in range(1, 11):
    dict[i] = i * 2 

print(dict)

dict_v2 = { i : i * 2 for i in range(1, 11) }
print(dict_v2)


import random
countries = ['col', 'mex', 'bol', 'pe']
population = { }

for country in countries:
    population[country] = random.randint(1, 100)

print(population)
'''

names = ['pepe', 'pablo', 'perejil']
ages = [12, 32, 56]

newlist = {name : age for (name, age) in zip(names, ages)}
print(newlist)