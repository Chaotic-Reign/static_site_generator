from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    dummy = TextNode(
        "this is some anchor text", 
        TextType.LINK, 
        "https://github.com/Chaotic-Reign/static_site_generator"
        )
    print(dummy)

main()