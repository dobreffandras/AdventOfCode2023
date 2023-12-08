from Day7_b import Player
import unittest

class TestPlayer(unittest.TestCase):
    def test_five_of_a_kind(self):
        self.assertEqual(6, Player("AAAAA", 1).score[0])

    def test_four_of_a_kind(self):
        self.assertEqual(5, Player("AA2AA", 1).score[0])
                
    def test_full_house(self):
        self.assertEqual(4, Player("AA22A", 1).score[0])
                
    def test_three_of_a_kind(self):
        self.assertEqual(3, Player("AA23A", 1).score[0])
                
    def test_two_pairs(self):
        self.assertEqual(2, Player("A323A", 1).score[0])
                
    def test_one_pair(self):
        self.assertEqual(1, Player("A234A", 1).score[0])
                
    def test_high_card(self):
        self.assertEqual(0, Player("A2345", 1).score[0])
        
    def test_five_of_a_kind_with_one_Joker(self):
        self.assertEqual(6, Player("AAAAJ", 1).score[0])

    def test_four_of_a_kind_with_one_Joker(self):
        self.assertEqual(5, Player("AA2AJ", 1).score[0])
                
    def test_full_house_with_one_Joker(self):
        self.assertEqual(4, Player("AA22J", 1).score[0])
                
    def test_three_of_a_kind_with_one_Joker(self):
        self.assertEqual(3, Player("A32JA", 1).score[0])

    def test_one_pair_with_one_Joker(self):
        self.assertEqual(1, Player("A234J", 1).score[0])
        
    def test_five_of_a_kind_with_two_Jokers(self):
        self.assertEqual(6, Player("AAAJJ", 1).score[0])

    def test_four_of_a_kind_with_two_Jokers(self):
        self.assertEqual(5, Player("AA2JJ", 1).score[0])
                
    def test_three_of_a_kind_with_two_Jokers(self):
        self.assertEqual(3, Player("AJ23J", 1).score[0])
        
    def test_five_of_a_kind_with_three_Jokers(self):
        self.assertEqual(6, Player("AAJJJ", 1).score[0])

    def test_four_of_a_kind_with_three_Jokers(self):
        self.assertEqual(5, Player("AJ2JJ", 1).score[0])
        
    def test_five_of_a_kind_with_four_Jokers(self):
        self.assertEqual(6, Player("AJJJJ", 1).score[0])

unittest.main()        