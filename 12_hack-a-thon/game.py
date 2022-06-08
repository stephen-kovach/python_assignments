# we are importing the ninja and pirate files

from ninja import Ninja
from pirate import Pirate
import time
# import module for sleep function on line 26 file from python

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

# defining a class called game, game inherting classes ninja and pirate (parents)
class Game(Ninja, Pirate):

    # setting global attribute for the game class 
    current_tick = 0

    # contructor function (defaut)
    def __init__(self):
        # super().__init__(name)
        self.michelangelo = Ninja("Michelanglo") # storing an instance of ninja
        self.jack_sparrow = Pirate("Jack Sparrow")
        self.current_tick = 0


    def tick(self): # defining a function called tick
        time.sleep(.1)  # setting our 'tick' to .1 second, telling program to pause .1 sec
        self.current_tick += 1 # incrememting the current tick attribure to the current instance of the game class


# below code is our experience 

# class myThread(threading.Thread):
#     def __init__(self, thread_ID, name, counter):
#         threading.Thread.__init__(self)
#         self.thread_ID = thread_ID
#         self.name = name
#         self.counter = counter
    
#     def run(self):
#         print("Staring " + self.name)
#         threadLock.acquire()
#         count -= 1
        
# threadLock = threading.Lock()
# threads = []

# This is our menu, giving an option to stop and start the game

print("1) Start new game")
print("2) Exit game")

# option variable that will be input 1 or 2, determining the players choice to begin or end
option = input("Enter an option")

# condtitional that says what to do based on what the input is
if(option == "1"):
    new_game = Game()
elif(option == "2"):
    print("Goodbye")

# creating a while loop
while(new_game.michelangelo.health > 0 and new_game.jack_sparrow.health > 0):
    # print("1)attack")
    # action = input("Enter your action")
    if(new_game.current_tick == 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    elif(new_game.current_tick % new_game.michelangelo.speed == 0 and new_game.current_tick % new_game.jack_sparrow.speed == 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    elif(new_game.current_tick % new_game.michelangelo.speed == 0 and new_game.current_tick % new_game.jack_sparrow.speed != 0):
        new_game.michelangelo.attack(new_game.jack_sparrow)
        new_game.tick()
    elif(new_game.current_tick % new_game.jack_sparrow.speed == 0 and new_game.current_tick % new_game.michelangelo.speed != 0):
        new_game.jack_sparrow.attack(new_game.michelangelo)
        new_game.tick()
    else:
        new_game.tick()
    new_game.michelangelo.show_stats()
    new_game.jack_sparrow.show_stats()

# setting up another conditional checking who hits zero first 
if(new_game.michelangelo.health <= 0 and new_game.jack_sparrow.health > 0):
        print("Jack Sparrow is the winner.")
elif(new_game.jack_sparrow.health <= 0 and new_game.michelangelo.health > 0):
        print("Michaelangelo is the winner.")

# Our next step was to create interactivity with the player getting to choose different attacks, as is
    # this code predetermines that Michelangelo will hit zero before Jack Sparrow

print("1) Start new game")
print("2) Exit game")

# another chance to choose option variable that will be input 1 or 2, determining the players choice to begin or end
option = input("Enter an option")