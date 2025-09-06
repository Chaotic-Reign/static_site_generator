import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnode(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), expected_result)

    def test_text_to_textnode_nested(self):
        text = "This _is **where**_ things get tricky."
        expected_result = [
            TextNode("This ", TextType.TEXT),
            TextNode("is **where**", TextType.ITALIC),
            TextNode(" things get tricky.", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected_result)

    def test_text_to_textnode_multiple(self):
        text = "This `code block contains _italics_`. This is _italics with **bold** inside_ and **bold text.**"
        expected_result = [
            TextNode("This ", TextType.TEXT),
            TextNode("code block contains _italics_", TextType.CODE),
            TextNode(". This is ", TextType.TEXT),
            TextNode("italics with **bold** inside", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold text.", TextType.BOLD),
        ]
        self.assertEqual(text_to_textnodes(text), expected_result)