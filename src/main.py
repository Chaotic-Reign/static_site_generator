from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_image
from extract_markdown import extract_markdown_images, extract_markdown_links
from text_to_textnodes import text_to_textnodes

def main():
    text = "This `code block contains _italics_`. This is _italics with **bold** inside_ and **bold text.**"
    print(text_to_textnodes(text))

main()