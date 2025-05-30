class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise  NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        res= ""
        if self.props:
                
            for key in self.props:
                result= f' {key}="{self.props[key]}"'
                res += result
            
        return res

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

