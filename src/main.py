from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_image
from extract_markdown import extract_markdown_images, extract_markdown_links

def main():
    node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
         TextType.TEXT,
        )
    print(split_nodes_link([node]))

main()