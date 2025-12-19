
def area(a, b): 
    '''
    Возвращает площадь прямоугольника со смежными сторонами длиной a и b.
    
        Параметры:
            a (int)/(float): целое или вещественное число, длина одной смежной стороны
            b (int)/(float): целое или вещественное число, длина второй смежной стороны
        
        Возвращаемое значение:
            (int)/(float): целое или вещественное число, площадь заданного прямоугольника
    '''

    if type(a) not in [float, int] or type(b) not in [float, int]:
        raise TypeError("Wrong type")
    if a <= 0 or b <= 0:
        raise ValueError("Negative or zero value")

    return a * b

def perimeter(a, b): 
    '''
    Возвращает периметр прямоугольника со смежными сторонами длиной a и b.
    
        Параметры:
            a (int)/(float): целое или вещественное число, длина одной смежной стороны
            b (int)/(float): целое или вещественное число, длина второй смежной стороны
        
        Возвращаемое значение:
            (int)/(float): целое или вещественное число, периметр заданного прямоугольника
    '''
    if type(a) not in [float, int] or type(b) not in [float, int]:
        raise TypeError("Wrong type")
    if a <= 0 or b <= 0:
        raise ValueError("Negative or zero value")

    return 2 * (a + b)
