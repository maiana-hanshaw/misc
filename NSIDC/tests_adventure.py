<<<<<<< HEAD
### NAME:  tests_adventure.py
### MODIFICATION HISTORY:  Written by Maiana Hanshaw for Python (08/08/2020);
###                        Updated on 08/10/20 with help from Michael Brandt and Hannah Wilcox
### PURPOSE:  To create unit tests for the adventure.py game, for the NSIDC Software Developer Interview.

###############################################################################

import unittest
from adventure import move_direction

#########################

class TestMoveDirection(unittest.TestCase):
    
    def test_movedirection_newroom(self):
        room, ind = move_direction(1, "west")
        self.assertEqual(room, 2)
        self.assertEqual(ind, 1)
    
    def test_movedirection_sameroom(self):
        room, ind = move_direction(1, "up")
        self.assertEqual(room, 1)
        self.assertEqual(ind, 0)    
    
#########################
    
if __name__ == '__main__':
    unittest.main()

=======
### NAME:  tests_adventure.py
### MODIFICATION HISTORY:  Written by Maiana Hanshaw for Python (08/08/2020);
###                        Updated on 08/10/20 with help from Michael Brandt and Hannah Wilcox
### PURPOSE:  To create unit tests for the adventure.py game, for the NSIDC Software Developer Interview.

###############################################################################

import unittest
from adventure import move_direction

#########################

class TestMoveDirection(unittest.TestCase):
    
    def test_movedirection_newroom(self):
        room, ind = move_direction(1, "west")
        self.assertEqual(room, 2)
        self.assertEqual(ind, 1)
    
    def test_movedirection_sameroom(self):
        room, ind = move_direction(1, "up")
        self.assertEqual(room, 1)
        self.assertEqual(ind, 0)    
    
#########################
    
if __name__ == '__main__':
    unittest.main()

>>>>>>> 6ba5dcc7f001b2a7f0a8b47d70050a1f55bdbe8d
###############################################################################