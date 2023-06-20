import turtle
from time import sleep

count = 1


# TESTING X - NAME X - NAME

def alkyne(direction):
    if direction == 'Up':
        turtle.penup()
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(5)
        turtle.pendown()
        turtle.forward(40)
        turtle.left(180)
        turtle.penup()
        turtle.forward(45)
        turtle.left(90)
        turtle.forward(10)

        turtle.left(90)
        turtle.forward(5)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.penup()
        turtle.forward(45)
        turtle.right(90)
        turtle.forward(5)

        turtle.pendown()

    elif direction == 'Down':
        turtle.penup()
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(5)
        turtle.pendown()
        turtle.forward(40)
        turtle.left(180)
        turtle.penup()
        turtle.forward(45)
        turtle.right(90)
        turtle.forward(10)

        turtle.right(90)
        turtle.forward(5)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.penup()
        turtle.forward(45)
        turtle.left(90)
        turtle.forward(5)
        turtle.pendown()


def alkene(direction):
    if direction == 'Up':
        turtle.penup()
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(5)
        turtle.pendown()
        turtle.forward(40)
        turtle.left(180)
        turtle.penup()
        turtle.forward(45)
        turtle.left(90)
        turtle.forward(5)
        turtle.left(180)
        turtle.pendown()

    elif direction == 'Down':
        turtle.penup()
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(5)
        turtle.pendown()
        turtle.forward(40)
        turtle.left(180)
        turtle.penup()
        turtle.forward(45)
        turtle.right(90)
        turtle.forward(5)
        turtle.right(180)
        turtle.pendown()


def sus_len(sus_len, direction, count=0):
    if direction == 'Up':
        turtle.left(45)
    elif direction == 'Down':
        turtle.right(45)
    count = 1
    for i in range(sus_len):
        if count == sus_len:  # this break only here since this for is the foward statement
            print('first brek')
            break
        turtle.forward(50)
        count += 1
        turtle.right(90)
        if count == sus_len:  # this break only here since this for is the foward statement
            break
        turtle.forward(50)
        count += 1
        turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    if sus_len % 2 == 1:
        print('retocede')
        for i in range(count):  # going back statement
            if count == 1:
                break
            turtle.forward(50)
            count -= 1
            turtle.right(90)
            if count == 1:
                break
            turtle.forward(50)
            count -= 1
            turtle.left(90)

        turtle.forward(50)
        if direction == 'Up':
            turtle.left(135)
        if direction == 'Down':
            turtle.right(135)
    elif sus_len % 2 == 0:
        print('xx')
        for i in range(count):  # going back statement
            if count == 1:
                break
            turtle.forward(50)
            count -= 1
            turtle.left(90)
            if count == 1:
                break
            turtle.forward(50)
            count -= 1
            turtle.right(90)

        turtle.forward(50)
        if direction == 'Up':
            turtle.left(135)
        if direction == 'Down':
            turtle.right(135)


def straight(x):
    if x == 'Up':
        turtle.left(90)
        turtle.forward(50)
    if x == 'Down':
        turtle.right(90)
        turtle.forward(50)


