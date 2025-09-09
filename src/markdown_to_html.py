from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from split_blocks import markdown_to_blocks
from extract_markdown import extract_markdown_images, extract_markdown_links
from block_markdown import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes

def block_type_to_tag(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARA:
            return "p"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.HEAD:
            if block.startswith("# "):
                return "h1"
            if block.startswith("## "):
                return "h2"
            if block.startswith("### "):
                return "h3"
            if block.startswith("#### "):
                return "h4"
            if block.startswith("##### "):
                return "h5"
            if block.startswith("###### "):
                return "h6"
        case BlockType.UNLIST:
            return "ul"
        case BlockType.ORLIST:
            return "ol"
        case _:
            raise Exception("invalid block type")
        
def text_to_children(block):
    nodes = []
    block_type = block_to_block_type(block)
    if block_type == BlockType.UNLIST or block_type == BlockType.ORLIST:
        parents = block.split("\n")
        stripped_parents = []

        if block_type == BlockType.UNLIST:
            for parent in parents:
                stripped_parent = parent[2:]
                stripped_parents.append(stripped_parent)
                
        if block_type == BlockType.ORLIST:
            for parent in parents:
                stripped_parent = parent[3:]
                stripped_parents.append(stripped_parent)

        for stripped_parent in stripped_parents:
            children = []
            text_nodes = text_to_textnodes(stripped_parent)

            for node in text_nodes:
                children.append(text_node_to_html_node(node))

            parent_node = ParentNode("li", children)
            nodes.append(parent_node)

    if block_type == BlockType.HEAD:
        block_tag = (block_type_to_tag(block))

        match block_tag:
            case "h1":
                block = block.strip("# ")
            case "h2":
                block = block.strip("## ")
            case "h3":
                block = block.strip("### ")
            case "h4":
                block = block.strip("#### ")
            case "h5":
                block = block.strip("##### ")
            case "h6":
                block = block.strip("###### ")

        text_nodes = text_to_textnodes(block)

        for text_node in text_nodes:
            node = text_node_to_html_node(text_node)
            nodes.append(node)

    if block_type == BlockType.QUOTE:
        lines = block.split("\n")
        p_block_values = []
        p_block = ""

        for i in range(len(lines)):
            new_line = lines[i].strip(">")

            if new_line == "":
                p_block = p_block.strip()
                p_block_values.append(p_block)
                p_block = ""

            if i == (len(lines) - 1):
                p_block = p_block + new_line
                p_block = p_block.strip()
                p_block_values.append(p_block)
                    
            else:
                p_block = p_block + new_line + " "

        for value in p_block_values:
            children = []
            text_nodes = text_to_textnodes(value)

            for node in text_nodes:
                children.append(text_node_to_html_node(node))
            
            p_node = ParentNode("p", children)
            nodes.append(p_node)

    if block_type == BlockType.PARA:
        block = " ".join(block.split("\n"))
        text_nodes = text_to_textnodes(block)

        for text_node in text_nodes:
            node = text_node_to_html_node(text_node)
            nodes.append(node)

    return nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        if block == "":
            continue
        if block_to_block_type(block) != BlockType.CODE:
            block_tag = block_type_to_tag(block)
            nodes = text_to_children(block)
            node = ParentNode(block_tag, nodes)
            html_nodes.append(node)
        if block_to_block_type(block) == BlockType.CODE:
            text = (block.strip("```")).lstrip("\n")
            text_node = TextNode(text, TextType.CODE)
            node = ParentNode("pre", [text_node_to_html_node(text_node)])
            html_nodes.append(node)
    html_node = ParentNode("div", html_nodes)
    return html_node


