import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )
    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()


if __name__ == "__main__":
    unittest.main(
        )
