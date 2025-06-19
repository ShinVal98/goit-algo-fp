import turtle
import math

# Малюю квадрат і повертаю координати верхнього лівого кута
def draw_square(t, side):
    for _ in range(4):
        t.forward(side)
        t.left(90)

# Рекурсивно будуємо дерево
def pythagoras_tree(t, side, level):
    if level == 0:
        return
    # Малюю квадрат
    draw_square(t, side)

    # Переходжу до верхнього лівого кута
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.right(90)

    # Обчислюю довжини гілок
    left_side = side * math.cos(math.radians(45))
    right_side = side * math.sin(math.radians(45))

    # Зберігаю позицію та кут
    pos = t.position()
    heading = t.heading()

    # Ліва гілка
    t.left(45)
    pythagoras_tree(t, left_side, level-1)

    # Повертаюся
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()

    # Права гілка
    t.right(45)
    pythagoras_tree(t, right_side, level-1)

    # Повертаюся до вихідної позиції
    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()

def main():
    level = int(input("Вкажи рівень рекурсії (1-10): "))
    side = 100
    turtle.setup(800, 800)
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.setposition(-side/2, -300)
    t.pendown()
    pythagoras_tree(t, side, level)
    turtle.done()

if __name__ == "__main__":
    main()

