import unittest
from unittest import mock

from common.utilities.deal import write_deals_to_pbn_file


class WriteDealsToPBNFileTestCase(unittest.TestCase):

    @mock.patch("common.utilities.deal.PBNImportFormatter")
    @mock.patch("builtins.open", new_callable=mock.mock_open())
    def test_write_deals_to_pbn_file(self, mock_open, mock_pbn_formatter):
        # Given
        deals = []

        # When
        write_deals_to_pbn_file("fake_path.pbn", deals)

        # Then
        self.assertTrue(mock_pbn_formatter.format.called)
        self.assertTrue(mock_open.called)
        self.assertTrue(mock_open.return_value.__enter__().write.called)
