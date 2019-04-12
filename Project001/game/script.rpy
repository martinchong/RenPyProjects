#First Renpy Game created by Martin Chong.
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Voice")
define mc = Character("[name]")
define e = Character("")
define a = Character("Agent Foster")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# The game starts here

label start:
    $pipe = 0
    $blood = 0
    $info = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    python:
        name = renpy.input("Before we start the game, let me know your name.\n"
        + "Unless you just wanna be a 'Nobody'")
        name = name.strip()
        if not name:
            renpy.say(e, "Okay fine, Nobody it is.")
            name = "Nobody"

    scene bg droom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    with flash

    e "You woke up in a dark room with nothing around but a table."

    mc "God. My head hurts like hell. What happened?"

    e "Buzzzz.... Buzz...."

    e "You seem to hear a mobile phone buzzing in your right pocket."

    menu:
        "Answer the phone.":
            jump pick

        "Ignore the phone.":
            jump nopick

    label pick:
        mc "Hello?"

        v "Thank god! You finally picked up."

        v "My name is Agent Foster from the FBI. Listen carefully,
        I know you are scared right now but please stay calm."

        v "We believe that you are the newest target of the serial killer known
        as 'I.F.'. Can you tell me where you are now?"

        menu:
            "Look around and tell him what you see.":
                jump obey

            "Ask for more info on this 'I.F.'.":
                jump question

    label nopick:
        mc "I don't have time for this. I need to find a way out"

        menu:
            "Look around the room.":
                jump look

            "Sit still and do nothing.":
                jump sit

    label question:
        a "I.F. is the initials of the killer, he is a master of deception. But
        enough chit chat, we must focus of getting you out of here. What can you
        tell me about the room you are in ?"
        $info = 1

        menu:
            "Look around and tell him what you see.":
                jump obey


    label look:
        e "You search around the room and find a broken metal pole."

        e "Got a broken metal pole."
        $pipe = 1

        e "You also see some red faded words on the wall that wrote 'Ivan
        Fos...' with the last few letters being too hard to read what it is."

        mc "Red? Is this blood!? It looks like it still hasnt dry off yet."
        $blood = 1

        e "There not much else around the room."

    label sit:
        e "After awhile, the phone rings again."

        menu:
            "Answer the phone.":
                jump pick

            "Ignore the phone.":
                jump end1
        return

    label obey:
        mc "I don't know. I am in a dark room with a table. I don't see much
        around by the looks of it."

        a "Maybe you can explore abit? Check around the room to see if theres
        any clue for us to know more?"

        menu:
            "Search around the room":
                jump search

    label search:
        if pipe == 0:
            e "You search around the room and find a broken metal pole."

            e "Got a broken metal pole."

            mc "I found a metal pole but I think it has much use."
            $pipe = 1

        e "You see some red faded words, but it seems it has dried off into a
        mess and you can't figure out whats wrriten."

        mc "Is this blood!? Sadly I can't seem to figure out what it says in
        such condition. If only I have found this earlier."

        if blood == 1:
            mc "Oh wait, I saw this earlier, I recall it wrotes 'Ivan Fos'."

            if info == 1:
                mc "It also fits the serial killers initial, I.F. Could it be?"

                menu:
                    "Ask for Agent Foster's first name":
                        jump confront
        jump end1

    label confront:
        mc "Excuse me Agent Foster? Do you mind telling me you first name?"

        a "You are trapped and you care what my first name is?"

        mc "Sorry but I am getting really stressed here, any kinda distraction
        can really help me stay sane."

        a "Fine... It's Ivan. My name is Ivan Foster. Can we please carry on?"

        menu:
            "Yes, lets carry on":
                jump end2

            "Hold up. This is strange, I sense something fishy":
                jump fishy

    label fishy:
        mc "No way this is coincidence, you are lying to me."

        a "What do you mean? Is this a joke? I am trying to save you here!"

        mc "I would hope thats true but there is just too many effidence that
            suggest otherwise. First off..."

        menu:
            "Agent Foster's real name":
                jump fishy2

            "Agent Foster's real age":
                a "Age? Like I am old of something?"
                jump fail

            "Agent Foster's real estate":
                jump fail

    label fishy2:
        mc "You name is written on the wall."

        a "Hold up. How would you know that's my name when half of it is
            blurred out?"

        mc "And how would you know half of it is blurred out? I don't recall
            tell you that."

        e "This is good, he's panicing, I should keep on going."

        a "Okay, so what if it's my name? It doesn't mean anything."

        mc "It surely does, the relation between your name and the killer is..."

        menu:
            "The number of words":
                jump fail

            "The meaning of it":
                jump fail

            "The initials":
                jump fishy3

    label fishy3:
        mc "You name's initials are same as the killer's initials!"


    label fail:
        a "Is that all you have to say? That makes comepletely no sense."

        mc "Emmmmmmm... I guess you are right..."

        mc "I am sorry, I wasn't thinking straight."

    label end1:
        e "You hear something buzzing again but this time its not the phone."

        e "You looked around and found a bomb under the chair"

        return


    label end2:
        a "Okay, I just got word from our tech team, they said if you dial
            our secure line, we can track the GPS on your phone."
        a "Try punching in 6668241121."

        e "You punched in the numbers and dial"

        mc "Done! What now?"

        a "HAHAHAHA. Now you die, you just activiated your own death trap."

        jump end1


        return

    # This ends the game.

    return
