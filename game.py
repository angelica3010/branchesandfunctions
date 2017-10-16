import time

name = input("What is your name? > ")
name = name.capitalize()

def letsgo(name):
    time.sleep(1.5)
    print(f"\"Hi {name}, welcome to New York City.  What do you want to do today?\"")
    time.sleep(1.5)
    print("You see a sign for the D train to Stillwell Ave and a 7 train to 42nd St Times Square.")
    time.sleep(1.5)

    badchoice = True
    while badchoice:
        choice = input("\"Should we stay in Manhattan or explore Brooklyn today?\" > ")
        choice = normalizer(choice)
        #print(choice)

        if choice in ["D TRAIN", "D", "STILLWELL", "BROOKLYN"]:
            #print("Going to Brooklyn")
            badchoice = False
            time.sleep(1.5)
            brook()
        elif choice in ["TIMES SQUARE", "42ND", "MANHATTAN", "7", "7 TRAIN"]:
            #print ("Staying in Manhattan")
            badchoice = False
            time.sleep(1.5)
            manhattan()
        else:
            print("I didn't understand your choice. Can you type Brooklyn or Manhattan? \n")


def normalizer(inp_txt):
    return inp_txt.upper()


def brook():
    badchoice = True
    while badchoice:
        choice = input("\"Alright, here we are in the 'in'-famous Coney Island.\"\nYou look around and see Nathan's, the amusement park, and the beach.\n\"Do you want to eat or play?\" > ")
        choice = normalizer(choice)

        if choice in ["PLAY"]:
            badchoice = False
            time.sleep(1.5)
            play_bk()
            #print("Lets PLAY")
        elif choice in ["EAT"]:
            badchoice = False
            time.sleep(1.5)
            eat_bk()
            #print("LETS EAT")
        else:
            print("\"I didn't understand your choice.  Did you say 'play' or 'eat?'\"\n")


def play_bk():
    badchoice = True
    while badchoice:
        choice = input("\"Great.  I wanted to play too!  I'm not sure where to begin!  Do you want to go to the beach?\" > ")
        choice = normalizer(choice)

        if choice in ["YEAH", "YES", "YEA", 'SURE', 'YEP']:
            badchoice = False
            time.sleep(1.5)
            beach()
            #print("Lets PLAY")
        elif choice in ["NO", "NAH", 'NOPE', 'NO WAY']:
            badchoice = False
            time.sleep(1.5)
            print('"Alright, I\'m getting kinda hungry anyway, let\'s eat instead."')
            time.sleep(1.5)
            eat_bk()
            #print("LETS EAT")
        else:
            print("\"I didn't understand your choice.  Did you say 'yes' or 'no?'\"\n")


def eat_bk():
    badchoice = True
    while badchoice:
        choice = input("Do you want to eat hotdog or pizza? > ")
        choice = normalizer(choice)

        if choice in ["HOT", "DOG", "HOTDOG"]:
            badchoice = False
            time.sleep(1.5)
            hotdog()
            #print("Lets PLAY")
        elif choice in ["PIZZA"]:
            badchoice = False
            time.sleep(1.5)
            pizza()
            #print("LETS EAT")
        else:
            print("\"I didn't understand your choice.  Did you say 'hotdog' or 'pizza?'\"\n")


def beach():
    print("\"Sure, let's take a walk on the boardwalk to find a nice spot on the beach.\"")
    time.sleep(1.5)
    choice = input("The water looks freezing. Are you sure you want to swim?")
    choice = normalizer(choice)

    if choice in ["YES", "YEAH", "YEA"]:
        choice = False
        time.sleep(1.5)
        swim_yea()
        #print("Lets PLAY")
    elif choice in ["NO", "NAH" "NO WAY"]:
        badchoice = False
        time.sleep(1.5)
        swim_no()
        #print("LETS EAT")
    else:
        ("\"I didn't understand your choice.  Did you say 'yes' or 'no?'\"\n")


def swim_yea():
    badchoice = True
    while badchoice:
        choice = input("\"Awesome the water is not that cold! I thought it was really fun. Show we take the N train or D train to go home?\" > ")
        choice = normalizer(choice)

        if choice in ["D", "N"]:
             badchoice = False
             time.sleep(1.5)
             print(f"Great, let's jump on the {choice}!\"")
             gohome(name,choice)
        else:
             print("\"Sorry I'm too tired. Say 'D' or 'N' for us to leave.\" \n")


def swim_no():
    badchoice = True
    while badchoice:
        choice = input("\"Thank goodness you said no to swimming.  It looks sooooooo cold.\nWell, we got in some nice sun time at the shore.  Shall we take the N train or D train to go home?\" > ")
        choice = normalizer(choice)

        if choice in ["D", "N"]:
             badchoice = False
             print(f"On the {choice}")
             time.sleep(1.5)
             gohome(name, choice)
        else:
             print("\"Sorry, I'm too tired. Say 'D' or 'N' for us to leave.\" \n")


def hotdog():
    badchoice = True
    while badchoice:
        choice = input("\"Those natural casing hotdogs at Nathans were the real deal!  Great suggestion!  But, we ate way too much. Should we take the N train or D train to go home?\" > ")
        choice = normalizer(choice)

        if choice in ["D", "N"]:
             badchoice = False
             time.sleep(1.5)
             print(f"On the {choice}")
             gohome(name, choice)
        else:
             print("\"Sorry, I'm too tired. Say 'D' or 'N' for us to leave.\" \n")


