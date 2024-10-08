from common.enums import Suit
from common.models import Hand, Holding


def get_holding_in_suit(hand: Hand, suit: Suit) -> Holding:
    cards = [card for card in hand.cards if card.suit == suit]
    return Holding(cards=cards)
