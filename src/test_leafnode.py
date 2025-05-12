import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World")
        self.assertEqual(node.to_html(), "<p>Hello World</p>")
        
    def test_empty_value(self):
        node = LeafNode("p","")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_attributes(self):
        node = LeafNode("p","Click me!", {"href": "https:// www.google.com"})
        self.assertEqual(node.to_html(), '<p href="https:// www.google.com">Click me!</p>')

    def test_no_tag(self):
        node = LeafNode("", "Chuk de fatte!")
        self.assertEqual(node.to_html(), 'Chuk de fatte!')

if __name__ =="__main__":
    unittest.main()