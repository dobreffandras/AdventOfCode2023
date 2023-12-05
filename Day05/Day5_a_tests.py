from Day5_a import Mapper
import unittest

class TestMapper(unittest.TestCase):
    def test_maps_seed_smaller_than_mapper(self):
        #  97 ->  97 (default) *
        #  ---------
        #  98 -> 102
        #  99 -> 103
        # 100 -> 104
        #     .
        #     .
        # 107 -> 113
        
        seed = 98
        source = 98
        destination = 102
        range_length = 10
        expected = 102
        
        mapper = Mapper([(destination, source, range_length)])
        
        self.assertEqual(expected, mapper.map(seed)) 
        
    def test_maps_seed_with_mapper_at_start(self):
        #  98 -> 102 *
        #  99 -> 103
        # 100 -> 104
        #     .
        #     .
        # 107 -> 113
        
        seed = 98
        source = 98
        destination = 102
        range_length = 10
        expected = 102
        
        mapper = Mapper([(destination, source, range_length)])
        
        self.assertEqual(expected, mapper.map(seed)) 
        


    def test_maps_seed_with_mapper_in_the_middle(self):
        #  98 -> 102
        #  99 -> 103
        # 100 -> 104 *
        #     .
        #     .
        # 107 -> 113
        
        seed = 100
        source = 98
        destination = 102
        range_length = 10
        expected = 104
        
        mapper = Mapper([(destination, source, range_length)])
        
        self.assertEqual(expected, mapper.map(seed))

    def test_maps_seed_with_mapper_at_end(self):
        #  98 -> 102
        #  99 -> 103
        #     .
        #     .
        #     .
        # 107 -> 111 *
        
        seed = 107
        source = 98
        destination = 102
        range_length = 10
        expected = 111
        
        mapper = Mapper([(destination, source, range_length)])
        
        self.assertEqual(expected, mapper.map(seed))
        
    def test_maps_seed_bigger_than_mapper(self):
        #  98 -> 102
        #  99 -> 103
        #     .
        #     .
        #     .
        # 107 -> 111
        # ----------
        # 108 -> 108 (default) *
        
        seed = 108
        source = 98
        destination = 102
        range_length = 10
        expected = 108
        
        mapper = Mapper([(destination, source, range_length)])
        
        self.assertEqual(expected, mapper.map(seed))
        
    def test_maps_seed_with_second_mapper(self):
        #   0 -> 5
        #     .
        #     .
        #     .
        #   4 -> 9
        # ----------
        #     .
        #     .
        #     .
        # ----------
        #  98 -> 102
        #  99 -> 103
        # 100 -> 104 *
        #     .
        #     .
        #     .
        # 107 -> 111
        # ----------
        # 109 ->  13
        #     .
        #     .
        #     .
        # 118 ->  22
        # ----------
        
        seed = 100
        source = 98
        destination = 102
        range_length = 10
        expected = 104
        
        mapper = Mapper([(5, 0, 5), (destination, source, range_length), (13, 109, 10)])
        
        self.assertEqual(expected, mapper.map(seed))

unittest.main()