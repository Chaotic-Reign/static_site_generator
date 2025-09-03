class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_attributes = ""
        keys_list = list(self.props.keys())
        values_list = []
        for value in self.props:
            values_list.append(self.props[value])
        for i in range(len(values_list)):
            html_attributes = html_attributes + keys_list[i] + '="' + values_list[i] + '"'
            if i < len(self.props) - 1:
                html_attributes = html_attributes + " "
        return html_attributes
    
    def __repr__(self):
        return f"""HTMLNode(\nTag: {self.tag},\nValue: {self.value},\nChildren: {self.children},\nProps: {self.props})"""
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
        self.children = None
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNodes must have a value!")
        if self.tag == None:
            return self.value
        if self.props != None:
            return "<" + self.tag + " " + self.props_to_html() + ">" + self.value + "</" + self.tag + ">"
        else:
            return "<" + self.tag + ">" + self.value + "</" + self.tag + ">"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.value = None
        self.props = props

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent Nodes must have a tag!")
        if self.children == None:
            raise ValueError("Parent Nodes must have one or more children!")
        if self.props != None:
            opening = "<" + self.tag + " " + self.props_to_html() + ">"
        else:
            opening = "<" + self.tag + ">"
        ending = "</" + self.tag + ">"
        middle = ""
        for child in self.children:
            middle = middle + child.to_html()
        result = opening + middle + ending
        return result