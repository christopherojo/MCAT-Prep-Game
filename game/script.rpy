# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pheemail")

# The game starts here.

label start:
    
    $ correct = 0
    $ total = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show game girl normal

    # These display lines of dialogue.

    p "You're a cringe Med Sci kid."

    p "I am going to make you a successful cringe Med Sci kid!"

    call question1
    call question2

# This ends the game.

return

label correct:
    show game girl happy

    p "Ding! Ding! Ding! That's one hour less you will have to spend working at McDonalds to cover your medical fees!"
    
    $ correct += 1

    call total

    return

label wrong:
    show game girl frustrated

    p "That's tough! You will be stuck working at McDonald's for life!"

    call total
    
    return

label total:
    show game girl normal

    $ total += 1

    p "You've gotten [correct] questions correct out of [total] total questions."

    return

label question1:

    p "Time for questions!"

    menu:

        p "What is the approximate number of cells in the body?"

        "37 trillion":
            call correct

        "43 billion":
            call wrong

        "219 million":
            call wrong

    return

label question2:    
    p "Question 2, coming in hot!"

    menu:

        p "What is the ratio of bacterial to eukaryotic cells in the human body?"

        "1:8":
            call wrong

        "10:1":
            call correct

        "100:1":
            call wrong

    return
