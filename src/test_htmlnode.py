import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print_self(self):
        htmlnode = HTMLNode(
            "<p>",
            "This is an HTML Node",
            None,
            {"href": "https://www.google.com"}
        )
        htmlnode2 = HTMLNode(
            "<p>",
            "This is an HTML Node",
            None,
            {"href": "https://www.google.com"}
        )
        self.assertEqual(htmlnode.props_to_self(), htmlnode2.props_to_self())