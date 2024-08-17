init python:
    def sammy_test(script) -> bool:
        '''Suits are 
        H C S D

        Ranks are

        A 2 3 4 5 6 7 8 9 10 J Q K

        A hand is built like
        ['HA', 'HK', 'HQ', "HJ", "H10"] = "Royal Flush"

        No special secret suits like in balatro
        '''
        tests = { #KEYS MUST BE TUPLES
            ('HA', 'HK', 'HQ', "HJ", "H10"): "Royal Flush",
            ("S2", "H3", "H4", "D5", "C6"): "Straight",
            ("C6", "C5", "C4", "C3", "C2"): "Straight Flush",
            ("HA", "DA", "HK", "CQ", "D2"): "Pair",
            ("C2", "C4", "CQ", "CA", "C10"): "Flush",
            ("D10", "H9", "S2", "H3", "D5"): "High Card",
            ("D10", "D10", "H10", "C5", "C5"): "Full House",
            ("D5", "H5", "C5", "S5", "S4"): "Four of a kind"
        }
        score = 0
        for k, v in tests.items():
            if script.spiral(k) == v:
                score += 1
        
        return score >= (len(tests) * 0.8)

label sammy_path:
    scene bg classroom
    show sammy neutral

    jump sammy_problem


define poker_hand_text = "Detect what kind of poker hand comes from a set of 5 cards. \
Cards come in a combination of suit and rank. Suits are \
H, C, D, and S. Ranks are A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, and K. Hands are \
the standard poker hands, High Card, Pair, Two Pair, Three of a kind, Straight, \
Flush, Full House, Four of a kind, Straight Flush, Royal Flush."
define poker_hand_examples = '''Examples
HA, HK, HQ, HJ, H10: Royal Flush
S2, H3, H4, D5, C6: Straight
HA, DA, HK, CQ, D2: Pair
D10, D10, H10, C5, D5: Full House
'''
define poker_hand_instructions = "You will provide a python script with method \
'poker_hand(hand: tuple[[str])', which will return a string. The tests will not provide \
invalid hands. This file will be inputted as a full path to the incoming text box. \
Code this python script in any editor you desire."

screen sammy_screen():
    frame:
        xpadding 100
        ypadding 30
        xalign 0.5
        yalign 0.5
        background Solid("000c") #may replace with something else
        text "[poker_hand_text]" xalign 0.5 yalign 0.1
        text "[poker_hand_examples]" xalign 0.5 yalign 0.4
        text "[poker_hand_instructions]" xalign 0.5 yalign 0.6
        text "poker_hand(hand: tuple[[str]) -> str" xalign 0.5 yalign 0.8
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

    "Ending: Good ending with Sammy"
    return

label sammy_bad_ending:

    "Ending: Bad ending with Sammy"
    return