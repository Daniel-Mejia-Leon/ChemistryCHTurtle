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

molecule = '3 - metil ,icotane'

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
    ch(1)

if et in name[-1]:
    ch(2)

if prop in name[-1]:
    ch(3)

if but in name[-1]:
    ch(4)

if pent in name[-1]:
    ch(5)

if hex in name[-1]:
    ch(6)

if hept in name[-1]:
    ch(7)

if oct in name[-1]:
    ch(8)

if non in name[-1]:
    ch(9)

nine = 9
# if ico in name[-1]:
#     for i in range(9):
#         turn(left, False)
#         count += 1
#         print(count)
#         turn(right, False)
#         count += 1
#         print(count)
#     turn(left, False)
#     count += 1
#     print(count)

    # if int(name[-3]) in numbers:
    #     if int(name[-3]) == 4:
    #         for i in range(nine):
    #             if count == 4: #right here, check why this is ignored
    #
    #                 print('llego aqui')
    #                 turn(left, True)
    #                 turn(right, False)
    #                 nine -= 1
    #                 continue
    #             turn(left, False)
    #             count += 1
    #             print(count)
    #             turn(right, False)
    #             count += 1
    #             print(count)
    #         turn(left, False)
    #         count += 1
    #         print(count)
    #         pass


    # for i in range(9):
    #     turn(left, False)
    #     count += 1
    #     print(count)
    #     turn(right, False)
    #     count += 1
    #     print(count)
    # turn(left, False)
    # count += 1
    # print(count)

if ico in name[-1]:
    if name[-3] == 0:
        ch(20)
    if int(name[-3]) == 2:
        ch(20, 2)
    if int(name[-3]) == 3:
        ch(20, 3)
    if int(name[-3]) == 4:
        ch(20, 4)
    if int(name[-3]) == 5:
        ch(20, 5)
    if int(name[-3]) == 6:
        ch(20, 6)
    if int(name[-3]) == 7:
        ch(20, 7)
    if int(name[-3]) == 8:
        ch(20, 8)
    if int(name[-3]) == 9:
        ch(20, 9)
    if int(name[-3]) == 10:
        ch(20, 10)
    if int(name[-3]) == 11:
        ch(20, 11)
    if int(name[-3]) == 12:
        ch(20, 12)



screen.mainloop()












# draw_molecule('4 metil icosane')
