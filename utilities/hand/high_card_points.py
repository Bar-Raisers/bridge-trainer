from common.enums import Rank
from models import Hand


def calculate_high_card_points(hand: Hand) -> int:
    high_card_points_by_rank = {
        Rank.ACE: 4,
        Rank.KING: 3,
        Rank.QUEEN: 2,
        Rank.JACK: 1,
    }
    return sum([high_card_points_by_rank.get(card.rank, 0) for card in hand.cards])
