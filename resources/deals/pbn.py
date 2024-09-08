"""PBN Standard specification can be found at: https://www.tistis.nl/pbn/"""

from __future__ import annotations

from typing import List

from common.enums import Seat, Suit, Vulnerability
from models import Deal, Hand
from utilities.hand import get_holding_in_suit


class PBNImportFormatter:

    @classmethod
    def format(cls, deals: List[Deal]) -> str:
        pbn_repr = "% PBN 2.1\n" "% IMPORT\n"

        for deal in deals:
            dealer_repr = cls._represent_dealer(deal)
            vulnerability_repr = cls._represent_vulnerability(deal)
            deal_repr = cls._represent_deal(deal)
            game_repr = "\n".join(
                [
                    f'[Board "{deal.board_number}"]',
                    f'[Dealer "{dealer_repr}"]',
                    f'[Vulnerable "{vulnerability_repr}"]',
                    f'[Deal "{deal_repr}"]',
                ]
            )
            pbn_repr += "\n" + game_repr + "\n"

        return pbn_repr

    @staticmethod
    def _represent_deal(deal: Deal) -> str:

        def represent_hand(hand: Hand) -> str:
            spades = get_holding_in_suit(hand, Suit.SPADES)
            hearts = get_holding_in_suit(hand, Suit.HEARTS)
            diamonds = get_holding_in_suit(hand, Suit.DIAMONDS)
            clubs = get_holding_in_suit(hand, Suit.CLUBS)
            return f"{spades}.{hearts}.{diamonds}.{clubs}"

        north_repr = represent_hand(deal.north)
        east_repr = represent_hand(deal.east)
        south_repr = represent_hand(deal.south)
        west_repr = represent_hand(deal.west)
        return f"N:{north_repr} {east_repr} {south_repr} {west_repr}"

    def _represent_dealer(deal: Deal) -> str:
        dealer_representation_map = {
            Seat.NORTH: "N",
            Seat.EAST: "E",
            Seat.SOUTH: "S",
            Seat.WEST: "W",
        }
        return dealer_representation_map[deal.dealer]

    def _represent_vulnerability(deal: Deal) -> str:
        vulnerability_representation_map = {
            Vulnerability.NONE: "None",
            Vulnerability.NS: "NS",
            Vulnerability.EW: "EW",
            Vulnerability.ALL: "All",
        }
        return vulnerability_representation_map[deal.vulnerability]
