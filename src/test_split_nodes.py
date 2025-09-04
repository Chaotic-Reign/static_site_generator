from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest

class TestSplitNodes(unittest.TestCase):
    
    def test_split_bold(self):
        nodes = [
            TextNode("This is a test node with **bold** text", TextType.TEXT),
        ]

        newnode1 = TextNode("This is a test node with ", TextType.TEXT)
        newnode2 = TextNode("bold", TextType.BOLD)
        newnode3 = TextNode(" text", TextType.TEXT)

        expected_output = [newnode1, newnode2, newnode3]

        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), expected_output)

    def test_split_italic(self):
        nodes = [
            TextNode("This is a test node with _italic_ text", TextType.TEXT),
        ]

        newnode1 = TextNode("This is a test node with ", TextType.TEXT)
        newnode2 = TextNode("italic", TextType.ITALIC)
        newnode3 = TextNode(" text", TextType.TEXT)

        expected_output = [newnode1, newnode2, newnode3]

        self.assertEqual(split_nodes_delimiter(nodes, "_", TextType.ITALIC), expected_output)

    def test_split_code(self):
        nodes = [
            TextNode("This is a test node with a `code block` inside", TextType.TEXT),
        ]

        newnode1 = TextNode("This is a test node with a ", TextType.TEXT)
        newnode2 = TextNode("code block", TextType.CODE)
        newnode3 = TextNode(" inside", TextType.TEXT)

        expected_output = [newnode1, newnode2, newnode3]

        self.assertEqual(split_nodes_delimiter(nodes, "`", TextType.CODE), expected_output)

    def test_split_invalid_syntax(self):
        nodes = [
            TextNode("This is a test node with **invalid syntax", TextType.TEXT),
        ]
        with self.assertRaises(Exception):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    def test_split_invalid_text_type(self):
        nodes = [
            TextNode("This is a test node with _italic_ text", TextType.BOLD),
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "_", TextType.ITALIC), nodes)

    def test_split_multiple_nodes(self):
        node1 = TextNode("This is a test node with **bold** text", TextType.TEXT)
        node2 = TextNode("This is a test node with _italic_ text", TextType.TEXT)
        node3 = TextNode("This is a test node with a `code block` inside", TextType.TEXT)

        nodes = [node1, node2, node3]

        newnode1 = TextNode("This is a test node with ", TextType.TEXT)
        newnode2 = TextNode("bold", TextType.BOLD)
        newnode3 = TextNode(" text", TextType.TEXT)
        newnode4 = TextNode("This is a test node with ", TextType.TEXT)
        newnode5 = TextNode("italic", TextType.ITALIC)
        newnode6 = TextNode(" text", TextType.TEXT)
        newnode7 = TextNode("This is a test node with a ", TextType.TEXT)
        newnode8 = TextNode("code block", TextType.CODE)
        newnode9 = TextNode(" inside", TextType.TEXT)

        expected_result = [newnode1, newnode2, newnode3, newnode4, newnode5, newnode6, newnode7, newnode8, newnode9]

        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

        self.assertEqual(nodes, expected_result)

    def test_split_multiple_markdown_types(self):
        self.maxDiff = None

        node1 = TextNode("This string has **bold** text **twice** in it.", TextType.TEXT)
        node2 = TextNode("This string has **bolded** and _italic_ text.", TextType.TEXT)
        node3 = TextNode("This string has _italics with nested **bold**_ text (but nesting isn't supported).", TextType.TEXT)
        node4 = TextNode("This string ****has empty syntax.", TextType.TEXT)

        nodes = [node1, node2, node3, node4]

        newnode1 = TextNode("This string has ", TextType.TEXT)
        newnode2 = TextNode("bold", TextType.BOLD)
        newnode3 = TextNode(" text ", TextType.TEXT)
        newnode4 = TextNode("twice", TextType.BOLD)
        newnode5 = TextNode(" in it.", TextType.TEXT)
        newnode6 = TextNode("This string has ", TextType.TEXT)
        newnode7 = TextNode("bolded", TextType.BOLD)
        newnode8 = TextNode(" and ", TextType.TEXT)
        newnode9 = TextNode("italic", TextType.ITALIC)
        newnode10 = TextNode(" text.", TextType.TEXT)
        newnode11 = TextNode("This string has ", TextType.TEXT)
        newnode12 = TextNode("italics with nested **bold**", TextType.ITALIC)
        newnode13 = TextNode(" text (but nesting isn't supported).", TextType.TEXT)
        newnode14 = TextNode("This string ", TextType.TEXT)
        newnode15 = TextNode("has empty syntax.", TextType.TEXT)

        expected_result = [
            newnode1,
            newnode2,
            newnode3,
            newnode4,
            newnode5,
            newnode6,
            newnode7,
            newnode8,
            newnode9,
            newnode10,
            newnode11,
            newnode12,
            newnode13,
            newnode14,
            newnode15,
            ]
        
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        self.assertEqual(nodes, expected_result)

if __name__ == "__main__":
    unittest.main()
