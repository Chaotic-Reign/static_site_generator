from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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

class TestSplitNodesImage(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
         TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image_with_link(self):
        node = TextNode(
            "This node has an ![image](www.cookiebake.org/gal/03-04-21.png) and a [link](www.cookiebake.org/arch/03-04-21)",
            TextType.TEXT,
        )
        expected_result = [
            TextNode("This node has an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "www.cookiebake.org/gal/03-04-21.png"),
            TextNode(" and a [link](www.cookiebake.org/arch/03-04-21)", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_image([node]), expected_result)

    def text_split_image_multiple_nodes(self):
        nodes = [
            TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
         TextType.TEXT,
        ),
        TextNode(
            "This node has an ![image](www.cookiebake.org/gal/03-04-21.png) and a [link](www.cookiebake.org/arch/03-04-21)",
            TextType.TEXT,
        ),
        TextNode(
            "This node has [two](www.cookibake.org/recipes/1420) [links](www.cookiebake.org/info-dump/245)",
            TextType.TEXT,
        ),
        ]

        expected_result = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            TextNode("This node has an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "www.cookiebake.org/gal/03-04-21.png"),
            TextNode(" and a [link](www.cookiebake.org/arch/03-04-21)", TextType.TEXT),
            TextNode(
                "This node has [two](www.cookibake.org/recipes/1420) [links](www.cookiebake.org/info-dump/245)", TextType.TEXT
            ),
        ]

        self.assertEqual(split_nodes_image(nodes), expected_result)

class TestSplitNodesLink(unittest.TestCase):

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
         TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link_with_image(self):
        node = TextNode(
            "This node has an ![image](www.cookiebake.org/gal/03-04-21.png) and a [link](www.cookiebake.org/arch/03-04-21)",
            TextType.TEXT,
        )
        expected_result = [
            TextNode("This node has an ![image](www.cookiebake.org/gal/03-04-21.png) and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "www.cookiebake.org/arch/03-04-21"),
        ]
        self.assertEqual(split_nodes_link([node]), expected_result)

    def text_split_link_multiple_nodes(self):
        nodes = [
            TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
         TextType.TEXT,
        ),
        TextNode(
            "This node has an ![image](www.cookiebake.org/gal/03-04-21.png) and a [link](www.cookiebake.org/arch/03-04-21)",
            TextType.TEXT,
        ),
        TextNode(
            "This node has [two](www.cookibake.org/recipes/1420) [links](www.cookiebake.org/info-dump/245)",
            TextType.TEXT,
        ),
        ]

        expected_result = [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT
                ),
            TextNode("This node has an ![image](www.cookiebake.org/gal/03-04-21.png) and a", TextType.TEXT),
            TextNode("link", TextType.LINK, "www.cookiebake.org/arch/03-04-21"),
            TextNode("This node has ", TextType.TEXT),
            TextNode("two", TextType.LINK, "www.cookibake.org/recipes/1420"),
            TextNode("links", TextType.LINK, "www.cookiebake.org/info-dump/245"),
        ]

        self.assertEqual(split_nodes_link(nodes), expected_result)

    def text_split_link_and_image_multiple_nodes(self):
        nodes = [
            TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
         TextType.TEXT,
        ),
        TextNode(
            "This node has an ![image](www.cookiebake.org/gal/03-04-21.png) and a [link](www.cookiebake.org/arch/03-04-21)",
            TextType.TEXT,
        ),
        TextNode(
            "This node has [two](www.cookibake.org/recipes/1420) [links](www.cookiebake.org/info-dump/245)",
            TextType.TEXT,
        ),
        ]

        result = split_nodes_image(split_nodes_link(nodes))
        expected_result = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            TextNode("This node has an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "www.cookiebake.org/gal/03-04-21.png"),
            TextNode(" and a", TextType.TEXT),
            TextNode("link", TextType.LINK, "www.cookiebake.org/arch/03-04-21"),
            TextNode("This node has ", TextType.TEXT),
            TextNode("two", TextType.LINK, "www.cookibake.org/recipes/1420"),
            TextNode("links", TextType.LINK, "www.cookiebake.org/info-dump/245"),
        ]

        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
