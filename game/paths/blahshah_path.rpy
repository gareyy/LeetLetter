init python:
    def blahshah_test(script):
        #script is of module type
        pass

label blahshah_path:

    scene bg black with fade
    scene bg classroom with fade

    show blahshah neutral

    blahshah "BlayBlooBlah, BlayBlooBlah..."

    player "What?"

    blahshah "Let me explain it to you"

    blahshah "Blay is when a number is a power of two"

    blahshah "Bloo is when a number is divisible by three"

    blahshah "Blah is when a number is an integer when multiplied by 1.5"

    blahshah "6 is a BlooBlah, 16 is a BlayBlah, 5 is none of them, 9 is a BlayBloo,
        2 is just a Blah, 36 is a BlayBlooBlah..."

    player "Ok ok, I get the point!"

    show blahshah mad
    blahshah "Don't insult me baka!"

    player "I just, know what to do already!"

    blahshah "Then what is 28?"

    menu:
        "What is 28?"

        "BlayBloo":
            blahshah "Wrong stupid!"

        "Blah":
            show blahshah blushing
            blahshah "Thats correct actually"

        "BlooBlah":
            blahshah "Wrong stupid!"
    
    show blahshah neutral

    blahshah "Alright, I already have the tests, let me see you code."

    #PUT SCREEN UP FOR SHOWING TODO
    # PROBLEM
    # EXAMPLE CASES
    # INSTRUCTIONS (SHOULD BE IN A PYTHON FILE WITH METHOD BlayBlooBlah())
    # CONFIRMATION BUTTON WITH WAIT OF 30 SECONDS

label blahshah_file_dialog:
    $ file = renpy.input("Please paste in a full path (/home/user/file.py) to your python file")
    menu:
        "Are you sure you this is the desired file? [file]"

        "Yes":
            if not file.endswith(".py"):
                "File is not a python file"
                jump blahshah_file_dialog
            else:
                python: 
                    pack = load_script(file)
                    try:
                        pack.testie() # HAHA I DID IT
                    except Exception as e:
                        blahshah("Uh, you are going to need to fix this")
                        narrator(e)
                        jump(blahshah_file_dialog)
                        

        "No":
            jump blahshah_file_dialog

    return