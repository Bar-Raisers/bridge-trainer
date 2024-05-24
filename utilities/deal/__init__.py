from typing import List

from models import Deal
from resources.deals import PBNImportFormatter


def write_deals_to_pbn_file(pbn_file_path: str, deals: List[Deal]) -> None:
    pbn_string = PBNImportFormatter.format(deals)
    with open(pbn_file_path, "w+") as pbn_file:
        pbn_file.write(pbn_string)
