init python:
    def hopper_test(script) -> bool:
        tests = {

        }

label hopper_path:

    "This path is not implemented yet!"

    call screen who_to_help()

    return

define spiral_text = ""
define spiral_examples = ""
define spiral_instructions = ""

screen hopper_screen():
    frame:
        xpadding 100
        ypadding 30
        xalign 0.5
        yalign 0.5
        background Solid("000c") #may replace with something else
        text "[spiral_text]" xalign 0.5 yalign 0.1
        text "[spiral_examples]" xalign 0.5 yalign 0.325
        text "[spiral_instructions]" xalign 0.5 yalign 0.6
        text "TODO CHANGE" xalign 0.5 yalign 0.8
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
    return

label hopper_bad_ending:
    return