import turtle
from time import sleep

count = 1


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

def straight(x):
    if x == 'Up':
        turtle.left(90)
        turtle.forward(50)
    if x == 'Down':
        turtle.right(90)
        turtle.forward(50)

def up_sus(c_number=1):
    # methyl
    if c_number == 1:
        turtle.left(45)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.left(135)

    # ethyl
    if c_number == 2:
        turtle.left(45)  # start sus
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(180)  # go back
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(135)  # finish sus

    # propil
    if c_number == 3:
        turtle.left(45)  # start sus
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(180)  # go back
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(135)  # finish sus

    # butyl
    if c_number == 4:
        turtle.left(45)  # start sus
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(180)  # go back
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(135)  # finish sus

def down_sus(c_number):
    # methyl
    if c_number == 1:
        turtle.right(45)
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(50)
        turtle.right(135)

    # ethyl
    if c_number == 2:
        turtle.right(45)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(135)

    # propyl
    if c_number == 3:
        turtle.right(45)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(135)

    # butyl
    if c_number == 4:
        turtle.right(45)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(135)


molecule = 'icosane'

# this function is to attach the sus on the main chain
# the main chain function has the message for invalid sus_loc
def ch(number, sus_loc=0, sus_len=0, count=1):
    down = 'Down'
    up   = 'Up'
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
        straight(up)
        count += 1
        # if sus_loc == count then proceed to create the sus_len sus
        if sus_loc == count:
            up_sus(sus_len)
        # if sus == count CHECK THIS
        for n in range(number):
            # for number of C
            if count == number:
                turtle.shape('circle')
                turtle.shapesize(0.5)
                break
            straight(down)
            count += 1
            # start sus creation in position = count
            if sus_loc == count:
                down_sus(sus_len)
            break
    # variable global count if count == carbonos: stop!

def name_check(x):
    if met in x:
        return 1
    if et in x:
        return 2
    if prop in x:
        return 3
    if but in x:
        return 4
    if pent in x:
        return 5
    if hex in x:
        return 6
    if hept in x:
        return 7
    if oct in x:
        return 8
    if non in x:
        return 9
    if dec in x:
        return 10
    if ico in x:
        return 20

def chain(x):
    # if the name is just a simple chain
    prefix = [met, et, prop, but, pent, hex, hept, oct, non, dec, 'Icosane'] # fix this part because we are supposed to use vars not strings
    if len(name) == 1:
        print('llego aqui')
        if name[0] in prefix:
            print('aqui tambien')
            ch(x)
    # if the name has 3 characters on it must be sus location-susType-chain#
    if len(name) == 3:
        if name[-3] == 0:
            ch(x)
        #         print('invalid, sus_loc cant be first nor final ')
        ch(x, int(name[-3]), name_check(name[-2]))


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
turtle.speed(2)
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

if dec in name[-1]:
    chain(10)

if ico in name[-1]:
    chain(20)



screen.mainloop()