def pizza():
    badchoice = True
    while badchoice:
        choice = input("\"Whoa, Grimaldi's pizza was awesome!  The cheese was fresh mozz!  The crust had a delicate crisp to it.  We gotta come back some day!\nShould we take the N train or D train to go home?\" > ")
        choice = normalizer(choice)

        if choice in ["D", "N"]:
             badchoice = False
             time.sleep(1.5)
             print(f"On the {choice}")
             gohome(name, choice)
        else:
             print("\"Sorry, I'm too tired. Say 'D' or 'N' for us to leave.\" \n")


def gohome(name, train):
    print(f"\"Perfect, {name}. This {train} train will get us back in no time.\"")
    print("\"What an end to another Tuesday!\"")


def manhattan():
    badchoice = True
    while badchoice:
        choice = input("\"YES.  Manhattan island.  Oh what?  You didn't know it's an island?  It sure is.\nMost people mistake Manhattan for NYC but, in reality, it's just a small part of NYC.\nSo, how now?  Do you want to eat or play?\" > ")
        choice = normalizer(choice)

        if choice in ["PLAY"]:
            badchoice = False
            time.sleep(1.5)
            play_man()
            #print("Lets PLAY")
        elif choice in ["EAT"]:
            badchoice = False
            time.sleep(1.5)
            eat_man()
            #print("LETS EAT")
        else:
            print("\"I didn't understand your choice.  Did you say 'eat' or 'play?'\"\n")


def play_man():
    badchoice = True
    while badchoice:
        choice = input("\"Great, let's do it up, GIRL!  Hows about we catch a show?\" > ")
        choice = normalizer(choice)

        if choice in ["YEAH", "YES", "YEA"]:
            badchoice = False
            time.sleep(1.5)
            show_yea()
            #print("Lets PLAY")
        elif choice in ["NO", "NAH"]:
            badchoice = False
            time.sleep(1.5)
            show_no()
            #print("LETS EAT")
        else:
            print("\"I didn't understand your choice.  Did you say 'yes' or 'no?'\"\n")


def eat_man():
    badchoice = True
    while badchoice:
        choice = input("\"That's a good idea, I haven't eaten in a minute.  I'm famished.  Do you want to grab some pasta or sandwiches?\" > ")
        choice = normalizer(choice)

        if choice in ["PASTA"]:
            badchoice = False
            time.sleep(1.5)
            pasta()
            #print("Lets PLAY")
        elif choice in ["SANDWICHES", "SANDWICH"]:
            badchoice = False
            time.sleep(1.5)
            sandwiches()
            #print("LETS EAT")
        else:
            print("\"I didn't understand your choice.  Did you say 'pasta' or 'sandwiches?'\"\n")


def show():
    badchoice = True
    while badchoice:
        choice = input("\"Real bold choices you're making today.  Awesome. Let's watch the Lion King?\" > ")
        choice = normalizer(choice)

        if choice in ["YES", "YEAH", "YEA"]:
            choice = False
            time.sleep(1.5)
            show_yea()
            #print("Lets PLAY")
        elif choice in ["NO", "NAH" "NO WAY"]:
            badchoice = False
            time.sleep(1.5)
            show_no()
            #print("LETS EAT")
        else:
            print("\"I didn't understand your choice.  Did you say 'yes' or 'no?'\"\n")


def show_yea():
    badchoice = True
    while badchoice:
        choice = input("\"Awesome, that show was great. I almost thought that dude was gonna get eaten by the lion!  But he didn't and then he became a king!  What a great day!  Should we take the N train or D train to go home?\" > ")
        choice = normalizer(choice)

        if choice in ["D", "N"]:
             badchoice = False
             print(f"On the {choice}")
             time.sleep(1.5)
             gohome(name, choice)
        else:
             print("\"Sorry, I'm too tired. Say 'D' or 'N' for us to leave.\" \n")


def show_no():
    badchoice = True
    while badchoice:
        choice = input("\"Thank goodness.  I do not have enough money anyway.  This freakin town is mad $$$$!  Should we take the N train or D train to go home?\" > ")
        choice = normalizer(choice)

        if choice in ["D", "N"]:
             badchoice = False
             print(f"On the {choice}")
             time.sleep(1.5)
             gohome(name, choice)
        else:
             print("\"Sorry, I'm too tired. Say 'D' or 'N' for us to leave.\" \n")


def pasta():
    badchoice = True
    while badchoice:
        choice = input("\"Holy cow, that pasta was amazing!  I didn't care so much for the snails though.  You scarfed everything down like it was your last day!\nI think we ate way too much.\nShould we take the N train or D train to go home?\" > ")
        choice = normalizer(choice)

        if choice in ["D", "N"]:
             badchoice = False
             print(f"On the {choice}")
             time.sleep(1.5)
             gohome(name, choice)
        else:
             print("\"Sorry, I'm too tired. Say 'D' or 'N' for us to leave.\" \n")


def sandwiches():
    badchoice = True
    while badchoice:
        choice = input("\"That pastrami was soooooooo good!  I'm glad I ordered some to go too.  I still can't believe you ate the whole sandwich by yourself!  That was as big as your face!  Should we take the N train or D train to go home?\" > ")
        choice = normalizer(choice)

        if choice in ["D", "N"]:
             badchoice = False
             print(f"On the {train}")
             time.sleep(1.5)
             gohome(name, choice)
        else:
             print("\"Sorry, I'm too tired. Say 'D' or 'N' for us to leave.\" \n")

letsgo(name)
