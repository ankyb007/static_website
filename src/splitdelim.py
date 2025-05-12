from textnode import TextNode, TextType
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    lst = []
    for i in old_nodes:
        
        if i.text_type != TextType.TEXT:
            lst.append(i)
        else:
            nodes_split = i.text.split(delimiter)
            if len(nodes_split)%2 == 0:
                raise Exception("Unmatched delimiter!")

            for j in range(len(nodes_split)):
                if nodes_split[j] != "":
                    if j%2 == 0:
                        lst.append(TextNode(nodes_split[j],TextType.TEXT))
                    else:
                        lst.append(TextNode(nodes_split[j],text_type))
    return lst


            





