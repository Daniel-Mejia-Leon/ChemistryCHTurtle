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


def up_sus(c_number=1):
    if c_number == 1:
        turtle.left(45)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.left(135)
    if c_number == 2:
        turtle.left(45)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(135)


def down_sus(c_number):
    if c_number == 1:
        turtle.right(45)
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(135)

molecule = '3 - methyl, butane'

# this function is to attach the sus on the main chain
# the main chain function has the message for invalid sus_loc
def ch(number, sus_loc=0, sus_len=0, count=1):
    # if the number is 1 dont do anything since methane is just a dot
    if number == 1:
        turtle.left(90)
        pass
    # for number of Carbons do up and down until number of carbons == count
    for i in range(number):
        # if C number is reached
        if count == number:
            turtle.shape('circle')
            turtle.shapesize(0.5)
            break
        turtle.left(90)
        turtle.forward(50)
        count += 1
        # if sus_loc == count then proceed to create the sus_len sus
        if sus_loc == count:
            if sus_len == 2:
                up_sus(2)
            if sus_len == 1:
                up_sus()
        # if sus == count CHECK THIS
        for n in range(number):
            # for number of C
            if count == number:
                turtle.shape('circle')
                turtle.shapesize(0.5)
                break
            turtle.right(90)
            turtle.forward(50)
            count += 1
            # start sus creation in position = count
            if sus_loc == count:
                down_sus(sus_len)
            break
    # variable global count if count == carbonos: stop!


def chain(x):
    # if the name is just a simple chain
    if len(name) == 1:
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
        # here is where you have to put the invalid warning for sus_loc == number
        if int(name[-3]) == 1:
            print('invalid 1 cant be sus_loc')
        if int(name[-3]) == 2:
            if x == 2:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]))

        if int(name[-3]) == 3:
            if x == 3:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]))
        if int(name[-3]) == 4:
            if x == 4:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]), 2)
        if int(name[-3]) == 5:
            if x == 5:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]))
        if int(name[-3]) == 6:
            if x == 6:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]))
        if int(name[-3]) == 7:
            if x == 7:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]))
        if int(name[-3]) == 8:
            if x == 8:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]))
        if int(name[-3]) == 9:
            if x == 9:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]))
        if int(name[-3]) == 10:
            if x == 10:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]))
        if int(name[-3]) == 11:
            if x == 11:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]))
        if int(name[-3]) == 12:
            if x == 11:
                print('invalid, sus_loc cant be first nor final ')
            else:
                ch(x, int(name[-3]))




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
turtle.shapesize(1.5)
turtle.goto(-screen_x / 2 + 50, 0)
turtle.pensize(2)
turtle.speed(1)
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
