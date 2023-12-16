from Day11_b import calculate_distances, create_coordinate_pairs, collect_galaxy_coordinates, parse
import unittest
from textwrap import dedent

sample1 = parse(dedent("""\
        ...#......
        .......#..
        #.........
        ..........
        ......#...
        .#........
        .........#
        ..........
        .......#..
        #...#....."""))

sample1 = parse(dedent("""\
        ...#......
        .......#..
        #.........
        ..........
        ......#...
        .#........
        .........#
        ..........
        .......#..
        #...#....."""))
           
class Test_figure_coming_directions_at_start(unittest.TestCase):
    def test_collect_galaxy_coordinates_factor_1(self):
        factor = 1
        expected_coordinates = [(0,3),(1,7),(2,0),(4,6),(5,1),(6,9), (8,7), (9,0), (9,4)]
        self.assertEqual(expected_coordinates, collect_galaxy_coordinates(sample1, factor))
        
    def test_collect_galaxy_coordinates_factor_2(self):
        factor = 2
        expected_coordinates = [(0,4),(1,9),(2,0),(5,8),(6,1),(7,12), (10,9), (11,0), (11,5)]
        self.assertEqual(expected_coordinates, collect_galaxy_coordinates(sample1, factor))
        
    def test_collect_galaxy_coordinates_factor_10(self):
        factor = 10
        expected_coordinates = [(0, 12), (1,25),(2,0),(13,24),(14,1),(15,36), (26,25), (27,0), (27,13)]
        self.assertEqual(expected_coordinates, collect_galaxy_coordinates(sample1, factor))
        
    def test_collect_galaxy_coordinates_factor_100(self):
        factor = 100
        expected_coordinates = [(0, 102), (1,205),(2,0),(103,204),(104,1),(105,306), (206,205), (207,0), (207,103)]
        self.assertEqual(expected_coordinates, collect_galaxy_coordinates(sample1, factor))
        
    def test_collect_galaxy_coordinates_factor_1000000(self):
        factor = 1_000_000
        expected_coordinates = [(0, 1000002), (1,2000005),(2,0),(1000003,2000004),(1000004,1),(1000005,3000006), (2000006,2000005), (2000007,0), (2000007,1000003)]
        self.assertEqual(expected_coordinates, collect_galaxy_coordinates(sample1, factor))
        
    def test_sample_puzzle_factor_2(self):
        factor = 2
        result = sum(calculate_distances(create_coordinate_pairs(collect_galaxy_coordinates(sample1, factor))))
        self.assertEqual(374, result)
        
    def test_sample_puzzle_factor_10(self):
        factor = 10
        result = sum(calculate_distances(create_coordinate_pairs(collect_galaxy_coordinates(sample1, factor))))
        self.assertEqual(1030, result)
        
    def test_sample_puzzle_factor_100(self):
        factor = 100
        result = sum(calculate_distances(create_coordinate_pairs(collect_galaxy_coordinates(sample1, factor))))
        self.assertEqual(8410, result)
unittest.main()
        