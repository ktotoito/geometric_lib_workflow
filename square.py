
def area(a):
    '''
    Возвращает площадь квадрата с длиной стороны равной a.
    
        Параметры:
            a (int)/(float): целое или вещественное число, длина стороны квадрата
        
        Возвращаемое значение:
            (int)/(float): целое или вещественное число, площадь квадрата с длиной стороны равной a
    '''
    if type(a) not in [float, int]:
        raise TypeError("Wrong type")
    if a <= 0:
        raise ValueError("Negative or zero value")

    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата с длиной стороны равной a.
    
        Параметры:
            a (int)/(float): целое или вещественное число, длина стороны квадрата
        
        Возвращаемое значение:
            (int)/(float): целое или вещественное число, периметр квадрата с длиной стороны равной a
    '''

    if type(a) not in [float, int]:
        raise TypeError("Wrong type")
    if a <= 0:
        raise ValueError("Negative or zero value")

    return 4 * a
