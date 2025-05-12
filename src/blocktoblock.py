from enum import Enum
from markdowntoblocks import markdown_to_blocks
import re

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(text):
    txt= text.split("\n")

    all_lines_are_unordered =  all(line.startswith("- ") for line in txt)
    all_lines_are_quotes = all(line.startswith(">") for line in txt)

    def is_ordered_list(lines):
        for i, line in enumerate(lines, start=1):
            expected_prefix = f"{i}. "
            if not line.startswith(expected_prefix):    
                return False
        return True
    
    if re.match(r'^#{1,6} (?!#)', text):
        return BlockType.HEADING
    elif text[0:3] =="```" and text[-3::1]=='```':
        return BlockType.CODE
    elif all_lines_are_quotes:
        return BlockType.QUOTE
    elif all_lines_are_unordered:
        return BlockType.UNORDERED_LIST 
    elif is_ordered_list(txt):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
