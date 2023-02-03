try:
    print(0 / 0)
    assert 1 != 1, 'Uno no es igual que uno'
    edad=10
    if edad<18:
        raise Exception("No se permite menores de edad")
    
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)
    

print('hola')