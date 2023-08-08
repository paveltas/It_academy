from numbers import Number

'''
Задание 3.
Классы. Наследование, волшебные методы.
'''


# Необходимо реализовать семейство классов, обеспечивающих прозрачную работу с такими единицами
# измерения, как миллиметры, сантиметры, метры, километры, дюймы, футы, ярды, фэнь, чи и инь.
# Требуется реализовать метод __str__, который будет возвращать текущее значение и единицу измерения,
# например "1 км", "2.35 мили" и т. д.
# Требуется реализовать методы __eq__ и __lt__ для сравнения любых единиц измерения между собой.
# Требуется реализовать методы __add__, __iadd__, __sub__ и __isub__, принимающие в качестве
# аргумента любой класс единиц, а также просто число. Если в качестве аргумента выступает число,
# то оно трактуется, как количество текущих единиц измерения.
# Требуется реализовать методы __mul__ и __imul__, принимающие числовое значение в качестве аргумента.
# Требуется реализовать методы __div__ и __idiv__, принимающие как числовое значение, так и любой класс
# единиц измерения. В случае, если в качестве аргумента выступает числовое значение, то результат
# возвращается в тех же единицах измерения, что и текущая. В остальных случаях возвращается число.
# Требуется добавить способ конвертации из одной системы единиц в другую (желательно с использованием
# __init__.
# Необходимо выбрать базовую единицу измерения, к которой во время выполнения операций будут
# приводиться все значения. Ее же использовать и в базовом классе. Практически вся функциональность
# реализуется в базовом классе. Иерархию наследования можно сделать двухуровневой, задача подходит
# для этого.


class LengthUnits:
    BASE_UNIT = 'м'
    factor = 1

    def __init__(self, value):
        if isinstance(value, Number):
            self.value = value * self.factor
        else:
            self.value = value.value

    @classmethod
    def __verify_data_number_and_class(cls, other):
        if not isinstance(other, (Number, LengthUnits)):
            raise TypeError('Unsupported operand type. Use numbers or objects of class "LengthUnits"')

    @classmethod
    def __verify_data_number(cls, other):
        if not isinstance(other, Number):
            raise TypeError('Unsupported operand type. Use numbers only')

    def __str__(self):
        return f'{self.value / self.factor} {self.BASE_UNIT}'

    def __eq__(self, other):
        self.__verify_data_number_and_class(other)
        return self.value == other.value if isinstance(other, LengthUnits) else self.value == other

    def __lt__(self, other):
        self.__verify_data_number_and_class(other)
        return self.value < other.value if isinstance(other, LengthUnits) else self.value < other

    def __add__(self, other):
        self.__verify_data_number_and_class(other)
        return type(self)((self.value + other.value) / self.factor) if isinstance(other, LengthUnits) else type(self)(
            (self.value / self.factor) + other)

    def __iadd__(self, other):
        self.__verify_data_number_and_class(other)
        self.value += other.value if isinstance(other, LengthUnits) else other * self.factor
        return self

    def __sub__(self, other):
        self.__verify_data_number_and_class(other)
        return type(self)((self.value - other.value) / self.factor) if isinstance(other, LengthUnits) else type(self)(
            (self.value / self.factor) - other)

    def __isub__(self, other):
        self.__verify_data_number_and_class(other)
        self.value -= other.value if isinstance(other, LengthUnits) else other * self.factor
        return self

    def __mul__(self, other):
        self.__verify_data_number(other)
        return type(self)((self.value / self.factor) * other)

    def __imul__(self, other):
        self.__verify_data_number(other)
        self.value *= other
        return self

    def __truediv__(self, other):
        self.__verify_data_number_and_class(other)
        return type(self)((self.value / self.factor) / other) if not isinstance(other, LengthUnits) else (
                self.value / other.value)

    def __itruediv__(self, other):
        self.__verify_data_number(other)
        self.value /= other
        return self


class Millimeters(LengthUnits):
    BASE_UNIT = 'мм'
    factor = 0.001


class Centimeters(LengthUnits):
    BASE_UNIT = 'см'
    factor = 0.01


class Meters(LengthUnits):
    BASE_UNIT = 'м'
    factor = 1


class Kilometers(LengthUnits):
    BASE_UNIT = 'км'
    factor = 1000


class Inches(LengthUnits):
    BASE_UNIT = 'дюйм'
    factor = 0.0254


class Feets(LengthUnits):
    BASE_UNIT = 'фут'
    factor = 0.3048


class Yards(LengthUnits):
    BASE_UNIT = 'ярд'
    factor = 0.9144


class Miles(LengthUnits):
    BASE_UNIT = 'мили'
    factor = 1609


class Fen(LengthUnits):
    BASE_UNIT = 'фэнь'
    factor = 0.003715


class Chi(LengthUnits):
    BASE_UNIT = 'чи'
    factor = 0.3333


class In(LengthUnits):
    BASE_UNIT = 'инь'
    factor = 32
