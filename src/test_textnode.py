import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()