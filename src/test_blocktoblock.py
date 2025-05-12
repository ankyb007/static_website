import unittest
from blocktoblock import block_to_block_type,BlockType

class TestBlocktoBlock(unittest.TestCase):

    def test_blocktoblock_heading(self):

        text = "### This is a heading"
        type = block_to_block_type(text)
        self.assertEqual(type, BlockType.HEADING)


    def test_blocktoblock_unordered_list(self):

        text = "- This is line1" \
        "- This is line 2" \
        "- This is line 3"
        type = block_to_block_type(text)
        self.assertEqual(type, BlockType.UNORDERED_LIST)    

if __name__ == "__main__":
    unittest.main()