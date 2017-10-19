from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is yet not configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        #print(f"Scene Map {self.scene_map}")

    def play(self):
        current_scene = self.scene_map.opening_scene()
        #print(f"This is the current scene {self.current_scene}")
        last_scene = self.scene_map.next_scene('Winner')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Gameover(Scene):
    loser = [
    "Sorry that was not the right choice",
    "Better luck next time",
    "You snooze you lose",
    "Whoops. Try again",
    "The timing is not right"
    ]

    def enter(self):
        print(Gameover.loser[randint(0, len(self.loser)-1)])
        exit(1)

class Bryant_park(Scene):

    def enter(self):
        print("Welcome to New York City. You are currently at Bryant Park. Let's explore. Do you want to take a train, taxi, or walk around the city?")

        action = input('> ').lower()
        if action == "train":
            print("Ok let's take the train to Central Park")
            return 'Central Park'
        elif action == "taxi":
            print("Sorry no money.")
            return 'Gameover'
        elif action == "walk":
            print("Too dangerous to walk. You almost got hit by a car!")
            return 'Gameover'
        else:
            print("Choose train, taxi, or walk")
            return 'Bryant Park'#remember to d
class Central_park(Scene):


    def enter(self):
        print("It's such a lovely day in Central Park. Walking around and everything is nice and green. Oh no, a homeless man just asked me for money. What should I do?")
        action = input('> ').lower()


        if action == "give money":
            print("Ok here is $5. I am leaving New York City now.")
            return 'Gameover'
        elif action == "call police":
            print("OMG 911!! SOS means someone help me! Why is the police taking so long to answer?! I am leaving New York City now after this.")
            return 'Gameover'
        elif action == "run":
            print("I am running for dear life from this homeless man! Look a museum is right ahead. I'm going to run inside.")
            return 'Met'
        else:
            print("Choose run, give money, or call police")
            return 'Central Park'#
class Met(Scene):


    def enter(self):
        print("I am so stressed from running away from that homeless man. I cannot believe I just experienced that. Thank goodness the Met Museum has some alcohol, so after two beers, I am so much better. Should I check out some Egyptian art? Or maybe I should try running away from this bar bill. Unless I want to just drink the night away and fall asleep.")
        action = input('> ').lower()


        if action == "check out egyptian art":
            print("I have always wanted to see some mummies.")
            return 'Egyptiangallery'
        elif action == "skip on bar bill and run":
            print("Ugh I deserve to run away from this bill. I had such a horrible day.")
            return 'Gameover'
        elif action == "fall asleep":
            print("Why bother even checking out this museum? I only came here to runaway from this homeless man. I might as well fall asleep and just drink some more. ZzZZzz")
            return 'Gameover'
        else:
            print("Choose Egyptiangallery, skip on bar bill and run, or fall asleep.")
            return 'Met'

class Egyptiangallery(Scene):


    def enter(self):
        print("Wow I just found a pen and I'm in the Egyptian Gallery. There are so many great artifacts here. What should I do with this pen? Should I graffiti a statue? Should I steal the statue? Or leave with the pen, since I'm so tired?")
        action = input('> ').lower()


        if action == "steal":
            print("This statue is mine!! Hahahhaha!")
            return 'Winner'
        elif action == "graffiti":
            print("I have always wanted to be mischievious. Let's make my mark here.")
            return 'Gameover'
        elif action == "leave":
            print("I am so tired. I am so happy to leave.")
            return 'Gameover'
        else:
            print("Choose steal, graffiti, or leave.")
            return 'Egyptiangallery'


class Winner(Scene):

    def enter(self):
        print("I got away with it! I have a statue now!!")
        return 'Winner'

class Map(object):
    scenes = {
    'Bryant Park': Bryant_park(),
    'Central Park': Central_park(),
    'Met': Met(),
    "Egyptiangallery": Egyptiangallery(),
    "Winner": Winner(),
    "Gameover": Gameover()

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        #print(f"this is the next_scene {self.scene_name}")

        val = Map.scenes.get(scene_name)
        #print(f"this is val now {val}")
        return val
    def opening_scene(self):
        #print(self.next_scene(self.start_scene))
        return self.next_scene(self.start_scene)

a_map = Map('Bryant Park')
a_game = Engine(a_map)
#print(f"here is a_map {a_map} and here is {a_game}" )
a_game.play()
