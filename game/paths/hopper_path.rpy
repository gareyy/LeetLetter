init python:
    def hopper_test(script) -> bool:
        # input int will be in 1 <= n <= 9
        # will always be clockwise from inside
        tests = {
            3: '''07 08 09
            06 01 02
            05 04 03''',

            5: '''21 22 23 24 25
            20 07 08 09 10
            19 06 02 02 11
            18 05 04 03 12
            17 16 15 14 13''',
            
            1: '''01''',

            2: '''01 02
            04 03'''
        }
        score = 0
        for k, v in tests.items():
            if script.spiral(k) == v:
                score += 1
        
        return score >= (len(tests) * 0.8)

label hopper_path:

    scene bg classroom
    show hopper neutral

    "DEMO" "Unfortunately, the narrative parts of this romance path have not been implemented yet"

    "DEMO" "The problem code for this path has been implemented."

    "DEMO" "You may choose to continue with exploring this romance path, or go to the Blahshah path \
    which is the only fully implemented path."

    menu:
        "Where to go?"

        "Go to Blahshah path":
            jump blahshah_path
        
        "Continue Hopper Path":
            jump hopper_problem

    return

define spiral_text = "Your code will generate a spiral, with double digit numbers as \
the dots. This spiral will be clockwise from the inner most dot. The input will be \
an integer which will be the diameter. The output will be a multiline string, so use \
triple quotation mark strings."
define spiral_examples = '''Examples:
diam = 3    diam = 5

07 08 09    21 22 23 24 25
06 01 02    20 07 08 09 10
05 04 03    19 06 01 02 11
                18 05 04 03 12
                17 16 15 14 13'''
define spiral_instructions = "You will provide a python script with method \
spiral(diam: int), where the output is a multiline string. The tests will only \
have inputs in range 1 to 9. This file will be inputted as a full path to the incoming text box. \
Code this python script in any editor you desire."

screen hopper_screen():
    frame:
        xpadding 100
        ypadding 30
        xalign 0.5
        yalign 0.5
        background Solid("000c") #may replace with something else
        text "[spiral_text]" xalign 0.5 yalign 0.1
        text "[spiral_examples]" xalign 0.5 yalign 0.4
        text "[spiral_instructions]" xalign 0.5 yalign 0.7
        text "spiral(diam: int) -> str" xalign 0.5 yalign 0.8
        textbutton "I have coded a file with spiral(diam)":
            xalign 0.5 
            yalign 0.9 
            action Return()

label hopper_problem:

    call screen hopper_screen() with fade

    jump hopper_file_dialog

label hopper_file_dialog:
    $ file = renpy.input("Please paste in a full path (/home/user/file.py) to your python file")
    menu:
        "Are you sure you this is the desired file? [file]"

        "Yes":
            if not file.endswith(".py"): 
                "File is not a python file"
                jump hopper_file_dialog
            elif not os.path.exists(file):
                "Provided path is not a valid path to a python file"
                jump hopper_file_dialog
            else:
                python: 
                    pack = load_script(file)
                    try:
                        result = hopper_test(pack)
                    except Exception as e:
                        #show hopper concerned
                        hopper("Oh, something is bad")
                        narrator(f"{e}")
                        renpy.jump('hopper_file_dialog')
        "No":
            jump hopper_file_dialog

        "Instructions":
            jump hopper_problem

    if result:
        jump hopper_good_ending
    else:
        jump hopper_bad_ending

label hopper_good_ending:
    scene bg black
    hide hopper
    "Ending: Good ending with Hopper"
    return

label hopper_bad_ending:
    scene bg black
    hide hopper
    "Ending: Bad ending with Hopper"
    return