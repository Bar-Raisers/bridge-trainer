from random import shuffle

from common.enums import Rank, Suit
from common.models import Card, Distribution, Hand


def generate_hand_with_distribution(distribution: Distribution) -> Hand:
    suit_lengths = distribution.suit_lengths

    if not distribution.is_exact:
        shuffle(suit_lengths)

    cards = [
        Card(rank=rank, suit=suit)
        for rank_index, rank in enumerate(Rank)
        for suit_index, suit in enumerate(Suit)
        if rank_index < suit_lengths[suit_index]
    ]

    return Hand(cards=cards)
