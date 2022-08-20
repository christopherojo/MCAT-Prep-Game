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
    $ total = 0
    $ right_answers = 0     # result of quiz game
    $ quiz_length = 2       # number of questions in one game
    $ q_to_ask = []         # list of questions to ask in one game

    # list of all possible questions
    # it consist of dictionaries, that describe each question:
    # key "question" has value of a question, key "category" makes sense for bot, key "answer" is a list of answers, that are lists [answer itself, right/wrong]
    # the order of this keys is not matter
    $ question1 = {"question": "www?", "answer": [ ["w", "right"], ["q", "wrong"], ["e", "wrong"], ["r", "wrong"] ], "category": "logic"}
    $ question2 = {"question": "....?", "answer": [ ["42", "right"], ["green", "wrong"], ["don\'t know", "wrong"], ["XoX", "wrong"] ], "category": "abstract"}
    $ question3 = {"question": "2+2?", "answer": [ ["4", "right"], ["5", "wrong"], ["100", "wrong"], ["42", "wrong"] ], "category": "math"}
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

    menu:
        "Category - [category]\nQ - [question]"
        "[answ_0]":
            if b[0][1] == "right":        # checks the description of question if it's the right one
                $ right_answers += 1
                "That's true."
            else:
                "Nope."
        "[answ_1]":
            if b[1][1] == "right":
                $ right_answers += 1
                "That's true."
            else:
                "Nope."
        "[answ_2]":
            if b[2][1] == "right":
                $ right_answers += 1
                "That's true."
            else:
                "Nope."
        "[answ_3]":
            if b[3][1] == "right":
                $ right_answers += 1
                "That's true."
            else:
                "Nope."
    
    $ quiz_length -= 1
    if quiz_length > 0:
        jump questions
            
    "The result is - [right_answers]"

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
    $ answers1 = ["37 trillion", "43 billion", "219 million"]
    $ shuffleAnswers(answers1)

    menu:

        p "What is the approximate number of cells in the body?"

        "[answers1[0]]":
            call correct

        "[answers1[1]]":
            call wrong

        "[answers1[2]]":
            call wrong

    return

label question2:

    menu:

        p "What is the ratio of bacterial to eukaryotic cells in the human body?"

        "1:1":
            call wrong

        "10:1":
            call correct
            
        "2 million:1":
            call wrong

    return

label question3:

    menu:

        p "Which is the tenet that is CORRECT regarding cell theory?"

        "1. All living things are composed of cells 2. The cell is the basic functional unit of life 3. Cells arise only from preexisting cells 4. Cells carry genetic info (DNA), passed onto daughter cells.":
            call correct

        "Cells only make up eukaryotes.":
            call wrong

        "There are different forms of storage for genetic information that gets passed onto future cells.":
            call wrong

    return

label question4:

    menu:

        p "Membrane Bound Organelles Properties RECALL: - phospholipid bilayer is hydro______ outside and hydro_____ inside - Purpose of asymmetrical? - What is the purpose of the cytosol?"

        "1. hydrophobic outside, hydrophilic inside 2. So it can interact with whatever with greater affinity and selectivity 3. Structural component of the cells.":
            call correct

        "1. hydrophilic outside, hydrophobic inside 2. To keep hydrophilic molecules inside the cell and hydrophobic molecules out 3. Structural component of the cells.":
            call wrong

        "1. hydrophilic outside, hydrophobic inside 2. So it can interact with whatever with greater affinity and selectivity 3. Allows for diffusion of molecules throughout the cell.":
            call wrong

    return

label question5:

    menu:

        p "Nucleus Properties - What is a main purpose of the compartmentalization of DNA in the nucleus - Explain the function of the nucleolus, how can you identify it?"

        "1. Protects DNA from external damage 2. The function of the nucleolus is related to the synthesis of tRNA - takes approx 25\% of nucleus volume, and can be seen as a dark spot.":
            call correct

        "1. Protects DNA from external damage 2. The function of the nucleolus is related to the synthesis of rRNA - takes approx 25\% of nucleus volume, and can be seen as a dark spot.":
            call wrong

        "1. Compartmentalization of DNA allows you to create two distinct environments within the cell to separate transcription and translation 2. The function of the nucleolus is related to the synthesis of rRNA - takes approx 25\% of nucleus volume, and can be seen as a dark spot.":
            call wrong

    return

label question6:

    menu:

        p "Mitochondria What are the purposes of the two membranes in mitochondria (outer and inner)?"

        "Outer - contains the molecules and nz of e transport chain Inner - arranged into folds (christae), and contains the nz for ATP synthesis.":
            call correct

        "Outer - serves as barrier between the cytosol and inner environment of the mitochondrion Inner - arranged into folds (christae), and contains the molecules and nz of e transport chain.":
            call wrong

        "Outer - arranged into folds (christae), and contains the molecules and nz of e transport chain Inner - serves as barrier between the cytosol and inner environment of the mitochondrion.":
            call wrong

    return