# this function is to attach the sus on the main chain
# the main chain function has the message for invalid sus_loc
def ch(number, sus_loc=0, sus_type=0, sus_loc_nd=0, ene=0, yne=0, count=1):
    # ch(5, 2, 1, 0, 3)
    down = 'Down'
    up = 'Up'
    if number == 1:
        turtle.left(90)
        return None
    if ene >= number:
        print('Double bond location cannot start at last carbon in chain')
        return None
    if yne == number:
        print(f'triple bond location cannot start at last carbon in chain')
        return None
    if sus_loc != 0 and sus_loc == yne or sus_loc != 0 and sus_loc == yne + 1:
        print('Not valid. Substituent must not start where triple bond starts or finishes')
        return None
    # this is to avoid changing chain size, if sus_len to large chain name changes
    if sus_type > 0:  # > 0 because if no substituents no need to check
        if sus_type >= sus_loc:
            print('1Invalid, Substituent will change the chain name.\nSubstituent position and #C on substitutent must keep main chain name as entered')
            return None
        if sus_loc_nd > 0:
            if sus_type >= sus_loc_nd:
                print('2Invalid, Substituent will change the chain name.\nSubstituent position and #C on substitutent must keep main chain name as entered')
                return None
        if sus_type > number - sus_loc or sus_type > number - sus_loc_nd:
            print('Invalid, Substituent will change the chain name.\nSubstituent position and #C on substitutent must keep main chain name as entered')
            return None

    print(f'{number} carbons in main chain')
    print(f'{sus_type} carbons in Substituent')
    print(f'{sus_loc} = first Substituent location')
    print(f'{sus_loc_nd} = second Substituent location')
    print(f'{ene} = double bond location')
    print(f'{yne} = triple bond location')
    # for number of Carbons do up and down until number of carbons == count
    for i in range(number):
        if count == ene:
            alkene(down)
        if count == yne:
            alkyne(down)
        # if C number is reached
        if count == number:
            turtle.shape('circle')
            turtle.shapesize(0.5)
            break
        straight(up)
        count += 1
        if sus_loc == count:
            sus_len(sus_type, up)
        if sus_loc_nd == count:
            sus_len(sus_type, up)
        for n in range(number):
            if count == ene:
                alkene(up)
            if count == yne:
                alkyne(up)
            # for number of C
            if count == number:
                turtle.shape('circle')
                turtle.shapesize(0.5)
                break
            straight(down)
            count += 1
            # start sus creation in position = count
            if sus_loc == count:
                sus_len(sus_type, down)
            if sus_loc_nd == count:
                sus_len(sus_type, down)
            break


def name_check(x):
    if met in x:
        return 1
    elif et in x:
        return 2
    elif prop in x:
        return 3
    elif but in x:
        return 4
    elif pent in x:
        return 5
    elif hex in x:
        return 6
    elif hept in x:
        return 7
    elif oct in x:
        return 8
    elif non in x:
        return 9
    elif dec in x:
        return 10
    elif ico in x:
        return 20


def number_of_carbons_on_main_chaing(x):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
               '19', '20']
    # if the name is just a simple chain
    prefix = ['Met', 'Eth', 'Pro', 'But', 'Pen', 'Hex', 'Hep', 'Oct', 'Non', 'Dec',
              'Ico']  # fix this part because we are supposed to use vars not strings
    print(f'Length = {len(name)}')
    if len(name) == 1:
        if yl in name[0]:
            print('Main chain cant be Substituent')
        elif ane in name[0]:
            ch(x)
        elif ene in name[0]:
            ch(x, 0, 0, 0, 1)
        elif yne in name[0]:
            ch(x, 0, 0, 0, 0, 1)
        else:
            print(f'Not valid')
        # elif:
        #     ch(x, 0, 0, 0, yne)
        # print(f'If no substitutient, Carbons chain must be termination "ane"\nElse specify the double or triple bond as X-{name[0]}')

    elif len(name) == 2:
        # this is in case the input is x-methene/yne
        if met in name[1]:  # 3 methene
            print('Methane is a CH4, no option for x-METHene/yne')
        elif ene in name[-1]:  # 2 pentene
            ch(name_check(name[-1]), 0, 0, 0, int(name[-2]))
        elif yne in name[-1]:  # 2 pentene
            ch(name_check(name[-1]), 0, 0, 0, 0, int(name[-2]))
        else:
            print(f'Termination must be "ene/yne"\nOtherwise enter only the name of a simple C chain')

    # if the name has 3 characters on it must be sus location-susType-chain#
    elif len(name) == 3:
        if met in name[-1]:
            print('Methane is a CH4, no option for x-METHene/yne')
        elif ane in name[-1]:
            if name[-3] == numbers[0]:
                print('Substituent location cannot be 0 nor 1')
            elif name[-3] == numbers[0]:
                print('*Substituent location cannot be 0 nor 1')
            else:
                ch(x, int(name[-3]), name_check(name[-2]))
        # ene no location given
        elif ene in name[-1] and name[-2][0:3] in prefix:
            ch(x, int(name[-3]), name_check(name[-2]), 0, 1)

        elif yne in name[-1] and name[-2][0:3] in prefix:
            ch(x, int(name[-3]), name_check(name[-2]), 0, 0, 1)

    elif len(name) == 4:
        if met in name[-1]:
            print('Methane is a CH4, no option for x-METHene/yne')
        # ex: 2 - 3 methyl pentane
        elif ane in name[-1]:
            if name[-4] not in numbers or name[-3] not in numbers or 'yl' not in name[-2]:
                print('Invalid: number-number-Substituent-chain accepted only')
            elif name[-2][0:3] in prefix:
                print('2 times Substituent')
                ch(x, int(name[-3]), name_check(name[-2]), int(name[-4]))
            else:
                print('Invalid: number-number-Substituent-chain accepted only')


        # ex: 3 methyl 4 pentene
        elif ene in name[-1]:
            if name[-2] in numbers:
                ch(name_check(name[-1]), int(name[-4]), name_check(name[-3]), 0, int(name[-2]))
        # ex: 4 methyl 5 hexyne
        elif yne in name[-1]:
            if name[-2] in numbers:
                ch(name_check(name[-1]), int(name[-4]), name_check(name[-3]), 0, 0, int(name[-2]))


