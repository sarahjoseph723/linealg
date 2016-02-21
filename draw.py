from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    A = abs(x0 - x1)
    B = -abs(y0 - y1)
    if dy == 0: #slope undefined, vertical line
        #do stuff
        pass
    if dx == 0: #horizontal line
        #do stuff
        pass
    m = dx/dy
    #octant 1/5
    if m >= 0 && m <= 1:
        while (x <= x0):
            plot(screen, color, x, y)
            if d > 0:
                y += 1
            x += 1
            d += 2A

   ''' #octant 2/6
    if m >= 0 && m >= 1:
    #octant 3/7
    if m <= 0 && m <= -1:
    #octant 4/8
    if m <= 0 && m >= -1:
    '''
