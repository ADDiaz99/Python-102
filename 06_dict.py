import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100) for country in countries}
print(population_v2)

frase = "Existen 3 a en esta frase"

conteo = { c: frase.count(c) for c in frase if c in 'aeiou'}
print(conteo)