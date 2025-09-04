from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_nodes import split_nodes_delimiter

def main():
    nodes = [
            TextNode("This is a test node with **bold** text", TextType.TEXT),
        ]
    print(split_nodes_delimiter(nodes, "**", TextType.BOLD))

main()