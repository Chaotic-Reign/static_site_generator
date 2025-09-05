from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_nodes import split_nodes_delimiter
from extract_markdown_links_and_images import extract_markdown_images, extract_markdown_links

def main():
    print(
        extract_markdown_links(
            "This text has [one link](www.cookiebake.org/arch/14-08-21), ![one image](www.cookiebake.org/gal/04-07-19), and a [second link](www.cookiebake.org/arch/04-09-21)"
        )
    )

main()