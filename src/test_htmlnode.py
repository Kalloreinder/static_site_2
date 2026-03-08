import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_print_self_eq(self):
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
    
    def test_print_self_not_eq(self):
        htmlnode = HTMLNode(
            "<p>",
            "This is an HTML Node",
            None,
            {"href": "https://www.google.com"}
        )
        htmlnode2 = HTMLNode(
            "<p>",
            "This is not really and HTML Node",
            None,
            {"href": "https://www.firefox.com"}
        )
        self.assertNotEqual(htmlnode.props_to_self(), htmlnode2.props_to_self())
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()