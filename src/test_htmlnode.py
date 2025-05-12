import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"class": "btn"})
        expected = ' class="btn"'
        self.assertEqual(node.props_to_html(),expected)

    def test_eq_mul_prop(self):
        node = HTMLNode(props={"href": "https://boot.dev", "target": "_blank"})
        expected = ' href="https://boot.dev" target="_blank"'
        self.assertEqual(node.props_to_html(),expected)

    def test_props_to_html_with_no_props(self):
        # Test with no properties
        node = HTMLNode()
        expected = ''
        self.assertEqual(node.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()
