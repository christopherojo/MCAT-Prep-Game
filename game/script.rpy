# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pheemail")

# The game starts here.

label start:

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

    show game girl normal

    return

label wrong:
    show game girl frustrated

    p "That's tough! You will be stuck working at McDonald's for life!"

    show game girl normal
    
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
    p "Couldn't be me working at McDonald's"