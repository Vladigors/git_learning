
def draw_house(x, y, width, height):
    """   # Набираем тройные двойные кавычки + Enter между ними
    Функция, рисует домик полной ширины width и высоты height
    от опорной точки (x, y), которая находится в нижней точке
    фундамента посередине.
    :param x: координата х середины домика
    :param y: координата у низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крыши включены)
    :param height: полная высота домика
    :return: None
    """
    print('Типа рисую домик...', x, y, width, height)
    pass  # do nothing

x, y = 100, 100
width, height = 200, 200

draw_house(x, y, width, height)
