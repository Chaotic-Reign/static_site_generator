from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_image
from extract_markdown import extract_markdown_images, extract_markdown_links
from text_to_textnodes import text_to_textnodes
from split_blocks import markdown_to_blocks
from markdown_to_html import markdown_to_html_node
from static_to_public import static_to_public

def main():
    static_to_public(
        "/home/mascna/workspace/github.com/chaotic_reign/boot.dev/static_site_generator/static",
        "/home/mascna/workspace/github.com/chaotic_reign/boot.dev/static_site_generator/public"
        )

main()