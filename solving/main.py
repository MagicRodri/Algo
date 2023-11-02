import random
import turtle

# Написать программу которая запрашивает  количество
# треугольников пользователю и рисует это количество
# треугольников в виде матрешки (треугольники внутри треугольников)


def draw_triangle(pen, size, color):
    pen.color(color)
    # pen.begin_fill()
    for _ in range(3):
        pen.forward(size)
        pen.left(120)
    # pen.end_fill()


def draw_pattern(pen):
    pen.color('red')
    pen.fillcolor('yellow')
    pen.begin_fill()
    while True:
        pen.forward(200)
        pen.left(170)
        if abs(pen.pos()) < 1:
            break
    pen.end_fill()


def main():
    number_of_triangles = int(input('Введите количество треугольников: '))
    pen = turtle.Turtle()
    pen.speed(0)
    size = 300
    colors = ['red', 'green', 'blue']
    previous_color = None

    window = turtle.Screen()

    rootwindow = window.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

    for _ in range(number_of_triangles):
        color = random.choice(colors)
        while color == previous_color:
            color = random.choice(colors)
        previous_color = color
        draw_triangle(pen, size, color)
        size -= 10
        pen.penup()
        pen.forward(5)
        # pen.right(90)
        # pen.forward(5)
        # pen.left(90)
        pen.pendown()
    # draw_pattern(pen)
    turtle.done()


if __name__ == '__main__':
    main()