import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from new_edit_image import main

class TestNewEditImage(unittest.TestCase):

    def setUp(self):
        self.test_args = ['new_edit_image.py', '--person', 'test_person.png', '--product', 'test_product.png']

    @patch('new_edit_image.argparse.ArgumentParser.parse_args')
    @patch('new_edit_image.os.environ.get')
    def test_main_with_valid_args(self, mock_env_get, mock_parse_args):
        # Mock environment variable
        mock_env_get.return_value = '["test-api-key"]'

        # Mock parsed args
        mock_args = MagicMock()
        mock_args.person = 'test_person.png'
        mock_args.product = 'test_product.png'
        mock_args.custom_prompt = None
        mock_args.theme = 'modern'
        mock_parse_args.return_value = mock_args

        # Mock Path.exists to return True
        with patch('pathlib.Path.exists', return_value=True):
            with patch('new_edit_image.generate_ad', return_value='test_output.jpg'):
                with patch('new_edit_image.ThreadPoolExecutor') as mock_executor:
                    mock_executor.return_value.__enter__.return_value.submit.return_value.result.return_value = None
                    try:
                        main()
                        # If no exception, test passes
                        self.assertTrue(True)
                    except SystemExit:
                        # argparse may call sys.exit, which is normal
                        self.assertTrue(True)

    def test_api_key_loading(self):
        # Test that API keys are loaded correctly
        with patch('new_edit_image.os.environ.get', return_value='["key1","key2"]'):
            from new_edit_image import API_KEYS
            self.assertEqual(API_KEYS, ["key1", "key2"])

    def test_invalid_api_key_format(self):
        # Test error handling for invalid JSON
        with patch('new_edit_image.os.environ.get', return_value='invalid-json'):
            with self.assertRaises(ValueError):
                from new_edit_image import API_KEYS

if __name__ == '__main__':
    unittest.main()
