#!/usr/bin/env python3
"""
Parametize a unit test
"""
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Class that defines test cases for access_nested_map
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Tests if function return desired output
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests if KeyError is raised for inputs @parameterized
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Class that defines parameterized test cases for get_json function
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, url, payload):
        """
        Test if function returns desired output
        """

        class Mocked(Mock):
            """
            Inherits from Mock
            """

            def json(self):
                """
                returns payload
                """
                return payload

        with patch("requests.get") as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """
    Class that defines parameterized tests for memoize fn
    """

    def test_memoize(self):
        """Test"""

        class TestClass:
            """testing class"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock:
            fn = TestClass()
            fn.a_property
            fn.a_property
            mock.assert_called_once()
