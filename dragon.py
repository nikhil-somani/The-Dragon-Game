# here is the function showing the goal and move command for the game

#defined variables


class Dragon(object):
    
    def __init__(self):
        global current
        global itemSet
        global room
        global direction
        direction = dict()
        current = "Great Hall"
        room = list()
        itemSet = set()
        room = {
        'Great Hall' : {'South': 'Living Room', 'North': 'Garden', 'East': 'Kitchen', 'West': 'Attic'},
        'Garden' : {'South': 'Great Hall','East': 'Work-out Room', 'item':'Rock'},
        'Work-out Room' : {'West': 'Garden', 'item':'Mace'},
        'Attic' : {'East': 'Great Hall', 'item': 'Knife'},
        'Living Room' : {'North': 'Great Hall', 'East': 'Office', 'item': 'Flash Light'},
        'Office' : {'West': 'Living Room', 'item': 'Gun'},
        'Kitchen' : {'North': 'Basement', 'West': 'Great Hall', 'item': 'Water'},
        'Basement' : {'South': 'Kitchen'}
    }
        
        

    def show_instructions(self):
        #print main menu and commands
        print("Welcome to Dragon World, either win or lose!, Dragon is waiting, here are the moves command \n")
        print("Collect 6 items to win the game or be eaten by the dragon \n")
        print("Move command: South, North, West, East \n")
        print("Add to Inventory: get 'item name' \n")

    def show_current_status(self):
        #print Current Status of the user
        status = "\nYou are in the {}"
        print(status.format(current))
        
    def item_founder(self):
        if "item" in direction.keys():
            collect = direction["item"]
            result = "Yippee I found {} for you \n"
            print(result.format(collect))
            itemSet.add(collect)
            print("Collecting Item...... \n")
        

    def movement(self, move):
        #accept user movement and perform required actions based on it
        global current
        global direction
        direction = room[current]
        if move in direction.keys():
            current = direction[move]    
            direction = room[current]        
        else:
            print("Sorry!! There is no possible route to", move, "from", current)
    
    def show_items(self):
        #it shows the item collected till now
        if itemSet:
            print("You have following item till now:")
            print(itemSet)

#In this solution, the player's status would be shown in a separate function.
#You may organize your functions differently

def main():
   
    #dictionary linking to room to other rooms
    # and linking one item for each room except the start room, (great hall) and the room containing the monster
    dragon = Dragon()
    
    dragon.show_instructions()
    
    dragon.show_current_status()
    
    while len(itemSet) < 6:
        
        move = input("\nEnter Next Move (South, North, East, West) \n")
        if move == "South" or "North" or "East" or "West":
            dragon.movement(move) 

            if current == "Basement":
                print("Oh No!!! MOnster Caught you! \n")
                print("GAME OVER \n")
                break
            else: 
                dragon.show_current_status()
                dragon.item_founder()
                dragon.show_items()
        else:
            print("Invalid Command Entered \n")
    print("Congratulations !!!!! You have won the Game")

if __name__ == "__main__":
    main()