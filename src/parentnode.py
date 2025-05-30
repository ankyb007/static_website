from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag,children, props=None):
        super().__init__(tag,None, children, props)

    def to_html(self):
        if  self.tag is None:
            raise ValueError("Bhai tag kaha hai?")
        if  self.children is None:
            raise ValueError("Bhai bacche kaha hain?")
        children_html = ""
        
        
        for child in self.children:
            children_html += child.to_html()
            
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
        
