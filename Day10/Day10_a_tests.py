from Day10_a import figure_out_coming_directions_from_start
import unittest
from textwrap import dedent

grid = dedent("""\
           F-7
           | |
           L-J""").splitlines()
           
class Test_figure_coming_directions_at_start(unittest.TestCase):
    def test_00(self):
        self.assertEqual({'N', 'W'}, set(figure_out_coming_directions_from_start(grid, (0,0))))
        
    def test_01(self):
        self.assertEqual({'W', 'E'}, set(figure_out_coming_directions_from_start(grid, (0,1))))

    def test_02(self):
        self.assertEqual({'E', 'N'}, set(figure_out_coming_directions_from_start(grid, (0,2))))
    
    def test_10(self):
        self.assertEqual({'N', 'S'}, set(figure_out_coming_directions_from_start(grid, (1,0))))
    
    def test_12(self):
        self.assertEqual({'N', 'S'}, set(figure_out_coming_directions_from_start(grid, (1,2))))
    
    def test_20(self):
        self.assertEqual({'S', 'W'}, set(figure_out_coming_directions_from_start(grid, (2,0))))
    
    def test_21(self):
        self.assertEqual({'W', 'E'}, set(figure_out_coming_directions_from_start(grid, (2,1))))
    
    def test_22(self):
        self.assertEqual({'E', 'S'}, set(figure_out_coming_directions_from_start(grid, (2,2))))
           
unittest.main()
        