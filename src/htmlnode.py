from textnode import TextNode
class HTMLNode:
    def __init__(self,
                 tag = None,
                 value = None,
                 children = None,
                 props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_self(self):
        print_props = ""
        if self.props is not None:
            for key, value in self.props.items():
                print_props += f'{key}="{value}" '
        return print_props.rstrip()
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None")
        if self.children is None:
            raise ValueError("Children cannot be None")
        html_repr = f"<{self.tag}>"
        for child in self.children:
            html_repr += child.to_html()
        html_repr += f"</{self.tag}>"
        return html_repr      
