

numbers = [num for num in range(0,23,1)] # заполняем список от 1 до 23 с шагом 1


even = list(filter(lambda x: x % 2 == 0, numbers))  
odd = list(filter(lambda x: x % 2 != 0, numbers))   

#print("Чётные:", even)  
#print("Нечётные:", odd)  

words = ['12345', '123', '12345', '1234', 'белый', 'черный']
words_to_remove = ['123', 'белый']

filtered_words = list(filter(lambda word: word not in words_to_remove, words))

#print("Оставшиеся слова:", filtered_words)  

numbers = [num for num in range(0,45,1)] # заполняем список от 1 до 23 с шагом 1

is_sorted = all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

print("Список отсортирован:", is_sorted)
