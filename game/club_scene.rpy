screen who_to_help():
    frame:
        xpadding 30
        ypadding 30
        xalign 0.5
        yalign 0.5
        xysize (800, 500)
        background Solid("000c") #may replace with something else
        text "Who do I help?" xalign 0.5 yalign 0.1
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton idle "blahshah button" action Jump("blahshah_path")
            imagebutton idle "sammy button" action Jump("sammy_path")
            imagebutton idle "hopper button" action Jump("hopper_path")


label start_club:
    "I follow Sammy and Blahshah into the mysterious room ###-####"

    scene bg classroom with fade

    show hopper neutral

    "Goth Girl" "Uh, hello"

    show sammy neutral at right

    sammy "[player], this is our gracious little Hopper!"

    hopper "Shut up" 

    sammy "Anyway, now we have one more person, we can get our club off the ground!"

    show blahshah neutral at left

    blahshah "Yeah!"

    blahshah "Proper introductions are in order!"

    hopper "Oh no"

    hide hopper
    hide sammy
    show blahshah neutral at center

    blahshah "My name is Blahshah! 
                I am the founder of the Toruvalds High School Programming Club!"

    player "Can you explain the whole shark thing?"

    show blahshah blushing

    blahshah "No! I am a classic anime girl through and through baka!"

    blahshah "You are such a fool!"

    player "Woah! Easy there Blahshah!"

    show blahshah mad

    blahshah "Grrr!"

    blahshah "Shark Attack!"

    player "But you said you were not a shark!"

    "She tackles me to the ground"

    "Uh oh, she's perched on top of me"

    show blahshah blushing

    blahshah "..."

    blahshah "...."

    player "Lets get up"

    "I push her off me and stand up, she also stands up"

    show blahshah neutral

    blahshah "Anyway, as the founder, I have the most experience in programming
                so if any of you are struggling, come ask me!"

    "Uh oh, if I get caught lacking in programming skills, 
    they are totaly going to kill me! And my love quest will be over!"

    blahshah "Alright Sammy introduce yourself!"

    hide blahshah with fade
    show sammy neutral

    sammy "Well hello, beautiful little [player]"

    "He comes up close to me and pinches my chin"

    #show sammy blushing

    sammy "Wow, you look prettier up close"

    "Oh crap, my heart is beating too fast. I wish my old crush did this to me"

    "Hey! [player]! Think about other stuff! Now is not the time to dwell on past regrets!"

    sammy "Heh"

    "He lets go of my chin and steps back"

    sammy "Are you committed to a relationship handsome?"

    player "No?"

    "Hopper barges in Sammy's introduction"

    show hopper neutral at right with easeinright

    hopper "..."

    sammy "Uh, I'll leave them to you, I guess"

    hide sammy
    show hopper neutral

    hopper "..."

    player "Uh?"

    hopper "I see it in your eyes"

    player "What?"

    hopper "Heartbreak."

    "Huh? How does she know?"

    hopper "It's over for you, right? A love of seven years?"

    player "Uh, yeah? More like a crush..."

    hopper "Ha."

    "She pats my head"

    show hopper blushing

    hopper "There there, poor little thing"

    "She goes on to start scratching my hair lightly. This feels good..."

    "She takes her hand away"

    show hopper neutral

    hopper "..."

    hide hopper with fade
    show blahshah neutral at center with fade
    show sammy neutral at left with fade
    show hopper neutral at right with fade

    blahshah "Okay then! I guess we can start today's club activities!"

    blahshah "Let us begin with explaining our current projects!"

    hide hopper with fade
    hide sammy with fade

    blahshah "My project is a bunch of coding tests!"

    blahshah "Ever heard of fizzbuzz?"

    player "Uh, no?"

    blahshah "Well one of my tests is my own special version! BlayBlooBlah!"

    blahshah "Blay if a number is a power of two"

    blahshah "Bloo if a number is divisible by 3"

    blahshah "Blah if a number is an integer when multiplied by 1.5!"

    blahshah "And I need someone to code for it so I can see if my tests are good!"

    hide blahshah with fade
    show sammy neutral with fade

    sammy "My project is a poker game, but a little more complicated"

    sammy "In fact its so complicated that I don't even know how to add in the poker
            hand detection system"

    sammy "It's got everything from high cards to royal flushes, which complicates
            everything more"

    sammy "Maybe you could help me?"

    hide sammy with fade
    show hopper neutral with fade

    hopper "Spirals"

    hopper "Im making a spiral generator and I need help"

    hopper "The user inputs a spiral diameter and it generates a spiral"

    hopper "The spiral's dots are numbered"

    hopper "Don't ask what it is for"

    show hopper neutral at right
    show blahshah neutral
    show sammy neutral at left

    blahshah "So, [player], what is your project?"

    player "Um, I don't know, I only just got here"

    blahshah "Maybe you could help one of us out?"

    #TODO: Fancier menu
    call screen who_to_help()