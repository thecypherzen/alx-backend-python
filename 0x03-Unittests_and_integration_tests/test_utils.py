#!/usr/bin/env python3
"""Unittests for a function"""

from parameterized import parameterized
from utils import access_nested_map as anp
from unittest import TestCase


class TestAccessNestedMap(TestCase):
    """Unittest for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests access_nested_map by parameterization"""
        self.assertEqual(anp(nested_map, path), expected)
