import unittest
from markdowntoblocks import markdown_to_blocks

class TestMarkdowntoBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):

        text ="""This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line





- This is a list
- with items
"""

        blocks = markdown_to_blocks(text)
        self.assertEqual(blocks, [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ])

if __name__ == "__main__":
    unittest.main()

