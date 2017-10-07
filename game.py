
name = input("What is your name?")
def letsgo(name):

    print(f"Hi {name} welcome to New York City? What do you want to do today?")
    print("Should we stay in Manhattan or explore Brooklyn today?")

    badchoice = True
    while badchoice:

        man_bq = input("You see a sign for the D train to Stillwell Ave and a 7 train to 42nd St Times Square. Where do you want to go? > ")

        man_bq = man_bq.upper()

        if man_bq in ["D TRAIN", "STILLWELL", "BROOKLYN"]:
            #print("Going to Brooklyn")
            badchoice = False
            brook()
        elif man_bq in ["TIMES SQUARE", "42ND ST", "MANHATTAN", "7 TRAIN"]:
            #print ("Staying in Manhattan")
            badchoice = False
            manhattan()
        else:
            print("I didn't understand your choice. Can you type Brooklyn or Manhattan? \n")

def brook():
    badchoice = True
    while badchoice:
        choice = input("Do you want to eat or play? >")

        choice = choice.upper()

        if choice in ["PLAY"]:
            badchoice = False
            play()
            #print("Lets PLAY")
        elif choice in ["EAT"]:
            badchoice = False
            eat()
            #print("LETS EAT")
        else:
            print("I didn't understand your choice. Can you type play or eat? \n")

def play():
    badchoice = True
    while badchoice:
        choice = input("Do you want to go to the beach? >")

        choice = choice.upper()

        if choice in ["YEAH", "YES", "YEA"]:
            badchoice = False
            beachyea()
            #print("Lets PLAY")
        elif choice in ["NO", "NAH"]:
            badchoice = False
            beachno()
            #print("LETS EAT")
        else:
            print("I didn't understand your choice. Can you type yes or no? \n")

def eat():
    badchoice = True
    while badchoice:
        choice = input("Do you want to eat hot dog or pizza? >")

        choice = choice.upper()

        if choice in ["HOT DOG," "HOTDOG"]:
            badchoice = False
            hotdog()
            #print("Lets PLAY")
        elif choice in ["PIZZA"]:
            badchoice = False
            pizza()
            #print("LETS EAT")
        else:
            print("I didn't understand your choice. Can you type hot dog or pizza? \n")

def beach():
    choice = input("The water looks freezing. Are you sure you want to swim?")
    choice = choice.upper()

    if choice in ["YES", "YEAH", "YEA"]:
        choice = False
        beachyea()
        #print("Lets PLAY")
    elif choice in ["NO", "NAH" "NO WAY"]:
        badchoice = False
        beachno()
        #print("LETS EAT")
    else:
        print("I didn't understand your choice. Can you type yes or no? \n")

def beachyea():
    badchoice = True
    while badchoice:

        train = input("Awesome the water is not that cold! I thought it was really fun. Show we take the N train or D train to go home?")
        train = train.upper()
        if train  in ["D", "N"]:

             badchoice = False
             print(f"On the {train}")
             gohome(name,train)
        else:
             print("Sorry I'm too tired. Type in D or N for us to leave. \n")

def beachno():
    badchoice = True
    while badchoice:

        train = input("Thank goodness. It looks so cold. Show we take the N train or D train to go home?")
        train = train.upper()
        if train  in ["D", "N"]:

             badchoice = False
             print(f"On the {train}")
             gohome(name,train)
        else:
             print("Sorry I'm too tired. Type in D or N for us to leave. \n")
def hotdog():
    badchoice = True
    while badchoice:

        train = input("We ate way too much. Should we take the N train or D train to go home?")
        train = train.upper()
        if train  in ["D", "N"]:

             badchoice = False
             print(f"On the {train}")
             gohome(name,train)
        else:
             print("Sorry I'm too tired. Type in D or N for us to leave. \n")

def pizza():
    badchoice = True
    while badchoice:
        train = input("That pizza was awesome! Should we take the N train or D train to go home?")
        train = train.upper()
        if train  in ["D", "N"]:

             badchoice = False
             print(f"On the {train}")
             gohome(name,train)
        else:
             print("Sorry I'm too tired. Type in D or N for us to leave. \n")


def gohome(name,train):
    print (f"Perfect {name}. Let's take {train}")

def manhattan():
    badchoice = True
    while badchoice:
        choice = input("Do you want to eat or play? >")

        choice = choice.upper()

        if choice in ["PLAY"]:
            badchoice = False
            play()
            #print("Lets PLAY")
        elif choice in ["EAT"]:
            badchoice = False
            eat()
            #print("LETS EAT")
        else:
            print("I didn't understand your choice. Can you type play or eat? \n")

def play():
    badchoice = True
    while badchoice:
        choice = input("Do you want to go watch a show? >")

        choice = choice.upper()

        if choice in ["YEAH", "YES", "YEA"]:
            badchoice = False
            showyea()
            #print("Lets PLAY")
        elif choice in ["NO", "NAH"]:
            badchoice = False
            showno()
            #print("LETS EAT")
        else:
            print("I didn't understand your choice. Can you type yes or no? \n")

def eat():
    badchoice = True
    while badchoice:
        choice = input("Do you want to eat pasta or sandwiches? >")

        choice = choice.upper()

        if choice in ["PASTA"]:
            badchoice = False
            pasta()
            #print("Lets PLAY")
        elif choice in ["SANDWICHES", "SANDWICH"]:
            badchoice = False
            sandwiches()
            #print("LETS EAT")
        else:
            print("I didn't understand your choice. Can you type pasta or sandwiches? \n")

def show():
    choice = input("Awesome. Let's watch the Lion King.")
    choice = choice.upper()

    if choice in ["YES", "YEAH", "YEA"]:
        choice = False
        showyea()
        #print("Lets PLAY")
    elif choice in ["NO", "NAH" "NO WAY"]:
        badchoice = False
        showno()
        #print("LETS EAT")
    else:
        print("I didn't understand your choice. Can you type yes or no? \n")

def showyea():
    badchoice = True
    while badchoice:

        train = input("Awesome that show was great. Show we take the N train or D train to go home?")
        train = train.upper()
        if train  in ["D", "N"]:

             badchoice = False
             print(f"On the {train}")
             gohome(name,train)
        else:
             print("Sorry I'm too tired. Type in D or N for us to leave. \n")

def showno():
    badchoice = True
    while badchoice:

        train = input("Thank goodness. I do not have enough money anyway. Show we take the N train or D train to go home?")
        train = train.upper()
        if train  in ["D", "N"]:

             badchoice = False
             print(f"On the {train}")
             gohome(name,train)
        else:
             print("Sorry I'm too tired. Type in D or N for us to leave. \n")
def pasta():
    badchoice = True
    while badchoice:

        train = input("We ate way too much. Should we take the N train or D train to go home?")
        train = train.upper()
        if train  in ["D", "N"]:

             badchoice = False
             print(f"On the {train}")
             gohome(name,train)
        else:
             print("Sorry I'm too tired. Type in D or N for us to leave. \n")

def sandwiches():
    badchoice = True
    while badchoice:
        train = input("That was so good! Should we take the N train or D train to go home?")
        train = train.upper()
        if train  in ["D", "N"]:

             badchoice = False
             print(f"On the {train}")
             gohome(name,train)
        else:
             print("Sorry I'm too tired. Type in D or N for us to leave. \n")

letsgo(name)
