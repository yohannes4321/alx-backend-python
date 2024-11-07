#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        # The exception message includes quotes around the key
        self.assertEqual(str(context.exception), f"'{expected}'")


if __name__ == "__main__":
    unittest.main()
