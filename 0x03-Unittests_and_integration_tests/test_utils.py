#!/usr/bin/env python3
import unittest
from unittest.mock import Mock, patch
import requests
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        with patch('requests.get') as mock_get:
            mock = Mock()
            mock.json.return_value = test_payload
            mock_get.return_value = mock

            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
