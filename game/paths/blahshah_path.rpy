init python:
    def blahshah_test(script) -> bool:
        #script is of module type
        tests = {6: "BlooBlah", 16: "BlayBlah", 5: "", 9: "BlayBloo", 2: "Blah",
        36: "BlayBlooBlah", 28: "Blah", 30: "BlooBlah", 69: "Bloo", 1984: "Blah",
        100: "BlayBlah", 144: "BlayBlooBlah", 0: "BlayBlooBlah"}
        score = 0
        

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

    jump blahshah_problem

define BlayBlooBlah_text = "BlayBlooBlah is like FizzBuzz. A number has 'Blay' when \
it is a square of 2. A number has 'Bloo' when it is divisible by three. A number has \
'Blah' when it is an integer when multiplied by 1.5. The tests will not give you \
negative numbers."

define BlayBlooBlah_examples = '''Examples:
30 = BlooBlah
69 = Bloo
1984 = Blah
100 = BlayBlah
144 = BlayBlooBlah
5 = ""
'''

define BlayBlooBlah_instructions = "You will provide a python script with \
method 'BlayBlooBlah(i: int)', which will return a string. If a number does not \
quality for BlayBlooBlah, return an empty string. This file will be given as a full \
path to the incoming text input box. Code this python script in any code editor you \
desire."

screen blahshah_screen():
    frame:
        xpadding 100
        ypadding 30
        xalign 0.5
        yalign 0.5
        background Solid("000c") #may replace with something else
        text "[BlayBlooBlah_text]" xalign 0.5 yalign 0.1
        text "[BlayBlooBlah_examples]" xalign 0.5 yalign 0.325
        text "[BlayBlooBlah_instructions]" xalign 0.5 yalign 0.6
        text "BlayBlooBlah(i: int) -> str:" xalign 0.5 yalign 0.8
        textbutton "I have coded a file with BlayBlooBlah(i)":
            xalign 0.5 
            yalign 0.9 
            action Return()


label blahshah_problem:

    #PUT SCREEN UP FOR SHOWING TODO
    # PROBLEM
    # EXAMPLE CASES
    # INSTRUCTIONS (SHOULD BE IN A PYTHON FILE WITH METHOD BlayBlooBlah())
    # CONFIRMATION BUTTON

    call screen blahshah_screen() with fade

    jump blahshah_file_dialog

label blahshah_file_dialog:
    $ file = renpy.input("Please paste in a full path (/home/user/file.py) to your python file")
    menu:
        "Are you sure you this is the desired file? [file]"

        "Yes":
            if not file.endswith(".py"): 
                "File is not a python file"
                jump blahshah_file_dialog
            elif not os.path.exists(file):
                "Provided path is not a valid path to a python file"
                jump blahshah_file_dialog
            else:
                python: 
                    pack = load_script(file)
                    try:
                        result = blahshah_test(pack)
                    except Exception as e:
                        blahshah("Uh, you are going to need to fix this")
                        narrator(f"{e}")
                        renpy.jump('blahshah_file_dialog')
        "No":
            jump blahshah_file_dialog

    return

label blahshah_good_ending:
    pass

label blahshah_bad_ending:
    pass