# print('please input the name of the molecule in format\nnumber-substituentName-chain(ending in ane only)\nor\nnumber-number-(prefix)substituentName-chain(ending in ane only)')
molecule = input(': ')

name = []
numbers = range(1, 20)
dash = '-'
comma = ','
if dash in molecule:
    molecule = molecule.replace('-', ' ')
if comma in molecule:
    molecule = molecule.replace(',', '')
molecule_split = molecule.split()

for i in molecule_split:
    name.append(i.capitalize())

print(name)
print(f'Main chain = {name[-1]}')

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
undec = 'Undec'
dodec = 'Dodec'
hexdec = 'hexadec'
octadec = 'octadec'
ico = 'Ico'
##
yl = 'yl'
ane = 'ane'
ene = 'ene'
yne = 'yne'
left = 'left'.capitalize()
right = 'right'.capitalize()

screen = turtle.Screen()
screen.bgcolor('gray')
screen_x = 800
screen_y = 600
screen.setup(screen_x, screen_y)
# turtle.hideturtle()
turtle.penup()
turtle.shape()
turtle.shapesize(1.5)
turtle.goto(-screen_x / 2 + 50, 0)
turtle.pensize(2)
turtle.speed(5)
turtle.pendown()
turtle.right(45)
# print(f'Turtle pos = {turtle.pos()}')
sleep(2)

try:
    if met in name[-1]:
        number_of_carbons_on_main_chaing(1)

    elif et in name[-1]:
        number_of_carbons_on_main_chaing(2)

    elif prop in name[-1]:
        number_of_carbons_on_main_chaing(3)

    elif but in name[-1]:
        number_of_carbons_on_main_chaing(4)

    elif pent in name[-1]:
        number_of_carbons_on_main_chaing(5)

    elif hex in name[-1]:
        number_of_carbons_on_main_chaing(6)

    elif hept in name[-1]:
        number_of_carbons_on_main_chaing(7)

    elif oct in name[-1]:
        number_of_carbons_on_main_chaing(8)

    elif non in name[-1]:
        number_of_carbons_on_main_chaing(9)

    elif dec in name[-1]:
        number_of_carbons_on_main_chaing(10)

    # i am not activating this because undec has dec so it will recognized as 10 not 11, i still need to fix this
    # if undec in name[-1]:
    #     number_of_carbons_on_main_chaing(11)
    #
    # if dodec in name[-1]:
    #     number_of_carbons_on_main_chaing(12)
    #
    # if hexdec in name[-1]:
    #     number_of_carbons_on_main_chaing(16)
    #
    # if octadec in name[-1]:
    #     number_of_carbons_on_main_chaing(18)

    elif ico in name[-1]:
        number_of_carbons_on_main_chaing(20)
except TypeError:
    print('Double check if correctly written')

turtle.hideturtle()
screen.mainloop()
