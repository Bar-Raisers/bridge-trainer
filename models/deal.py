from pydantic import BaseModel

from common.enums import Seat, Vulnerability
from models.hand import Hand


class Deal(BaseModel):

    board_number: int
    dealer: Seat
    vulnerability: Vulnerability

    north: Hand
    east: Hand
    south: Hand
    west: Hand

    def __init__(self, **kwargs) -> None:
        board_number = kwargs.get("board_number", None)
        if board_number:
            kwargs["dealer"] = Seat.get_dealer_seat_from_board_number(board_number)
            kwargs["vulnerability"] = Vulnerability.from_board_number(board_number)

        super().__init__(**kwargs)

    def __str__(self) -> str:
        return "\n".join(
            [
                f"{Seat.NORTH}: {self.north}",
                f"{Seat.EAST}: {self.east}",
                f"{Seat.SOUTH}: {self.south}",
                f"{Seat.WEST}: {self.west}",
            ]
        )

    def get_hand(self, seat: Seat) -> Hand:
        hands_by_seat = {
            Seat.NORTH: self.north,
            Seat.EAST: self.east,
            Seat.SOUTH: self.south,
            Seat.WEST: self.west,
        }
        return hands_by_seat[seat]
