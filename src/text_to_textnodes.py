from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT),]
    
    text_bold = text.split("**")
    text_italic = text.split("_")
    text_code = text.split("`")
    count = 0

    while text != "" and count < 3 and (
        len(text_bold) > 1
        or len(text_italic) > 1
        or len(text_code) > 1
    ):
        delimiters = {}
        delimiters["bold"] = len(text_bold[0])
        delimiters["italic"] = len(text_italic[0])
        delimiters["code"] = len(text_code[0])
        delimiters = sorted(delimiters.items(), key=lambda item: item[1])
        match delimiters[0][0]:
            case "bold":
                split = text.split(f"{text_bold[0]}" + "**" + f"{text_bold[1]}" + "**", 1)
                text = split[1]
                nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
            case "italic":
                split = text.split(f"{text_italic[0]}" + "_" f"{text_italic[1]}" + "_", 1)
                text = split[1]
                nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
            case "code":
                split = text.split(f"{text_code[0]}" + "`" + f"{text_code[1]}" + "`", 1)
                text = split[1]
                nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        
        text_bold = text.split("**")
        text_italic = text.split("_")
        text_code = text.split("`")
        count += 1

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
