import re
from textnode import TextNode,TextType
from extractmarkdownimages import extract_markdown_images,extract_markdown_links

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            images = extract_markdown_images(node.text)
            if not images:
                result.append(node)
            else:
                image_alt, image_url = images[0]
                image_markdown = f"![{image_alt}]({image_url})"
                
                

                parts = node.text.split(image_markdown,1)
                if parts[0]:
                    result.append(TextNode(parts[0], TextType.TEXT))

                image_node = TextNode(image_alt, TextType.IMAGE, image_url)
                result.append(image_node)

                if len(parts) > 1 and parts[1]:
                    remaining_node = TextNode(parts[1], TextType.TEXT)
                    result.extend(split_nodes_image([remaining_node]))
    return result



def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            links = extract_markdown_links(node.text)
            if not links:
                result.append(node)
            else:
                link_alt, link_url = links[0]
                link_markdown = f"[{link_alt}]({link_url})"
                
                

                parts = node.text.split(link_markdown,1)
                if parts[0]:
                    result.append(TextNode(parts[0], TextType.TEXT))

                link_node = TextNode(link_alt, TextType.LINK, link_url)
                result.append(link_node)

                if len(parts) > 1 and parts[1]:
                    remaining_node = TextNode(parts[1], TextType.TEXT)
                    result.extend(split_nodes_link([remaining_node]))

    return result




        

