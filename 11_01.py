import os, functools
import collections

def processing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Начинаем выполнение метода: {func.__name__}')
        try:
            result = func(*args, **kwargs)
            print(f'Метод {func.__name__} выполнен успешно.')
            return result
        except Exception as e:
            print(f'Ошибка вида: {e}')  
            print(f'Метод {func.__name__} завершился с ошибкой.')  
            return None 
    return wrapper

class TextFileProcessor:
    def __init__(self, filename):
        self.filename = filename

    @processing
    def save_text(self, text): # класс записи в файл
        with open(self.filename, 'w', encoding='utf-8') as file: file.write(text)
    
    @processing
    def read_line(self, line_number): # чтение конкретной строки
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if line_number <= len(lines): return lines[line_number - 1].strip()
            else: return "Нет такого"

    @processing
    def read_lines(self, start_line, end_line):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if start_line <= len(lines) and end_line <= len(lines): return "".join(lines[start_line - 1:end_line]).strip()
            else: return "Нет такого"

    @processing
    def find_longest_word(self):
        with open(self.filename, 'r', encoding='utf-8') as file: return max(file.read().split(), key=len)

    @processing
    def words_counter(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            return collections.Counter(file.read().lower().split()).most_common()
    @processing
    def remove_stop_words(self, stop_words):
        with open(self.filename, 'r', encoding='utf-8') as file:
            text = file.read().lower().split()
            filtered_text = [word for word in text if word not in stop_words]
            return filtered_text

    @staticmethod
    @processing
    def save_numbers_to_desktop(numbers):
        numbers_text = " ".join(map(str, numbers))
        desktop_path = os.path.join(dir_file_path)
        with open(desktop_path, 'w', encoding='utf-8') as file:
            file.write(numbers_text)

    @staticmethod
    @processing
    def read_numbers(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            numbers = list(map(int, file.read().split()))
            if len(numbers) == 2:
                number1, number2 = numbers
                difference = number2 - number1
                return number1, number2, difference
            else:
                return "Файл должен содержать ровно два целых числа."


input_text = """На севере диком стоит одиноко
На голой вершине сосна
И дремлет качаясь, и снегом сыпучим
Одета, как ризой, она.
И снится ей всё, что в пустыне далекой 
В том крае, где солнца восход,
Одна и грустна на утесе горючем
Прекрасная пальма растет."""

file_path=os.path.join('11_01.txt')
dir_file_path=os.path.join('11_01','11_01.txt')
processor = TextFileProcessor(file_path)

processor.save_text(input_text) # ззапись текста


print(processor.read_line(3))  # чтение строки

print(processor.read_lines(2, 4))  # чтение с _____ по ______ строки

print(processor.find_longest_word())  # самое длинное слово

print(processor.words_counter())  # подсчет слов


print(processor.remove_stop_words(['и', 'в']))


TextFileProcessor.save_numbers_to_desktop([1,2])
print(TextFileProcessor.read_numbers(dir_file_path))
