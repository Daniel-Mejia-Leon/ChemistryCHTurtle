import turtle
from time import sleep


def draw_molecule(molecule):
    molecule = molecule.capitalize()
    count = 1
    met = 'Meth'
    et = 'Eth'
    prop = 'Prop'
    but = 'But'
    pent = 'Pent'
    hex = 'Hex'
    hept = 'Hept'
    oct = 'Oct'
    non = 'Non'
    dec = 'Dec'
    ico = 'Ico'
    left = 'left'.capitalize()
    right = 'right'.capitalize()
    screen = turtle.Screen()
    screen_x = 800
    screen_y = 600
    screen.setup(screen_x, screen_y)
    turtle.penup()
    turtle.shape()
    turtle.shapesize(2)
    turtle.goto(-screen_x / 2 + 50, 0)
    turtle.pensize(2)
    turtle.speed(3)
    turtle.pendown()
    turtle.right(45)
    sleep(1)

    if et in molecule:
        turn(left, False)

    if prop in molecule:
        turn(left, False)
        turn(right, False)

    if but in molecule:
        turn(left, False)
        turn(right, False)
        turn(left, False)

    if pent in molecule:
        for i in range(1):
            turn(left, True)
            count +=1
            print(count)
            turn(right, False)
            count += 1
            print(count)
            turn(left, False)
            count += 1
            print(count)
            turn(right, False)
            count += 1
            print(count)

    if hex in molecule:
        for i in range(2):
            turn(left, False)
            turn(right, False)
        turn(left, False)

    if hept in molecule:
        for i in range(3):
            turn(left, False)
            turn(right, False)

    if oct in molecule:
        for i in range(3):
            turn(left, False)
            turn(right, False)
        turn(left, False)

    if non in molecule:
        for i in range(4):
            # the sustituyent can be set with if i == number
            # if i == 2:
            #     turn(left, True)
            #     turn(right, False)
            turn(left, False)
            turn(right, False)

    if ico in molecule:
        for i in range(9):
            turn(left, False)
            count += 1
            print(count)
            turn(right, False)
            count += 1
            print(count)
        turn(left, False)
        count += 1
        print(count)

    screen.mainloop()


def turn(direction, sustituyente):
    if not sustituyente and direction == 'Left':
        turtle.left(90)
        turtle.forward(50)
    if sustituyente and direction == 'Left':
        turtle.left(90)
        turtle.forward(50)
        turtle.left(45)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.left(135)
    if not sustituyente and direction == 'Right':
        turtle.right(90)
        turtle.forward(50)
    if sustituyente and direction == 'Right':
        turtle.right(90)
        turtle.forward(50)
        turtle.right(45)
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(135)


draw_molecule('icosane')
