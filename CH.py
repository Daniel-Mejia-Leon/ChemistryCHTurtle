import turtle
from time import sleep

count = 1

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

def triangulo(up=False, down=False):
    if not up and not down:
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
    if up and not down:
        turtle.left(90)
        turtle.forward(50)
        turtle.left(45)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.left(135)
    if down and not up:
        turtle.right(90)
        turtle.forward(50)
        turtle.right(45)
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(135)

def ch(number, sus=0, count=1):
    if number == 1:
        turtle.left(90)
        pass
    # for number of C
    for i in range(number):
        # if C number is reached
        if count == number:
            break
        turtle.left(90)
        turtle.forward(50)
        count += 1
        # sus
        if sus == count:
            turtle.left(45)
            turtle.forward(50)
            turtle.left(180)
            turtle.forward(50)
            turtle.left(135)
        # if sus == count CHECK THIS
        for n in range(number):
            # for number of C
            if count == number:
                break
            turtle.right(90)
            turtle.forward(50)
            count += 1
            if sus == count:
                turtle.right(45)
                turtle.forward(50)
                turtle.right(180)
                turtle.forward(50)
                turtle.right(135)
            break
    # variable global count if count == carbonos: stop!


def chain(x):
    # if the name is just a simple chaing
    if len(name) == 1:
        print('llego aqui')
        if met in name[0]:
            ch(x)
        if et in name[0]:
            ch(x)
        if prop in name[0]:
            ch(x)
        if but in name[0]:
            ch(x)
        if pent in name[0]:
            ch(x)
        if hex in name[0]:
            ch(x)
        if hept in name[0]:
            ch(x)
        if oct in name[0]:
            ch(x)
        if non in name[0]:
            ch(x)
        if ico in name[0]:
            ch(x)
    # if the name has 3 characters on it must be sus location-susType-chain#
    if len(name) == 3:
        if name[-3] == 0:
            ch(x)
        if int(name[-3]) == 2:
            ch(x, 2)
        if int(name[-3]) == 3:
            ch(x, 3)
        if int(name[-3]) == 4:
            ch(x, 4)
        if int(name[-3]) == 5:
            ch(x, 5)
        if int(name[-3]) == 6:
            ch(x, 6)
        if int(name[-3]) == 7:
            ch(x, 7)
        if int(name[-3]) == 8:
            ch(x, 8)
        if int(name[-3]) == 9:
            ch(x, 9)
        if int(name[-3]) == 10:
            ch(x, 10)
        if int(name[-3]) == 11:
            ch(x, 11)
        if int(name[-3]) == 12:
            ch(x, 12)

molecule = 'icosne'

name = []
numbers = range(1, 20)
dash = '-'
comma = ','
if dash in molecule:
    molecule = molecule.replace('-', '')
if comma in molecule:
    molecule = molecule.replace(',', '')
molecule_split = molecule.split()

for i in molecule_split:
    name.append(i.capitalize())

print(name)
print(name[-1])

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
turtle.speed(4)
turtle.pendown()
turtle.right(45)




if met in name[-1]:
    chain(1)

if et in name[-1]:
    chain(2)

if prop in name[-1]:
    chain(3)

if but in name[-1]:
    chain(4)

if pent in name[-1]:
    chain(5)

if hex in name[-1]:
    chain(6)

if hept in name[-1]:
    chain(7)

if oct in name[-1]:
    chain(8)

if non in name[-1]:
    chain(9)

if ico in name[-1]:
    chain(20)



screen.mainloop()
