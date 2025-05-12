from splitdelim import split_nodes_delimiter
from textnode import TextNode,TextType
from splitimageslinks import split_nodes_image,split_nodes_link
def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_image([node])
    nodes =  split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    return nodes
  
   
    

