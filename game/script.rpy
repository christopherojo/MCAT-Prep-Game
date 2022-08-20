# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pheemail")

init python:
    def shuffle_answers(x):
        renpy.random.shuffle(x)
        return x

# The game starts here.

label start:
    
    $ correct = 0
    $ total = 0             # result of quiz game
    $ quiz_length = 2       # number of questions in one game
    $ q_to_ask = []         # list of questions to ask in one game

    # list of all possible questions
    # it consist of dictionaries, that describe each question:
    # key "question" has value of a question, key "category" makes sense for bot, key "answer" is a list of answers, that are lists [answer itself, right/wrong]
    # the order of this keys is not matter
    $ question1 = {"category": "logic", "question": "www?", "answer": [ ["w", "right"], ["q", "wrong"], ["e", "wrong"], ["r", "wrong"] ]}
    $ question2 = {"category": "abstract", "question": "....?", "answer": [ ["42", "right"], ["green", "wrong"], ["don\'t know", "wrong"], ["XoX", "wrong"] ]}
    $ question3 = {"category": "math", "question": "2+2?", "answer": [ ["4", "right"], ["5", "wrong"], ["100", "wrong"], ["42", "wrong"] ]}
    $ q_list = [question1, question2, question3]

    # let's choose some questions to play with
    while len(q_to_ask) < quiz_length:        # will work until we'll get enough questions for quiz
        $ a = renpy.random.choice (q_list)    # randomly pick a question from a list of all questions
        if a not in q_to_ask:                 # this question will be added only if we don't have it yet
            $ q_to_ask.append (a)

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

    p "Time for questions!"

    call questions

# This ends the game.

return

label questions:                              # game loop
    $ a = renpy.random.choice (q_to_ask)      # randomly pick the question from a list
    $ q_to_ask.remove (a)                     # remove it from list to not to ask it twice

    $ b = shuffle_answers (a["answer"])        # let's shuffle answers
            
    # ugly part... next variables are necessary to fill menu
    $ question = a["question"]
    $ category = a["category"]
    $ answ_0 = b[0][0]
    $ answ_1 = b[1][0]
    $ answ_2 = b[2][0]
    $ answ_3 = b[3][0]
    $ total += 1

    menu:
        "Category - [category]\nQ - [question]"
        "[answ_0]":
            if b[0][1] == "right":        # checks the description of question if it's the right one
                call correct
            else:
                call wrong
        "[answ_1]":
            if b[1][1] == "right":
                call correct
            else:
                call wrong
        "[answ_2]":
            if b[2][1] == "right":
                call correct
            else:
                call wrong
        "[answ_3]":
            if b[3][1] == "right":
                call correct
            else:
                call wrong
    
    $ quiz_length -= 1
    if quiz_length > 0:
        jump questions
            
    jump total

    return

label correct:
    show game girl happy

    p "Ding! Ding! Ding! That's one hour less you will have to spend working at McDonalds to cover your medical fees!"
    
    $ correct += 1

    return

label wrong:
    show game girl frustrated

    p "That's tough! You will be stuck working at McDonald's for life!"
    
    return

label total:
    show game girl normal

    p "You've gotten [correct] questions correct out of [total] total questions."

    return