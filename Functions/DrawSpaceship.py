

# To draw our spaceship we will separate in into 4 pieces
# Finally, we will just 'concadenate' them
def DrawLuanSpaceship(length):
   top = drawTopSpaceship(length)
   mid_top = drawMidTopSpaceship(length)
   mid_bottom = 'a'
   bottom = 'a'
      
   return top+mid_top


def drawTopSpaceship(length):
    top_spaceship = ''
   
    for i in range(0, length+1):
        if i == 0:
             top_spaceship += ' '*2*length
             top_spaceship += '^\n'
        
        elif i == length:
            top_spaceship += ' '*length 
            top_spaceship += '/'
            top_spaceship += '_'*((2*length)-1)
            top_spaceship += '\\\n'

        else:
            top_spaceship += ' '*(2*length-i)             
            top_spaceship += '/'
            top_spaceship += ' '*((2*i) - 1)
            top_spaceship += '\\\n'

    return top_spaceship

def drawMidTopSpaceship(length):
    midtop_spaceship = ''
    
    for j in range(0, length):

        midtop_spaceship += ' ' * length
        midtop_spaceship += '|'

        if j == length-1:
            midtop_spaceship += '_' * (2*length - 1)
        else: 
            midtop_spaceship += ' ' * (2*length - 1)

        midtop_spaceship += '|\n'

    return midtop_spaceship
    
