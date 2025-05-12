import unittest

from textnode import TextNode, TextType,text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node1)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node1 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node1)

    def test_noteq_url(self):
        node = TextNode("This is a text node", TextType.TEXT, "www.boot.dev")
        node1 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node1)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
if __name__ == "__main__":
    unittest.main()

