from splitdelim import split_nodes_delimiter
from textnode import TextNode, TextType

import unittest

class TestSplitDem(unittest.TestCase):

    def test_code_delimiter_split(self):
        node = TextNode("a `foo` b", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "a ")
        self.assertEqual(new_nodes[1].text, "foo")
        self.assertEqual(new_nodes[2].text, " b")

        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_unmatched_delim(self):
        node = TextNode("a `foo b", TextType.TEXT)
        #new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIn("Unmatched",str(context.exception))

    def test_bold(self):
        node = TextNode("ankit bhalla", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)




if __name__ == "__main__":
    unittest.main()




    
