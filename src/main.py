from textnode import TextType, TextNode

def main():
    dummy = TextNode(
        "this is some anchor text", 
        TextType.LINK, 
        "https://github.com/Chaotic-Reign/static_site_generator"
        )
    print(dummy)

main()