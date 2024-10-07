from abc import ABC, abstractmethod
import math
from PIL import Image, ImageDraw
 
class Shape(ABC):
    def __init__(self, name: str, x1: int, x2: int, y1: int, y2: int) -> any:
        self.img=Image.new('RGB', (500, 300), (255, 255, 255)) # фон
        self.draw = ImageDraw.Draw(self.img)
        self.name = name  
        self.x1 = x1  
        self.x2 = x2           
        self.y1 = y1    
        self.y2 = y2 
    def get_xy(self): print(f'{self.name} {self.x1}:{self.x2}  {self.y1}:{self.y2}')
    
    @abstractmethod
    def S(self):pass

    @abstractmethod
    def P(self):pass 

    
class Ellipse(Shape):
    def __init__(self, name: str, x1: int, x2: int, y1: int, y2: int,ma_ax:int, mi_ax:int) -> any:
        self.ma_ax = ma_ax  # Полуось большого радиуса
        self.mi_ax = mi_ax 
        super().__init__(name, x1, x2, y1, y2)  # Вызов конструктора родителя
        self.draw.ellipse((x1, x2, y1, y2), fill='black', outline=(1, 1, 1))
        self.img.show()

    def S(self): return math.pi * self.ma_ax * self.mi_ax

    def P(self): 
        return math.pi * (3 * (self.ma_ax + self.mi_ax) - math.sqrt((3 * self.ma_ax + self.mi_ax) * (self.ma_ax + 3 * self.mi_ax)))

class Rectangle(Shape):
    def __init__(self, name: str, x1: int, x2: int, y1: int, y2: int, x:int,y:int) -> any:
        self.x=x
        self.y=y
        super().__init__(name, x1, x2, y1, y2)  # Вызов конструктора родителя
        self.draw.line(((x2, x1), (y2, x2), (x2, y2), (x1, y1), (y1, x1)),fill='black',width=5)
        self.img.show()
    
    def S(self): return (self.x * self.y) / 2

    def P(self): 
        return 4 * math.sqrt((self.x / 2) ** 2 + (self.y / 2) ** 2)

class Cuboid(Shape):
    def __init__(self, name: str, x1: int, x2: int, y1: int, y2: int,length:int,width:int,height:int) -> any:
        self.length=length
        self.width=width
        self.height=height
        super().__init__(name, x1, x2, y1, y2)  # Вызов конструктора родителя

        front_bottom_left = (x1, x2 + y2)
        front_bottom_right = (x1 + y1, x2 + y2)
        front_top_left = (x1, x2)
        front_top_right = (x1 + y1, x2)

        back_bottom_left = (x1 - 50, x2 + y2 - 50)
        back_bottom_right = (x1 + y1 - 50, x2 + y2 - 50)
        back_top_left = (x1 - 50, x2 - 50)
        back_top_right = (x1 + y1 - 50, x2 - 50)

        self.draw.polygon([front_bottom_left, front_bottom_right, front_top_right, front_top_left], outline="black", fill="gray")
        self.draw.polygon([back_bottom_left, back_bottom_right, back_top_right, back_top_left], outline="black", fill="lightgrey")
        self.draw.line([front_bottom_left, back_bottom_left], fill="black")
        self.draw.line([front_bottom_right, back_bottom_right], fill="black")
        self.draw.line([front_top_left, back_top_left], fill="black")
        self.draw.line([front_top_right, back_top_right], fill="black")
        self.img.show()

    def S(self):return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def P(self): return 4 * (self.length + self.width + self.height)


def main():
    print(f"Выберите фигуру для вычисления S и P\n(1 - Ромб, 2 - Параллелепипед, 3 - Эллипс):")

    def get_rect():
        return Rectangle('Ромб',100,150,150,200,float(input("Введите длину первой диагонали ромба: ")), float(input("Введите длину второй диагонали ромба: ")))

    def get_cuboid():
        return Cuboid('Сuboid',150,100,100,100,float(input("Введите длину параллелепипеда: ")), float(input("Введите ширину параллелепипеда: ")), float(input("Введите высоту параллелепипеда: ")))

    def get_elips():
        return Ellipse('Эллипс',100,100,150,200,float(input("Введите длину полуоси большого радиуса эллипса: ")), float(input("Введите длину полуоси малого радиуса эллипса: ")))

    shapes = {
        '1': get_rect,
        '2': get_cuboid,
        '3': get_elips,
    }

    shape = shapes.get(input("Введите номер фигуры (1-3): "))()
    if shape:
        print(shape)
        print("Площадь: {:.2f}".format(shape.S()))
        print("Периметр: {:.2f}".format(shape.P()))
    else:
        print(f"Try again")

if __name__ == "__main__":
    while True:
        main()