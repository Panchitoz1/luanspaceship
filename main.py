from absl import app
from Functions import Get_input_as_flags as gi
import subprocess


# Define a class/struct with desired parameters for spaceship
# that will be obtained as input via flags
class Spaceship:
    def __init__(self, length, color, style):
        self.length = length
        self.color = color
        self.style = style

# When a user selects some flags, she/he can enable some functions
# with appropiated flags. This class/struct checks those options
class UserBoolOptions:
    def __init__(self, clipboard, help):
        self.clipboard = clipboard
        self.help = help


def main(argv):
    # Get parameters obtained with flags in command line
    spaceship_length, spaceship_color, spaceship_style,  user_clipboard, user_help = gi.GetInput(argv)

    #Use values obtained with flags and assign them to classes/structs
    LuanSpaceship = Spaceship(spaceship_length, spaceship_color, spaceship_style)
    UserOptions = UserBoolOptions(user_clipboard, user_help)


if __name__ == "__main__":
    app.run(main)
