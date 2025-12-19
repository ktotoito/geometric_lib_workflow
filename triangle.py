
def area(a, b, c): 
    '''
    Возвращает площадь треугольника со сторонами длиной a, b и c.
    
        Параметры:
            a (int)/(float): целое или вещественное число, длина первой стороны
            b (int)/(float): целое или вещественное число, длина второй стороны
            c (int)/(float): целое или вещественное число, длина третьей стороны
        
        Возвращаемое значение:
            s (float): число с плавающей точкой, площадь заданного треугольника
    '''
    if (type(a) not in [float, int]) or (type(b) not in [float, int]) or (type(c) not in [float, int]):
        raise TypeError("Wrong type")

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Negative or zero value")

    if a+b <= c or a+c <= b or b+c <= a:
        raise ValueError("Degenerate triangle")

    p = (a + b + c)/2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника со сторонами длиной a, b и c.
    
        Параметры:
            a (int)/(float): целое или вещественное число, длина первой стороны
            b (int)/(float): целое или вещественное число, длина второй стороны
            c (int)/(float): целое или вещественное число, длина третьей стороны
        
        Возвращаемое значение:
            (int)/(float): целое или вещественное число, периметр заданного треугольника
    '''

    if (type(a) not in [float, int]) or (type(b) not in [float, int]) or (type(c) not in [float, int]):
        raise TypeError("Wrong type")

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Negative or zero value")

    if a+b <= c or a+c <= b or b+c <= a:
        raise ValueError("Degenerate triangle")

    return a + b + c 


