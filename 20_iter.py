#Muestra el rango de numeros que sean digitados >:)
'''
first = int(input('First number =>'))
second = int(input('Second number =>'))

def multrange(first, second):
    for i in range(first, second):
       print(i) 


multrange(first, second)
'''

my_iter = (iter(range(1, 11)))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
