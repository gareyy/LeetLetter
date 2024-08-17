define player = Character("")

define blahshah = Character("Blashah")

define sammy = Character("Sammy")

define hopper = Character("Hopper")

label start: #testing type shit
    $ player.name = "Mr Testy"
    
    #jump start_club
    jump blahshah_file_dialog

label introduction:

    scene bg black

    "It had been a week since my crush of 7 years got a partner."

    "They said they were the one, and they were right."

    "I met them, they were a nice guy."

    "Certainly better than me at being a partner to my crush."

    "But life has to move on, and so should I."

    "My life up until this point had been defined in keeping them company."

    "I will now need to be a new person from here on out."

    jump naming

label naming:

    define input_name = ""
    $ input_name = renpy.input("Well, what is my name?")
    while input_name == "":
        player "if I want to move on from this heartbreak, I will need to define myself."
        $ input_name = renpy.input("(Please insert a name, this is mandatory)")
        # if player does not give a name, repeat
    
    menu:
        "Am I sure this is my identity?"

        "Yes":
            $ player.name = input_name.strip()
            jump to_school
        
        "No":
            jump naming

