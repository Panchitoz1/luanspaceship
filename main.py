from absl import app
from Functions import Get_input_as_flags as gi
from Functions import DrawSpaceship as ds
import subprocess


# Define a class/struct with desired parameters for spaceship
# that will be obtained as input via flags
class Spaceship:
    def __init__(self, length, color, style, ascii):
        self.length = length
        self.color = color
        self.style = style
        self.style = ascii

# When a user selects some flags, she/he can enable some functions
# with appropiated flags. This class/struct checks those options
class UserBoolOptions:
    def __init__(self, clipboard, help):
        self.clipboard = clipboard
        self.help = help


def main(argv):
    # Get parameters obtained with flags in command line
    spaceship_length, spaceship_color, spaceship_style,  user_clipboard, user_help = gi.GetInput(argv)

    #Create ASCII Spaceship art based on length provided by the user
    ascii_spaceship = ds.DrawLuanSpaceship(spaceship_length)
    print(ascii_spaceship)

    #Use values obtained with flags and assign them to classes/structs
    LuanSpaceship = Spaceship(spaceship_length, spaceship_color, spaceship_style, None)
    UserOptions = UserBoolOptions(user_clipboard, user_help)


if __name__ == "__main__":
    app.run(main)
