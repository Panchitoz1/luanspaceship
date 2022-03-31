# To draw our spaceship we will separate in into 4 pieces
# Finally, we will just 'concadenate' them
def DrawLuanSpaceship(length):
   top = drawTopSpaceship(length)
   mid_top = drawMidTopSpaceship(length)
   mid_bottom = drawMidBottomSpaceship(length)
   bottom = 'a'
      
   return top+mid_top+mid_bottom


# Draw the top part of the spaceship
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


# Draw the mid-top part of the spaceship
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


# Draw mid-bottom part of the spaceship 
def drawMidBottomSpaceship(length):
    # First, check 2 special cases/lengths that do not follow a pattern
    if length == 1:
        return "/|_|\\"

    if length == 2:
        midbottom_spaceship = ''
        midbottom_spaceship += ' ' * (1*length - 1)
        midbottom_spaceship += '/|'
        midbottom_spaceship += ' ' * (2*length - 1)
        midbottom_spaceship += '|\\\n'
        midbottom_spaceship += '/ |'
        midbottom_spaceship += '_' * (2*length - 1)
        midbottom_spaceship += '| \\\n'
        return midbottom_spaceship

    midbottom_spaceship = ''
    start = length//3 
    counter = 0

    for x in range(1, length+1):
        if x > start:
            midbottom_spaceship += ' ' * (1*length - x + start)
            midbottom_spaceship += '/'
            midbottom_spaceship += ' ' * counter
            midbottom_spaceship += '|'
            if x == length:
                midbottom_spaceship += '_' * ((2*length) - 1)
            else:
                midbottom_spaceship += ' ' * ((2*length) - 1)
            midbottom_spaceship += '|'
            midbottom_spaceship += ' ' * counter
            midbottom_spaceship += '\\\n'
            counter += 1
        else:
            midbottom_spaceship += ' ' * length 
            midbottom_spaceship += '|'
            midbottom_spaceship += ' ' * ((2*length) - 1)
            midbottom_spaceship += '|\n'
    return midbottom_spaceship
            
        
