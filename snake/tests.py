import unittest
import curses
from snake import sn

class TestSnake(unittest.TestCase):

    def setUp(self):
        self.body = ([10, 10], [10, 9], [10, 8])
        self.direction = curses.KEY_RIGHT
        self.eaten_food = []

    def test_set_direction(self):
        '''Testing add menthod'''
        sn.set_direction(self, curses.KEY_UP)

        self.assertEqual(sn.direction,curses.KEY_UP)

     def test_move(self):
        '''Testing add menthod'''
        field = Field (20, 20, sn)
        sn.move(self, field)
        self.assertEqual(sn.body[0],[9,10])

if __name__ == '__main__':
    unittest.main(verbosity=2)
