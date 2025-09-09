import unittest
from split_blocks import markdown_to_blocks
from block_markdown import BlockType, block_to_block_type

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

if __name__ == "__main__":
    unittest.main()