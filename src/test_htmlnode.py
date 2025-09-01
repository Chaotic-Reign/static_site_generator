import unittest

from htmlnode import HTMLNode, LeafNode

dict1 = {
    "href": "https://www.cookiebake.org",
    "target": "_blank",
}

node1 = HTMLNode(tag="a", value="Cookie Bake", props=dict1)
node2 = HTMLNode(tag="p", value="This is a paragraph of text.")
node3 = HTMLNode(tag="p", value="This is another paragraph of text.")

list1 = [
    node2, 
    node3
    ]


node4 = HTMLNode(tag="body", children=list1)

nodes1 = [
    node1,
    node2,
    node3,
    node4
]

result1 = """HTMLNode(
Tag: a,
Value: Cookie Bake,
Children: None,
Props: {'href': 'https://www.cookiebake.org', 'target': '_blank'})"""

result2 = """HTMLNode(
Tag: p,
Value: This is a paragraph of text.,
Children: None,
Props: None)"""

result3 = """HTMLNode(
Tag: p,
Value: This is another paragraph of text.,
Children: None,
Props: None)"""

result4 = """HTMLNode(
Tag: body,
Value: None,
Children: [HTMLNode(
Tag: p,
Value: This is a paragraph of text.,
Children: None,
Props: None), HTMLNode(
Tag: p,
Value: This is another paragraph of text.,
Children: None,
Props: None)],
Props: None)"""

expected1 = [
    result1,
    result2,
    result3,
    result4
]

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        expected = 'href="https://www.cookiebake.org" target="_blank"'
        result = node1.props_to_html()
        self.assertEqual(expected, result)

    def test_repr(self):
        result = node1.__repr__()
        self.assertEqual(result1, result)

    def test_repr2(self):
        result = node2.__repr__()
        self.assertEqual(result2, result)

    def test_repr3(self):
        result = node3.__repr__()
        self.assertEqual(result3, result)

    def test_repr4(self):
        result = node4.__repr__()
        self.assertEqual(result4, result)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html(self):
        node = LeafNode("a", "Cookie Bake", dict1)
        self.assertEqual(node.to_html(), '<a href="https://www.cookiebake.org" target="_blank">Cookie Bake</a>')

    def test_leaf_to_html2(self):
        node = LeafNode("b", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html3(self):
        node = LeafNode(None, "This is plain text, wooo")
        self.assertEqual(node.to_html(), "This is plain text, wooo")
