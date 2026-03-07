from textnode import TextNode
class HTMLNode:
    def __init__(self,
                 tag: str = None,
                 value: str = None,
                 children: list[TextNode] = None,
                 props: dict[str:str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_self(self):
        print_props = ""
        for key, value in self.props.items():
            print_props += f'{key}="{value}" '
        return print_props.rstrip()
    
    def __repr__(self):
        print(f"Tag: {self.tag}")
        print(f"Value: {self.value}")
        for child in self.children:
            print(f"{child}")
        print(self.props_to_self())
    