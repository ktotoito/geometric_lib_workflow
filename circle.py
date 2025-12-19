import math


def area(r):
    '''
    Возвращает площадь круга радиусом r.
    
        Параметры:
            r (int)/(float): целое или вещественное число, радиус круга
            
        Возвращаемое значение:
            (float): число с плавающей точкой, площадь круга радиусом r
    '''
    if type(r) not in [float, int]:
        raise TypeError("Wrong type")
    if r <= 0:
        raise ValueError("Negative or zero value")
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности круга радиусом r.
    
        Параметры:
            r (int)/(float): целое или вещественное число, радиус круга
            
        Возвращаемое значение:
            (float): число с плавающей точкой, длина окружности круга радиусом r
    '''
    if type(r) not in [float, int]:
        raise TypeError("Wrong type")
    if r <= 0:
        raise ValueError("Negative or zero value")
    return 2 * math.pi * r
