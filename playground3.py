def filter_by_length(words):
   # Escribe tu solución 👇
   words = list(filter(lambda words : len(words)>= 4, words ))
   return words

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)