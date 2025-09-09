import unittest
from split_blocks import markdown_to_blocks
from block_markdown import BlockType, block_to_block_type
from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode

class TestMarkdownToBlock(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line
            
        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_2(self):
        md = """This is the first paragraph.
        It contains **bolded** text.
        It also contains _italics_.
        
        This is a new paragraph.
        I am tired of making these tests.
        
        # Someone save me
        # (yes, I know it doesn't make sense to put the heading at the end)
        """

        expected_result = [
            "This is the first paragraph.\nIt contains **bolded** text.\nIt also contains _italics_.",
            "This is a new paragraph.\nI am tired of making these tests.",
            "# Someone save me\n# (yes, I know it doesn't make sense to put the heading at the end)"
        ]

        self.assertEqual(expected_result, markdown_to_blocks(md))

class TestBlockToBlockType(unittest.TestCase):

    def test_heading1(self):
        block = "# heading1"
        self.assertEqual(block_to_block_type(block), BlockType.HEAD)

    def test_heading2(self):
        block = "## heading2"
        self.assertEqual(block_to_block_type(block), BlockType.HEAD)

    def test_heading3(self):
        block = "### heading3"
        self.assertEqual(block_to_block_type(block), BlockType.HEAD)

    def test_heading4(self):
        block = "#### heading4"
        self.assertEqual(block_to_block_type(block), BlockType.HEAD)

    def test_heading5(self):
        block = "##### heading5"
        self.assertEqual(block_to_block_type(block), BlockType.HEAD)

    def test_heading6(self):
        block = "###### heading6"
        self.assertEqual(block_to_block_type(block), BlockType.HEAD)

    def test_code(self):
        block = "```This is a code block```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = ">This is a quote\n>with multiple lines\n>it is three lines long"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unlist(self):
        block = "- This is\n- an unordered\n- list"
        self.assertEqual(block_to_block_type(block), BlockType.UNLIST)

    def test_orlist(self):
        block = "1. This is\n2. an ordered\n3. list"
        self.assertEqual(block_to_block_type(block), BlockType.ORLIST)

    def test_paragraph0(self):
        block = "This is a normal paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

    def test_paragraph1(self):
        block = "- This is\nnot an\n- unordered list"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

    def test_paragraph2(self):
        block = "1. This is\n2. not an\nordered list"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

    def test_paragraph3(self):
        block = "2. This is\n3. also not\n4. an ordered list"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

    def test_paragraph4(self):
        block = "1. This is\n3. yet again\2. not an ordered list"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

    def test_paragraph5(self):
        block = ">This is\nnot a\n>quote"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)
    
    def test_paragraph6(self):
        block = "```This is not a code block"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

    def test_paragraph7(self):
        block = "This is also not a code block```"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

    def test_paragraph8(self):
        block = "####### This is not a valid heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

    def test_paragraph9(self):
        block = "#This is also not a valid heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_paragraphs(self):
        self.maxDiff = None

        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        self.maxDiff = None

        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """>This is
        >a
        >blockquote
        >
        >with two
        >paragraphs
        """
        node = markdown_to_html_node(md)
        html = node.to_html()

        expected_result = "<div><blockquote><p>This is a blockquote</p><p>with two paragraphs</p></blockquote></div>"

        self.assertEqual(html, expected_result)

    def test_heading(self):
        md = """# heading1

        ## heading2

        ### heading3

        #### heading4

        ##### heading5

        ###### heading6"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        expected_result = "<div><h1>heading1</h1><h2>heading2</h2><h3>heading3</h3><h4>heading4</h4><h5>heading5</h5><h6>heading6</h6></div>"

        self.assertEqual(html, expected_result)

    def test_unlist(self):
        md = """- This is
        - an unordered
        - list"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        expected_result = "<div><ul><li>This is</li><li>an unordered</li><li>list</li></ul></div>"

        self.assertEqual(html, expected_result)

    def test_orlist(self):
        md = """1. This is
        2. an ordered
        3. list"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        expected_result = "<div><ol><li>This is</li><li>an ordered</li><li>list</li></ol></div>"

        self.assertEqual(html, expected_result)

    def test_quote_with_md(self):
        md = """>This is
        >a
        >blockquote
        >
        >with two
        >paragraphs and **bolded** text
        """
        node = markdown_to_html_node(md)
        html = node.to_html()

        expected_result = "<div><blockquote><p>This is a blockquote</p><p>with two paragraphs and <b>bolded</b> text</p></blockquote></div>"

        self.assertEqual(html, expected_result)

    def test_unlist_with_md(self):
        md = """- This is
        - an unordered
        - list with _italic_ text"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        expected_result = "<div><ul><li>This is</li><li>an unordered</li><li>list with <i>italic</i> text</li></ul></div>"

        self.assertEqual(html, expected_result)

    def test_orlist_with_md(self):
        md = """1. This is
        2. an ordered
        3. list with **bolded**
        4. and _italic_ text"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        expected_result = "<div><ol><li>This is</li><li>an ordered</li><li>list with <b>bolded</b></li><li>and <i>italic</i> text</li></ol></div>"

        self.assertEqual(html, expected_result)

if __name__ == "__main__":
    unittest.main()