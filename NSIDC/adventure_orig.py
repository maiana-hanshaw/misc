### NAME:  adventure_orig.py
### MODIFICATION HISTORY:  Written by Maiana Hanshaw for Python (08/08/2020);
### PURPOSE:  To create a small game for the NSIDC Software Developer Interview.

###############################################################################

###### UPDATE THIS ######
input_config_file = "C:/Users/Maiana/hobbit.csv"
starting_room_id = 1
room_id = starting_room_id
#########################

import pandas as pd  # pandas library for dictionary and data frames

def get_config_file(file_in):    
    config = pd.read_csv(file_in, engine="python").to_dict(orient="list")
    config_df = pd.DataFrame.from_dict(config, orient='columns').sort_index()  # convert dictionary to a data frame with float numbers    
    return config_df

config_df = get_config_file(input_config_file)

#########################

def get_room_info(room, starting_room):    
    if room == starting_room:
        room_id = starting_room
        ind = config_df.index[config_df.room_id == starting_room][0]        
    if room != starting_room:
        room_id = room
        ind = config_df.index[config_df.room_id == room][0]      
    return room_id, ind

#########################
if __name__ == "__main__":
    
    name = ("\n\n" + "Welcome to Nano Adventure!"+ "\n\n" + "Type directions to move into different rooms to get through to the other side and find the lost treasure!" + "\n\n"
    + "The commands you can use are:" + "\n" + "look: show the description of the room" + "\n" + "north: attempt to move north" + "\n" + "south: attempt to move south" + "\n"
    + "east: attempt to move east" + "\n" + "west: attempt to move west" + "\n" + "up: attempt to move up" + "\n" + "down: attempt to move down" + "\n" + "quit: stop playing!"
    + "\n" + "help: show this list of commands" + "\n\n" + "Begin?")
    print(name)
    
    while True:
        try:
            letter = input("Please enter y/n\n")
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    room_id, ind = get_room_info(room_id, starting_room_id)
    if letter == "y":
        print("\n" + "Great! Let's begin!" + "\n\n" + "To start with, here is a list of rooms and their descriptions to let you know where you need to go:")
        
        room_dict = {}
        for i in range(len(config_df)):
            key = str(config_df["room_id"][i])
            value = config_df["description"][i]
            room_dict.update({key: value}) 
        for key, value in room_dict.items():
            print(key, ": ", value)
        print("\n" + "Which direction would you like to move?" + "\n" + "Hint: Type 'look' for a description of where you are, and for hints to door locations.")
    
    if letter == "n":
        letter = input("Quit (y/n)?\n")
        
        if letter == "n":
            print("\n" + "Great! Let's begin!" + "\n\n" + "To start with, here is a list of rooms and their descriptions to let you know where you need to go:")
            room_dict = {}
            for i in range(len(config_df)):
                key = str(config_df["room_id"][i])
                value = config_df["description"][i]
                room_dict.update({key: value}) 
            for key, value in room_dict.items():
                print(key, ": ", value)
            print("\n" + "Which direction would you like to move?" + "\n" + "Hint: Type 'look' for a description of where you are, and for hints to door locations.")
    
        if letter == "y":
            print("Thank you. Goodbye!")
            exit()

#########################

    command = []
    
    while command != "quit":
        
        command = input()
    
        if command == "quit":
            print("Thank you. Goodbye!")
            exit()
            
        if command == "help":
            print("\n" + "The commands you can use are:" + "\n" + "look: show the description of the room" + "\n" + "north: attempt to move north" + "\n" + "south: attempt to move south" + "\n"
            + "east: attempt to move east" + "\n" + "west: attempt to move west" + "\n" + "up: attempt to move up" + "\n" + "down: attempt to move down" + "\n" + "quit: stop playing!" + "\n")      
        
        if command == "look":
            room_id, ind = get_room_info(room_id, starting_room_id)
            print(config_df["description"][ind] + "\n" + "Door location hints:")
                   
            if config_df["u"][ind] == 1:
                print("- A cute Pixar movie.")
            if config_df["d"][ind] == 1:
                print("- Feeling blue :(")
            if config_df["n"][ind] == 1:
                print("- Polaris.")
            if config_df["s"][ind] == 1:
                print("- Where it is warmer :)")               
            if config_df["e"][ind] == 1:
                print("- The sun rises here.")
            if config_df["w"][ind] == 1:
                print("- Life is peaceful there.")          
            
        if command == "up":
            room_id, ind = get_room_info(room_id, starting_room_id)    
            if config_df["u"][ind] == 0:
                print("You cannot move up.")
            if config_df["u"][ind] == 1:
                room_id = config_df.u_room_id[ind]
                new_ind = config_df.index[config_df.room_id == room_id][0]
                print(config_df["description"][new_ind])
                 
        if command == "down":
            room_id, ind = get_room_info(room_id, starting_room_id)    
            if config_df["d"][ind] == 0:
                print("You cannot move down.")
            if config_df["d"][ind] == 1:
                room_id = config_df.d_room_id[ind]
                new_ind = config_df.index[config_df.room_id == room_id][0]
                print(config_df["description"][new_ind])
                
        if command == "north":
            room_id, ind = get_room_info(room_id, starting_room_id)    
            if config_df["n"][ind] == 0:
                print("You cannot move north.")
            if config_df["n"][ind] == 1:
                room_id = config_df.n_room_id[ind]
                new_ind = config_df.index[config_df.room_id == room_id][0]
                print(config_df["description"][new_ind])
                 
        if command == "south":
            room_id, ind = get_room_info(room_id, starting_room_id)    
            if config_df["s"][ind] == 0:
                print("You cannot move south.")
            if config_df["s"][ind] == 1:
                room_id = config_df.s_room_id[ind]
                new_ind = config_df.index[config_df.room_id == room_id][0]
                print(config_df["description"][new_ind])
                
        if command == "east":
            room_id, ind = get_room_info(room_id, starting_room_id)    
            if config_df["e"][ind] == 0:
                print("You cannot move east.")
            if config_df["e"][ind] == 1:
                room_id = config_df.e_room_id[ind]
                new_ind = config_df.index[config_df.room_id == room_id][0]
                print(config_df["description"][new_ind])
                 
        if command == "west":
            room_id, ind = get_room_info(room_id, starting_room_id)    
            if config_df["w"][ind] == 0:
                print("You cannot move west.")
            if config_df["w"][ind] == 1:
                room_id = config_df.w_room_id[ind]
                new_ind = config_df.index[config_df.room_id == room_id][0]
                print(config_df["description"][new_ind])

###############################################################################