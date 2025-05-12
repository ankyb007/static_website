from markdowntoblocks import markdown_to_blocks
from blocktoblock import block_to_block_type, BlockType
from htmlnode import HTMLNode
from textnode import TextNode,TextType,text_node_to_html_node
from texttotextnodes import text_to_textnodes
from parentnode import ParentNode
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = ParentNode("div", children = [])
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = convert_block_to_html(block, block_type)
        parent_node.children.append(html_node)
    return parent_node






def convert_block_to_html(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        content = " ".join([line.strip() for line in block.split("\n")])
        # create a <p> node with processed inline elements
        node = ParentNode(tag = "p", children=[])
        node.children = text_to_children(content)
        return node
    
    elif block_type == BlockType.HEADING:
        level = 0
        for i in block:
            if i == "#":
                level += 1
            else:
                break
        node = ParentNode(tag = f"h{level}", children= [])
        content = block[level:].strip()
        node.children = text_to_children(content)
        return node
    
    elif block_type == BlockType.QUOTE:
        node = ParentNode(tag = "blockquote", children= [])
        content = "\n".join([i.lstrip("> ").strip() for i in block.split("\n")])
        node.children = text_to_children(content)
        return node
    
    elif block_type == BlockType.UNORDERED_LIST:
        ul_node = ParentNode(tag = "ul", children= [])
        lines = block.split("\n")
        
        ul_node.children = []
        for line in lines:
            if line.strip().startswith("- ") or line.strip().startswith("* "):
                content = line.strip()[2:]
                li_node = ParentNode(tag = "li", children= [])
                li_node.children = text_to_children(content)
                ul_node.children.append(li_node)
        return ul_node
    
    elif block_type == BlockType.ORDERED_LIST:
        ol_node = ParentNode(tag = "ol", children= [])
        lines = block.split("\n")

        ol_node.children = []
        for line in lines:
            if re.match(r'^\d+\.\s', line.strip()):
                content = re.sub(r"^\d+\.\s*",'',line.strip())
                li_node = ParentNode(tag = "li", children= [])
                li_node.children = text_to_children(content)
                ol_node.children.append(li_node)
        return ol_node
    
    elif block_type == BlockType.CODE:
        # create <pre> <code> structure
        pre_node = ParentNode(tag = "pre", children= [])
        code_node = ParentNode(tag = "code", children= [])
        
        lines = block.split("\n")
        content = "\n".join(lines[1:-1])+"\n" if len(lines) >2 else ""

        # no inline processing for code blocks
        text_node = TextNode(content,TextType.TEXT)
        code_node.children = [text_node_to_html_node(text_node)]
        pre_node.children = [code_node]
        return pre_node












def text_to_children(text):
    """convert text with inline markdown to list of HTMLnodes"""
    # First convert the text to Textnode objects
    text_nodes = text_to_textnodes(text)
    # Then convert each textnode to HTML node

    html_nodes = []

    for text in text_nodes:
        html_node = text_node_to_html_node(text)
        html_nodes.append(html_node)
    return html_nodes

    


        

