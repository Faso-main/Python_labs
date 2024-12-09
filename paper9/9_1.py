from functools import reduce
import random

numbers = [random.randint(1, 500) for _ in range(30)]


threshold = 100

filtered_numbers = list(filter(lambda x: x > threshold, numbers))

sorted_numbers = sorted(filtered_numbers, reverse=True)


if sorted_numbers:  
    product = reduce(lambda x, y: x * y, sorted_numbers)
else:
    print(f'Список пуст')
    product = 0  


print("Список:", numbers)
print(f'Числа больше {threshold}: {filtered_numbers}')
print("Произведение отфильтрованных чисел:", product)
