from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_image
from extract_markdown import extract_markdown_images, extract_markdown_links
from text_to_textnodes import text_to_textnodes
from split_blocks import markdown_to_blocks

def main():
    md = """This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line
            
            - This is a list
            - with items
            """
    print(markdown_to_blocks(md))

main()