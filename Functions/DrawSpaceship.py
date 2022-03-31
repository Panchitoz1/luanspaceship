

# To draw our spaceship we will separate in into 4 pieces
# Finally, we will just 'concadenate' them
class ASCII_Spaceship:
    def __init__(self, top, mid_top, mid_bottom, bottom):
        self.top = top
        self.mid_top = mid_top 
        self.mid_bottom = mid_bottom
        self.bottom = bottom



def DrawLuanSpaceship(length):
   top = drawTopSpaceship(length)
   mid_top = 'a'
   mid_bottom = 'a'
   bottom = 'a'
   spaceship = ASCII_Spaceship(top, mid_top, mid_bottom, bottom)
   
   return top


def drawTopSpaceship(length):
    init_spaces = 2*length
    top_spaceship = ''
   
    for i in range(0, length+1):
        if i == 0:
             top_spaceship += ' '*init_spaces
             top_spaceship += '^\n'
        
        elif i == length:
            top_spaceship += ' '*length 
            top_spaceship += '/'
            top_spaceship += '_'*((2*length)-1)
            top_spaceship += '\\\n'

        else:
            top_spaceship += ' '*(init_spaces-i)             
            top_spaceship += '/'
            top_spaceship += ' '*((2*i) - 1)
            top_spaceship += '\\\n'

    return top_spaceship


