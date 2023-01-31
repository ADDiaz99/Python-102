def multiply_numbers(numbers):
    # Escribe tu solución 👇
    func = list(map(lambda numbers : numbers * 2, numbers)) 
    return func

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)