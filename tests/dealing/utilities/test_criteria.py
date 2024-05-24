import unittest
from unittest import mock

from dealing.filters import DealFilter
from dealing.utilities import parse_criteria_from_json_file


class ParseCriteriaFromJSONTestCase(unittest.TestCase):

    @mock.patch("json.load")
    @mock.patch("builtins.open")
    def test_parse_criteria_from_json(self, mock_open, mock_json_load):
        # Given
        mock_json_data = {
            "seat": "south",
            "type": "high_card_points",
            "minimum": 15,
            "maximum": 17,
        }
        mock_json_load.return_value = mock_json_data

        # When
        criteria = parse_criteria_from_json_file("fake_path.json")

        # Then
        self.assertTrue(mock_open.called)
        self.assertTrue(mock_json_load.called)
        self.assertIsInstance(criteria, DealFilter)


if __name__ == "__main__":
    unittest.main()
