from common.enums import Suit
from common.models import Distribution, Hand


def get_distribution(hand: Hand) -> Distribution:
    suit_lengths = [
        str(len([card for card in hand.cards if card.suit == suit])) for suit in Suit
    ]
    distribution = "=".join(suit_lengths)
    return Distribution(distribution=distribution)
