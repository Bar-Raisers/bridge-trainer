import argparse

from dealing.engine import BruteForceDealEngine
from dealing.utilities import parse_criteria_from_json_file
from utilities.deal import write_deals_to_pbn_file


def main():
    parser = __create_parser()
    args = parser.parse_args()

    criteria = parse_criteria_from_json_file(args.input_path)
    deal_engine = BruteForceDealEngine(criteria)
    deals = deal_engine.generate(deal_quantity=args.deal_quantity)
    write_deals_to_pbn_file(deals)


def __create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str, help="path to read input deal criteria")
    parser.add_argument("output_path", type=str, help="path to write output PBN file")
    parser.add_argument(
        "--deal_quantity",
        type=int,
        required=True,
        help="desired quantity of hands matching criteria",
    )
    return parser


if __name__ == "__main__":
    main()
