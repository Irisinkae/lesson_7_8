class Point:
    '''Класс точек'''
    def __init__(self, x, y):
        self.x =x
        self.y =y

class Line:
    '''Класс линий'''
    def __init__(self, start, end):
        self.start = start or Point()
        self.end = end or Point()     
   
    def length(self):
        return ((self.end.x-self.start.x)**2 +(self.end.y-self.start.y)**2)**0.5


from abc import ABC, abstractmethod
class Shape(ABC):
    '''Абстрактный класс Shape'''
    @property
    @abstractmethod 
    def area(self):
        pass
    
    @property
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape, Line):
    '''Класс квадратов(прямоугольников с равными сторонами)'''
    @property  
    def area(self):
        return f'Площадь квадрата: {self.length()**2}'

    @property
    def perimeter(self):
        return f'Периметр квадрата: {4*self.length()}'

class Cube(Square):
    '''Класс кубов (параллелепипедов с равными сторонами)'''
         
    def volume(self):
       return f'Объем куба: {self.length()**3}'


class Rectangle(Shape):
    '''Класс прямоугольников'''
    def __init__(self, length_p, breathe_p):
        self.length_p= length_p or Line() 
        self.breathe_p= breathe_p or Line()

    @property
    def area(self):
        return  f'Площадь прямоугольника: {self.length_p.length()*self.breathe_p.length()}'

    @property
    def perimeter(self):
        return  f'Периметр прямоугольника: {(self.length_p.length()+self.breathe_p.length())*2}'

#Примеры работы
a=Point(1,8)
b=Point(8,1)
c=Point(1,18)
d=Point(4,4)
print(f'Координаты точки a: {a.x},{a.y}, Координаты точки b: {b.x},{b.y}')
print(f'Координаты точки c: {c.x},{c.y}, Координаты точки d: {c.x},{c.y}')
ab=Line(a, b)
print(ab.length()) #длина линии
ac=Line(a,c)
print(ac.length()) #длина линии
S1=Square(a,b)
print(S1.area)   #Площадь квадрата
print(S1.perimeter) #Периметр квадрата
C1=Cube(a,b)            
print(C1.volume())     #Объем куба 
R1=Rectangle(ab,ac)
print(R1.area)       #Площадь прямоугольника
print(R1.perimeter)   #Периметр прямоугольника 
