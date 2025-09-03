import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):

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

    
class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )
        
    def test_to_html_no_children(self):
        parent_node = ParentNode("body", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_multiple_children(self):
        child_node1 = LeafNode("p", "paragraph1")
        child_node2 = LeafNode("a", "link", {"href": "https://www.site.com"})
        child_node3 = LeafNode("p", "paragraph2")
        parent_node = ParentNode("body", [child_node1, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(),
            '<body><p>paragraph1</p><a href="https://www.site.com">link</a><p>paragraph2</p></body>'
            )
        
    def test_to_html_parent_has_props(self):
        child_node = LeafNode("b", "bold text")
        parent_node = ParentNode ("div", [child_node], {"id": "yolo"})
        self.assertEqual(parent_node.to_html(), '<div id="yolo"><b>bold text</b></div>')

    def test_to_html_grandparent_has_a_lot_of_grandbabies_why_did_you_have_so_many_kids_grandma(self):
        self.maxDiff = None

        child_one_of_one = LeafNode(None, "Sentence one. ")
        child_two_of_one = LeafNode("b", "Sentence two is bold. ")
        child_three_of_one = LeafNode("a", "Sentence three is a link.", {"href": "www.linky_link.net"})
        child_one = ParentNode("p", [child_one_of_one, child_two_of_one, child_three_of_one])

        child_one_of_two = LeafNode("i", "Some italics this time because I am bored. ")
        child_two_of_two = LeafNode(None, "Why did I make so many children?")
        child_two = ParentNode("div", [child_one_of_two, child_two_of_two], {"id": "tbh-idk-the-difference-between-div-and-p"})

        child_one_of_three = LeafNode("b", "There is something wrong with child three. ")
        child_two_of_three = LeafNode("i", "Why did child three have so many kids? ")
        child_three_of_three = LeafNode(None, "Like five kids? ")
        child_four_of_three = LeafNode("a", "Are you kidding me?", {"href": "www.crazy_people_only.web"})
        child_one_of_five_of_three = LeafNode("i", " Five is way too many kids, and now five has a grandchild too?!?")
        child_five_of_three = ParentNode("b", [child_one_of_five_of_three])
        child_three = ParentNode("span", [child_one_of_three, child_two_of_three, child_three_of_three, child_four_of_three, child_five_of_three], {"title": "yeah, idk how span works either"})

        child_one_of_four = LeafNode(None, "Why did I do this to myself you ask? ")
        child_two_of_four = LeafNode(None, "I am a psychopath. ")
        child_three_of_four = LeafNode(None, "That is why.")
        child_four = ParentNode("p", [child_one_of_four, child_two_of_four, child_three_of_four])

        child_one_of_five = LeafNode("i", "Child five is the only sane one here.")
        child_five = ParentNode("p", [child_one_of_five])

        grandparent = ParentNode("body", [child_one, child_two, child_three, child_four, child_five])

        self.assertEqual(
            grandparent.to_html(),
            '<body><p>Sentence one. <b>Sentence two is bold. </b><a href="www.linky_link.net">Sentence three is a link.</a></p><div id="tbh-idk-the-difference-between-div-and-p"><i>Some italics this time because I am bored. </i>Why did I make so many children?</div><span title="yeah, idk how span works either"><b>There is something wrong with child three. </b><i>Why did child three have so many kids? </i>Like five kids? <a href="www.crazy_people_only.web">Are you kidding me?</a><b><i> Five is way too many kids, and now five has a grandchild too?!?</i></b></span><p>Why did I do this to myself you ask? I am a psychopath. That is why.</p><p><i>Child five is the only sane one here.</i></p></body>'
        )
