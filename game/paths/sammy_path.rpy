init python:
    def sammy_test(script) -> bool:
        '''Suits are 
        H C S D

        Ranks are

        A 2 3 4 5 6 7 8 9 10 J Q K

        A hand is built like
        ['HA', 'HK', 'HQ', "HJ", "H10"] = "Royal Flush"
        '''
        tests = {
            ('HA', 'HK', 'HQ', "HJ", "H10"): "Royal Flush"
        }

label sammy_path:

    "This path is not implemented yet!"

    call screen who_to_help()

    return

define poker_hand_text = ""
define poker_hand_examples = ""
define poker_hand_instructions = ""

screen sammy_screen():
    frame:
        xpadding 100
        ypadding 30
        xalign 0.5
        yalign 0.5
        background Solid("000c") #may replace with something else
        text "[poker_hand_text]" xalign 0.5 yalign 0.1
        text "[poker_hand_examples]" xalign 0.5 yalign 0.325
        text "[poker_hand_instructions]" xalign 0.5 yalign 0.6
        text "TODO CHANGE" xalign 0.5 yalign 0.8
        textbutton "I have coded a file with poker_hand(hand)":
            xalign 0.5 
            yalign 0.9 
            action Return()

label sammy_problem:

    call screen sammy_screen() with fade

    jump sammy_file_dialog

label sammy_file_dialog:
    $ file = renpy.input("Please paste in a full path (/home/user/file.py) to your python file")
    menu:
        "Are you sure you this is the desired file? [file]"

        "Yes":
            if not file.endswith(".py"): 
                "File is not a python file"
                jump sammy_file_dialog
            elif not os.path.exists(file):
                "Provided path is not a valid path to a python file"
                jump sammy_file_dialog
            else:
                python: 
                    pack = load_script(file)
                    try:
                        result = sammy_test(pack)
                    except Exception as e:
                        sammy("Pretty little thing, something did not go right.")
                        narrator(f"{e}")
                        renpy.jump('sammy_file_dialog')
        "No":
            jump sammy_file_dialog

        "Instructions":
            jump sammy_problem

    if result:
        jump sammy_good_ending
    else:
        jump sammy_bad_ending

label sammy_good_ending:
    return

label sammy_bad_ending:
    return