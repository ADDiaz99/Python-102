def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1

result = increment(10)
print(11)

full_name = lambda name, last_name : f'Full name es {name.title()} {last_name.title()}'

nombre = full_name('andres', 'david diaz')
print(nombre)