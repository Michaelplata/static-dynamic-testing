import unittest
from src.card_game import CardGame
from src.card import Card


class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()
        self.card = Card("clubs", 1)
        self.card1 = Card("hearts", 1)
        self.card2 = Card("hearts", 3)
        self.cards = [self.card, self.card1, self.card2]

    def test_check_for_ace(self):
        check_for_ace_result = self.card_game.check_for_ace(self.card)
        self.assertEqual(True, check_for_ace_result)
    
    def test_highest_card(self):
        highest_card_result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(3, highest_card_result.value)

    def test_cards_total(self):
        cards_total_result = self.card_game.cards_total(self.cards)
        self.assertEqual('You have a total of5', cards_total_result)


