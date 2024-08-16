# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("")

define blahshah = Character("Blashah")

define sammy = Character("Sammy")

define hopper = Character("Hopper")

# The game starts here.

label start: #testing type shit
    $ player.name = "Mr Testy"
    jump to_school

label introduction:

    "It had been a week since my crush of 7 years got a partner"

    "They said they were the one, and they were right"

    "I met them, they were a nice guy"

    "Certainly better than me at being a partner to my crush"

    "But life has to move on, and so should I"

    "My life up until this point had been defined in keeping them company"

    "I will now need to be a new person from here on out"

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

    player "A journey of a thousand steps starts with one"

    "I got ready for school for the first time in a week, 
    ever since I saw my crush confess their love to them"

    "The walk to school was a bit hard, I had done it a million times 
    before, but emotionally, I was still not prepared"

    "However, some sort of treat awaited for me at the school gates"

    #scene bg school front

    #show blahshah shadow

    "Pretty Girl" "Come join the programming club! We still do not have enough members!"

    "I approached her, pretending to be interested in programming"

    "Well, I haven't done any coding since year 3, so I better win an oscar for
    the acting im about to do"

    player "Hey!"

    "Pretty Girl" "Hello there!"

    "I get a closer look at her face, and..."

    #show blahshah normal

    #TODO implement screen shaking?
    "She's a shark???????????"

    "Pretty Shark" "Well hello there? May I ask for your name?"

    player "its, uh, [player]..."

    "Pretty Shark" "Well hello [player]! My name is Blahshah!"

    "Blahshah?"

    blahshah "Are you interested in coding perchance?"

    player "You simply can't say perchance, but yeah, I have some idea of programming"

    return
