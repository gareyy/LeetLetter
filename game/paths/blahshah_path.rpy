init python:
    def blahshah_test(script) -> bool:
        #script is of module type
        tests = {6: "BlooBlah", 16: "BlayBlah", 5: "", 9: "BlayBloo", 2: "Blah",
        36: "BlayBlooBlah", 28: "Blah", 30: "BlooBlah", 69: "Bloo", 1984: "Blah",
        100: "BlayBlah", 144: "BlayBlooBlah", 0: "BlayBlooBlah"}
        score = 0
        for k, v in tests.items():
            if script.blayblooblah(k) == v:
                score += 1
        return score >= (len(tests) / 2)
        

label blahshah_path:

    scene bg black with fade
    scene bg classroom with fade

    show blahshah neutral

    blahshah "BlayBlooBlah, BlayBlooBlah..."

    player "What?"

    blahshah "Let me explain it to you"

    blahshah "Blay is when a number is a power of two."

    blahshah "Bloo is when a number is divisible by three."

    blahshah "Blah is when a number is an integer when multiplied by 1.5."

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
            blahshah "Thats correct actually."

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

        "Instructions":
            jump blahshah_problem

    if result:
        jump blahshah_good_ending
    else:
        jump blahshah_bad_ending

label blahshah_good_ending:
    show bg classroom
    show blahshah neutral

    blahshah "Oh! Successful test!"

    blahshah "How experienced are you at this?"

    player "Oh uh, not that much."

    blahshah "Wow, so you are a natural at programming?"

    player "Suprisingly, I guess so."

    show blahshah blushing

    player "Uh?"

    blahshah "J-Join me later, by the tree at the lake."

    player "That tree?"

    blahshah "Y-yeah."

    scene bg black with fade

    "Time passes, the programming club meeting wraps up, and I follow Blahshah 
    to the tree by the lake."

    scene bg confessiontree

    blahshah "Hey! Wait up [player]!"

    show blahshah neutral

    blahshah "*panting* Silly! Don't get ahead! You know I can't run for long."

    player "I've only known you for a day, how am I supposed to know that?"

    blahshah "I don't know, it just felt like I have known you for forever."

    player "..."

    blahshah "Yeah, i've been reading that code. Somehow, despite knowing nothing
            about coding, you've managed to solve my problem."

    player "..."

    blahshah "Isn't that lovely to see? One can know a person through their programming."

    player "What? That's a ridiculous claim."

    blahshah "I think what makes a person beautiful is their intelligence."

    blahshah "How the human mind can solve complicated problems."

    player "..."

    player "I have to confess to you something Blahshah."

    show blahshah blushing

    blahshah "Huh?"

    player "..."

    player "Well, I've kind of lied about my own programming skill."

    player "I haven't really coded since I was in grade 3."

    blahshah "Oh."

    player "It's kind of funny right?"

    #show blahshah sad

    blahshah "Oh.."

    blahshah "I thought you were going to confess to me."

    player "..!"

    show blahshah mad

    blahshah "You idiot!"

    player "What?"

    show blahshah neutral

    blahshah "Sorry for that..."

    blahshah "I have a problem with expressing love."

    blahshah "Or rather my inability to express love properly."

    blahshah "Kind of a left over instinct I have from a past breakup."

    blahshah "I don't think I have recovered from that."

    blahshah "Ever since then, I hide my feelings too much."

    blahshah "Maybe until I met you today."

    return

label blahshah_bad_ending:
    show bg classroom
    show blahshah neutral

    return