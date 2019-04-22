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


if __name__ == '__main__':
    unittest.main(verbosity=2)
