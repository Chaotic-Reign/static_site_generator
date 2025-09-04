import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_def(self):
        node = TextNode("This has no url", TextType.TEXT, None)
        node2 = TextNode("This has no url", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.cookiebake.org/arch/01-03-22/oatmeal-raisin-is-superior")
        node2 = TextNode("This is not a link", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This text is the same", TextType.TEXT, "https://www.cookieback.org/arch/03-04-21/why-baking-soda-is-important")
        node2 = TextNode("This text is the same", TextType.TEXT)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNODE(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
        node = TextNode("This is a code block", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code block")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "www.cookiebake.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "www.cookiebake.org"})

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "www.cookiebake.org/gal/02-12-21")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.cookiebake.org/gal/02-12-21", "alt": "This is an image"})

    def test_invalid_text_type(self):
        node = TextNode("This will raise an Exception", "Bold")
        with self.assertRaises(Exception):
            html_node = text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()