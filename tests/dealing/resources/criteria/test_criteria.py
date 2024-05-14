import unittest
from unittest import mock

from dealing.resources.criteria import load_criteria_from_json_file, parse_criteria


class LoadCriteriaTestCase(unittest.TestCase):

    @mock.patch("json.load")
    @mock.patch("builtins.open")
    def test_load_criteria_from_json_file(self, mock_open, mock_json_load):
        # Given
        mock_json_data = {"mock": "content"}
        mock_json_load.return_value = mock_json_data

        # When
        criteria_json = load_criteria_from_json_file("fake_path.json")

        # Then
        self.assertTrue(mock_open.called)
        self.assertTrue(mock_json_load.called)
        self.assertDictEqual(mock_json_data, criteria_json)


class ParseCriteriaTestCase(unittest.TestCase):

    @mock.patch("dealing.resources.criteria.parse_high_card_points_criteria")
    def test_parse_criteria_with_high_card_points_criteria(self, mock_filter):
        # Given
        attributes = {
            "type": "high_card_points",
        }

        # When
        parse_criteria(attributes)

        # Then
        self.assertTrue(mock_filter.called)


if __name__ == "__main__":
    unittest.main()
