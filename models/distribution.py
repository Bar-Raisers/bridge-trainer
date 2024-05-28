from __future__ import annotations

import re
from typing import List

from pydantic import BaseModel, computed_field, field_validator


class Distribution(BaseModel):

    distribution: str

    def __str__(self) -> str:
        return self.distribution

    @computed_field
    @property
    def is_exact(self) -> bool:
        return self.distribution.count("=") == 3

    @computed_field
    @property
    def suit_lengths(self) -> List[int]:
        suit_lengths = [
            int(suit_length)
            for suit_length in self.distribution.replace("=", "-").split("-")
        ]

        if self.is_exact:
            return suit_lengths

        return sorted(suit_lengths, reverse=True)

    def matches(self, other: Distribution) -> bool:
        if self.is_exact and other.is_exact:
            return self.distribution == other.distribution

        return sorted(self.suit_lengths, reverse=True) == sorted(
            other.suit_lengths, reverse=True
        )

    @field_validator("distribution")
    @classmethod
    def validate_distribution(cls, distribution: str) -> str:
        exact_distribution_regex = "^(\\d+)=(\\d+)=(\\d+)=(\\d+)$"
        inexact_distribution_regex = "^(\\d+)-(\\d+)-(\\d+)-(\\d+)$"

        exact_match = re.compile(exact_distribution_regex).match(distribution)
        inexact_match = re.compile(inexact_distribution_regex).match(distribution)
        valid_match = exact_match or inexact_match

        if not valid_match:
            raise ValueError(f"distribution {distribution} is malformed")

        suit_lengths = [
            int(suit_length) for suit_length in valid_match.group(1, 2, 3, 4)
        ]

        if sum(suit_lengths) != 13:
            raise ValueError(f"distribution {distribution} must sum to 13")

        return distribution
