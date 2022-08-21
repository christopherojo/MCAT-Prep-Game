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
    $ quiz_length = 20       # number of questions in one game
    $ q_to_ask = []         # list of questions to ask in one game

    # list of all possible questions
    # it consist of dictionaries, that describe each question:
    # key "question" has value of a question, key "category" makes sense for bot, key "answer" is a list of answers, that are lists [answer itself, right/wrong]
    # the order of this keys is not matter

    # $ question1 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    # $ question2 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    # $ question3 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    # $ question4 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    # $ question5 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    # $ question6 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    # $ question7 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    # $ question8 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    # $ question9 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    # $ question10 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}

    $ question1 = {"category": "Biology", "question": "1. Aprox # of cells in body 2. Ratio of bacterial to eukaryotic", "answer": [ ["37 trillion 10:1", "right"], ["28 billion 2 million:1", "wrong"], ["153 trillion 1:1", "wrong" ]]}
    $ question2 = {"category": "Biology", "question": "Which is the tenet that is CORRECT regarding cell theory?", "answer": [ ["Cells only make up eukaryotes ", "wrong"], ["There are different forms of storage for genetic information that gets passed onto future cells", "wrong"], ["1. All living things are composed of cells 2. The cell is the basic functional unit of life 3. Cells arise only from preexisting cells 4. Cells carry genetic info (DNA), passed onto daughter cells", "right"] ]}
    $ question3 = {"category": "Biology", "question": "Membrane Bound Organelles Properties RECALL: - phospholipid bilayer is hydro______ outside and hydro_____ inside - Purpose of asymmetrical? - What is the purpose of the cytosol", "answer": [ ["1. hydrophilic outside, hydrophobic inside 2. To keep hydrophilic molecules inside the cell and hydrophobic molecules out 3. Structural component of the cells", "wrong"], ["1. hydrophilic outside, hydrophobic inside 2. So it can interact with whatever with greater affinity and selectivity 3. Allows for diffusion of molecules throughout the cell", "right"], [". 1. hydrophobic outside, hydrophilic inside 2. So it can interact with whatever with greater affinity and selectivity 3. Structural component of the cells", "wrong"] ]}
    $ question4 = {"category": "Biology", "question": "Nucleus Properties - What is a main purpose of the compartmentalization of DNA in the nucleus - Explain the function of the nucleolus, how can you identify it?", "answer": [ ["1. Protects DNA from external damage 2. The function of the nucleolus is related to the synthesis of tRNA - takes approx 25% of nucleus volume, and can be seen as a dark spot", "wrong"], ["1. Compartmentalization of DNA allows you to create two distinct environments within the cell to separate transcription and translation 2. The function of the nucleolus is related to the synthesis of rRNA - takes approx 25% of nucleus volume, and can be seen as a dark spot", "right"], ["1. Protects DNA from external damage 2. The function of the nucleolus is related to the synthesis of rRNA - takes approx 25% of nucleus volume, and can be seen as a dark spot", "wrong"] ]}
    $ question5 = {"category": "Biology", "question": "Mitochondria What are the purposes of the two membranes in mitochondria (outer and inner)", "answer": [ ["Outer - contains the molecules and nz of e transport chain Inner - arranged into folds (christae), and contains the nz for ATP synthesis", "wrong"], ["Outer - arranged into folds (christae), and contains the molecules and nz of e transport chain Inner - serves as barrier between the cytosol and inner environment of the mitochondrion", "wrong"], ["Outer - serves as barrier between the cytosol and inner environment of the mitochondrion Inner - arranged into folds (christae), and contains the molecules and nz of e transport chain", "right" ]]}
    $ question6 = {"category": "Biology", "question": "Mitochondria Explain the role of christae", "answer": [ ["Christae: contains the molecules and nz of the electron transport chain - increase the surface area of inner membrane - place where proton motive force is established for ATP synthase", "right"], ["contains the molecules and nz of the electron transport chain - increase the volume of the matrix - place where proton motive force is established for ATP synthase", "wrong"], ["contains ATP synthase - increase the volume of the matrix - place where proton motive force is established for ATP synthase", "wrong" ]]}
    $ question7 = {"category": "Biology", "question": "Mitochondria How does the mitochondria replicate for cell replication?", "answer": [ ["BINARY FISSION semi autonomous", "right"], ["Produced by budding off from the ER", "wrong"], ["Undergoes mitosis autonomously", "wrong" ]]}
    $ question8 = {"category": "Biology", "question": "Explain cytoplasmic/extranuclear inheritance - PROVIDE EXAMPLES", "answer": [ ["transmission of genetic material independent of the nucleus - mitochondria, chloroplast...etc", "right"], ["Inheritance of genetic information not related to changes in nucleotides (aka epigenetic changes) – e.g., histone acetylation, DNA methylation", "wrong"], ["Transmission of RNA found in the cytoplasm – e.g., mRNA, tRNA, siRNA", "wrong" ]]}
    $ question9 = {"category": "Biology", "question": "Mitochondria Explain how the mitochondria is associated with apoptosis", "answer": [ ["Can turn off ATP production to shut down the cell", "wrong"], ["Release of nz from the electron transport chain can trigger apoptosis", "right"], ["Mitochondrial DNA contains genes for apoptosis", "wrong" ]]}
    $ question10 = {"category": "Biology", "question": "Lysosomes What type of nz are contained within them? What would happen if they were released?", "answer": [ ["the Nz are hydrolytic nz. Release of these nz would trigger autolysis directly.", "right"], ["the Nz are kinases and phosphatases. Release of these nz would trigger autolysis indirectly.", "wrong"], ["the Nz are hydrolytic nz. Release of these nz would activate other nz that would cause autolysis.", "wrong" ]]}
    
    $ question11 = {"category": "Biology", "question": "ER Explain the difference in function between the RER and the SER", "answer": [ ["RER - studded with ribosomes, which permit the translation of proteins destined for secretion diretly into its lumen ER - lacks ribosomes and is utilized primarily for lipid synthesis. Also transports proteins from RER to golgi", "right"], ["RER - studded with ribosomes; anchoring allows for more efficient translation into the cytoplasm SER - lacks ribosomes and is utilized primarily for lipid synthesis. Also transports proteins from RER to golgi", "wrong"], ["RER - studded with ribosomes, which permit the translation of proteins destined for the mitochondria SER - lacks ribosomes and is utilized primarily for the synthesis of cytoplasmic proteins. Also transports proteins from SER to golgi", "wrong" ]]}
    $ question12 = {"category": "Biology", "question": "Golgi apparatus What are some of the destinations past the golgi (3)? What happens to products WITHIN the golgi?", "answer": [ ["lysosome, plasma membrane, exocytosis addition of additional groups, introduction of signal sequences...etc", "right"], ["lysosome, cytoplasm, mitochondria; first glycosylation, addition of additional groups...etc", "wrong"], ["cytoplasm, plasma membrane, exocytosis addition of additional groups, introduction of signal sequences...etc", "wrong" ]]}
    $ question13 = {"category": "Biology", "question": "Peroxisomes What is the main thing that peroxisomes contain? One of the primary functions of peroxisomes is the breakdown of ___________ via ________.", "answer": [ ["hydrogen peroxide, breakdown of long chain fatty acids due to beta-oxidation", "right"], ["ammonium peroxide; breakdown of steroids due to oxidation", "wrong"], ["lysozymes; breakdown of reactive species due to beta-oxidation", "wrong" ]]}
    $ question14 = {"category": "Biology", "question": "Cytoskeleton What are the three types of cytoskeleton", "answer": [ ["microfilaments, intermediate filaments, and microtubules", "right"], ["intermediate filaments, intermediate tubules, and microtubules", "wrong"], ["macrotubules, intermediate tubules, and microtubules", "wrong" ]]}
    $ question15 = {"category": "Biology", "question": "Cytoskeleton - Microfilaments What are they made of What do they interact with What do they play a role in (explain what cleavage furrow is)", "answer": [ ["1. Made up for solid polymerized actin strands 2. Use ATP to generate force by interacting with myosin 3. Plays a role in cytokinesis", "right"], ["1. Made up for solid polymerized actin strands 2. Use GTP to generate force by interacting with kinesin 3. Plays a role in cytokinesis", "wrong"], ["1. Made up for solid polymerized tubulin strands 2. Use GTP to generate force by interacting with kinesin 3. Plays a role in cell transport", "wrong" ]]}
    $ question16 = {"category": "Biology", "question": "Cytokinesis - Microtubules What are they made of? What are the motor proteins that they interact with (2) What structures are they associated with (how)?", "answer": [ ["1. Hollow polymers of tubulin proteins 2. They interact with 2 types of motor proteins (kinesin + denein) 3. They make up apart of cilia and flagella (9+2 structure for cilia) - they also make up centrioles and kinetochores", "right"], ["1. Hollow polymers of tubulin proteins 2. They interact with myosin 3. They make up apart of cilia and flagella (9+2 structure for cilia) - they also make up centrioles and kinetochores", "wrong"], ["1. Hollow polymers of tubulin proteins 2. They interact with myosin 3. They make up apart of cilia and flagella (9+2 structure for cilia) and create the cleavage furrow in cytokinesis", "wrong" ]]}
    $ question17 = {"category": "Biology", "question": "Intermediate Filaments What are the four proteins that are classified in this group", "answer": [ ["Keratin, desmin, vimentin, lamins", "right"], ["Keratin, desmin, vimentin, laminins", "wrong"], ["Adherens, desmin, integrin, laminins", "wrong" ]]}
    $ question18 = {"category": "Biology", "question": "Intermediate Filaments What is the main function of intermediate filaments", "answer": [ ["involved with cell cell adhesion, maintenance of the overall integrity of the cytoskeleton - increases structural rigidity - anchoring organelles", "right"], ["Cellular transport, maintenance of the overall integrity of the cytoskeleton - increases structural rigidity - anchoring organelles", "wrong"], ["involved with cell cell adhesion, make up cilia and flagella", "wrong" ]]}
    $ question19 = {"category": "Biology", "question": "What are the four types of tissues", "answer": [ ["Connective, Epithelial, Muscle, Nervous", "right"], ["Bone, Blood, Muscle, Nervous", "wrong"], ["Connective, Structural, Endothelial, Nervous", "wrong" ]]}
    $ question20 = {"category": "Biology", "question": "Epithelial Tissue What is the underlying layer of connective tissue called?", "answer": [ ["Basement Membrane", "right"], ["Endothelium", "wrong"], ["Base membrane", "wrong" ]]}
   
    $ question21 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    $ question22 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    $ question23 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    $ question24 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    $ question25 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    $ question26 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    $ question27 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    $ question28 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    $ question29 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}
    $ question30 = {"category": "Biology", "question": "", "answer": [ ["", "right"], ["", "wrong"], ["", "wrong" ]]}


    $ q_list = [question1, question2, question3,question4,question5,question6,question7,question8,question9,question10,question11,question12,question13,question14,question15,question16,question17,question18,question9,question20]

    # let's choose some questions to play with
    # while len(q_to_ask) < quiz_length:        # will work until we'll get enough questions for quiz
    #     $ a = renpy.random.choice(q_list)    # randomly pick a question from a list of all questions
    #     if a not in q_to_ask:                 # this question will be added only if we don't have it yet
    #         $ q_to_ask.append (a)

    # for x in q_list:
    #     $ q_to_ask.append (a)


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
    $ a = renpy.random.choice (q_list)      # randomly pick the question from a list
    $ q_list.remove (a)                     # remove it from list to not to ask it twice

    $ b = shuffle_answers (a["answer"])        # let's shuffle answers
            
    # ugly part... next variables are necessary to fill menu
    $ question = a["question"]
    $ category = a["category"]
    $ answ_0 = b[0][0]
    $ answ_1 = b[1][0]
    $ answ_2 = b[2][0]
    # $ answ_3 = b[3][0]
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
        # "[answ_3]":
        #     if b[3][1] == "right":
        #         call correct
        #     else:
        #         call wrong
    
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