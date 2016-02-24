from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x0 - x1
    dy = y0 - y1
    if (dx > 0 && dy >= 0 and abs(dx) >= abs(dy)):
        one(screen, x0, y0, x1, y1, color)
    elif (dx >= 0 && dy > 0 and abs(dx) < abs(dy)):
        two(screen, x0, y0, x1, y1, color)
    elif (dx < 0 && dy > 0 and abs(dx) <= abs(dy)):
        three(screen, x0, y0, x1, y1, color)
    elif (dx < 0 && dy > 0 and abs(dx) <= abs(dy)):
        four(screen, x0,y0, x1,y1, color)
    elif (dx < 0 && dy < 0 and abs(dx) >= abs(dy)):
        one(screen, x1,y1, x0,y0, color)
    elif (dx <= 0 && dy < 0 and abs(dx) < abs(dy)):
        two(screen, x1, y1, x0, y0, color)
    elif (dx > 0 && dy < 0 and abs(dx) <= abs(dy)):
        three(screen, x1, y1, x0, y0, color)
    elif (dx > 0 && dy < 0 and abs(dx) > abs(dy)):
        four(screen, x1, y1, x0, y0, color)
    else:
        print "uh oh"
    
def one(screen, x0,y0, x1,y1, color):
    x = x0
    y = y0
    dx = abs(x1-x0)
    dy = abs(y1 - y0)
    A = dy
    B = -1 * dx
    d = 2*A + B
    while (x <= x1):
        plot(screen, color, x, y)
        if (d > 0):
            y += 1
            d += 2 * B
        x += 1
        d += 2 * A


def two(screen, x0,y0, x1,y1, color):
    x = x0
    y = y0
    dx = abs(x1-x0)
    dy = abs(y1 - y0)
    A = dy
    B = -1 * dx
    d = 2*B + A
    while (x <= x1 and y <= y1):
        plot (screen, color, x, y)
        if (d < 0):
            x += 1
            d += 2 * A
        y += 1
        d += 2 * B

def three(screen, x0,y0, x1,y1, color):
    x = x0
    y = y0
    dx = abs(x1-x0)
    dy = abs(y1 - y0)
    A = dy
    B = -1 * dx
    d = 2*B + A
    while (x >= x1):
        plot (screen, color, x, y)
        if (d < 0):
            x += 1
            d += 2 * A
        y += 1
        d += 2 * B

def four(screen, x0,y0, x1,y1, color):
    x = x0
    y = y0
    dx = abs(x1-x0)
    dy = abs(y1 - y0)
    A = dy
    B = -1 * dx
    d = 2*A + B
    while (x >= x1):
        plot (screen, color, x, y)
        if (d < 0):
            x += 1
            d += 2 * A
            y += 1
            d += 2 * A
