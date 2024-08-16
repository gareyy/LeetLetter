# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("")

define blahshah = Character("Blashah")

# The game starts here.

label introduction:

    player ""
    jump naming

label naming:

    define input_name = ""
    $ input_name = renpy.input("Well, what is my name?")
    while input_name == "":
        player "if I want to move on from this heartbreak, I will need to define myself"
        $ input_name = renpy.input("(Please insert a name, this is mandatory)")
        # if player does not give a name, repeat
    
    menu:
        "Am I sure this is my identity?"

        "Yes":
            $ player.name = input_name.strip()
        
        "No":
            jump naming

label to_school:

    return
