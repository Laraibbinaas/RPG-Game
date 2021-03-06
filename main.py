# Course: CS 30
# Period: 2
# Date created: 21/02/08
# Date last modified: 21/02/08
# Name: Laraib Bin Aas
# Description: Main code that runs the game
# Code adpated from https://github.com/kynite/FishingRPG

# Game breaks after moving out of map
# Could be solves with a visaul map
import world
from world import *
from player import Player
import locations as loc

print("You wake up after a long night and realize you are not at home")
print("You find yourseld in the middle of a random road with a letter")
print("The letter says that there is one exit and you must find it to escape")
print("You get ready to explore this land and try to escape")


def location():
    global world_map
    """Commands that allow for movement on the map"""
    # While loop for continous play
    while True:
        # Tells user to type q to go to the previous menu
        print("\ntype q to quit")
        print("Map is a 3x3 grid and you start in the bottom middle")
        print("If you leave the map it will stop working")
        print("North")
        print("West")
        print("East")
        print("South")
        # Asks for user input of what location they would like to go to
        user = input('Select a Movement: ')
        # Makes all user inputs lower cased to match if and elif statements
        user = user.lower()
        # Checks to see if user typed in movement command
        if user == 'north':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move north
                    if isinstance(object, Player):
                        # Checks to see if the Player is going to move into
                        # another object and runs something else
                        if isinstance(world.world_map[y - 1][x], cave):
                            loc.cave()
                        elif isinstance(world.world_map[y - 1][x], mountain):
                            loc.mountain()
                        elif isinstance(world.world_map[y - 1][x], jungle):
                            loc.jungle()
                        elif isinstance(world.world_map[y - 1][x], house):
                            loc.house()
                        elif isinstance(world.world_map[y - 1][x], end):
                            loc.end()
                        else:
                            # moves the player in north direction
                            world.world_map[y - 1][x] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        elif user == 'west':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move west
                    if isinstance(object, Player):
                        # Checks to see if the Player is going to move into
                        # another object and runs something else
                        if isinstance(world.world_map[y][x - 1], cave):
                            loc.cave()
                        elif isinstance(world.world_map[y][x - 1], mountain):
                            loc.mountain()
                        elif isinstance(world.world_map[y][x - 1], jungle):
                            loc.jungle()
                        elif isinstance(world.world_map[y][x - 1], house):
                            loc.house()
                        elif isinstance(world.world_map[y][x - 1], end):
                            loc.end()
                        else:
                            # moves the player west
                            world.world_map[y][x - 1] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        # Checks to see if user typed in movement command
        elif user == 'east':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move east
                    if isinstance(object, Player):
                        # Checks to see if the Player is going to move into
                        # another object and runs something else
                        if isinstance(world.world_map[y][x + 1], cave):
                            loc.cave()
                        elif isinstance(world.world_map[y][x + 1], mountain):
                            loc.mountain()
                        elif isinstance(world.world_map[y][x + 1], jungle):
                            loc.jungle()
                        elif isinstance(world.world_map[y][x + 1], house):
                            loc.house()
                        elif isinstance(world.world_map[y][x + 1], end):
                            loc.end()
                        else:
                            # moves the player east
                            world.world_map[y][x + 1] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        # Checks to see if user typed in movement command
        elif user == 'south':
            # Finds Player in the world_map
            for y, row in enumerate(world.world_map):
                for x, object in enumerate(row):
                    # if the object is a player move south
                    if isinstance(object, Player):
                        # Checks to see if the Player is going to move into
                        # another object and runs something else
                        if isinstance(world.world_map[y + 1][x], cave):
                            loc.cave()
                        elif isinstance(world.world_map[y + 1][x], mountain):
                            loc.mountain()
                        elif isinstance(world.world_map[y + 1][x], jungle):
                            loc.jungle()
                        elif isinstance(world.world_map[y + 1][x], house):
                            loc.house()
                        elif isinstance(world.world_map[y + 1][x], end):
                            loc.end()
                        else:
                            # moves the player south
                            world.world_map[y + 1][x] = object
                            # replaces tile with no value
                            world.world_map[y][x] = None
                            # reloads the location call to continue the map
                            location()
                            # returns the new y value/ player position
                            return
        elif user == 'q':
            break
        else:
            print('invalid option')

location()
