
def ApplyLSystem(string, baserule1, baserule2, rule1, rule2, n):
    if (n <= 0):
        return string
    else:
        for i in range(n):          
            string = string.replace(baserule1, rule1)       #replaces the F in string(FB) with (F+B)
            string = string.replace(baserule2, rule2)       #replaces the B in string(F+BB) with (F-B)
        return string


def DrawLSystem(theturtle, color, thestring,):
    theturtle.color(color)
    for i in range(len(thestring)):
        if (thestring[i] == 'F'):
            theturtle.forward(5)
        elif (thestring[i] == 'B'):
            theturtle.forward(5)
        elif (thestring[i] == '+'):
            theturtle.right(90)
        elif (thestring[i] == '-'):
            theturtle.left(90)

