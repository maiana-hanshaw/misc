### NAME:  tests_adventure_orig.py
### MODIFICATION HISTORY:  Written by Maiana Hanshaw for Python (08/08/2020);
### PURPOSE:  To create unit tests for the adventure.py game, for the NSIDC Software Developer Interview.

###############################################################################

import unittest
from adventure import config_df

commands = ["look", "help", "quit", "up", "down", "north", "south", "east", "west"]

#########################

class TestStringMethods(unittest.TestCase):
 
    # I *think* this works
    def test_yn(self):
        self.assertEqual("y", "y")
        self.assertEqual("n", "n")
        self.assertIsNotNone("")

    # I *think* this works
    def test_commands(self):
        for command in commands:
            self.assertEqual(command, command)
            self.assertIsNotNone(command)
   
    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them
    def test_roomid(self):
        values = config_df["room_id"].values
        for value in values:
            self.assertIsNotNone(value, "")
       
    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_description(self):        
        values = config_df["description"].values
        for value in values:
            self.assertIsNotNone(value, "")
            
    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_u(self):        
        values = config_df["u"].values
        for value in values:
            self.assertIsNotNone(value, "")

    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_u_roomid(self):        
        values = config_df["u_room_id"].values
        for value in values:
            self.assertIsNotNone(value, "")

    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_d(self):        
        values = config_df["d"].values
        for value in values:
            self.assertIsNotNone(value, "")

    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_d_roomid(self):        
        values = config_df["d_room_id"].values
        for value in values:
            self.assertIsNotNone(value, "")

    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_n(self):        
        values = config_df["n"].values
        for value in values:
            self.assertIsNotNone(value, "")

    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_n_roomid(self):        
        values = config_df["n_room_id"].values
        for value in values:
            self.assertIsNotNone(value, "")
            
    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_s(self):        
        values = config_df["s"].values
        for value in values:
            self.assertIsNotNone(value, "")
            
    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_s_roomid(self):        
        values = config_df["s_room_id"].values
        for value in values:
            self.assertIsNotNone(value, "")
            
    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_e(self):        
        values = config_df["e"].values
        for value in values:
            self.assertIsNotNone(value, "")
            
        # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_e_roomid(self):        
        values = config_df["e_room_id"].values
        for value in values:
            self.assertIsNotNone(value, "")
            
    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_w(self):        
        values = config_df["w"].values
        for value in values:
            self.assertIsNotNone(value, "")
            
    # I do NOT think that this works... I don't know why but even when blank it doesn't seem to find them   
    def test_w_roomid(self):        
        values = config_df["w_room_id"].values
        for value in values:
            self.assertIsNotNone(value, "")

#########################
    
if __name__ == '__main__':
    unittest.main()

###############################################################################