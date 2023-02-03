file = open('./text.txt')
print(file.read())


#SIEMPRE CERRAR ARCHIVO PARA GUARDAR MEMORIA
file.close()

#o asi

with open('./text.txt') as file:
    for line in file:
        print(line)

        