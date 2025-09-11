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
        new_lines = []
        for line in lines:
            new_line = line.strip(">").strip()
            if new_line != "":
                new_lines.append(new_line)
        block = " ".join(new_lines)
        text_nodes = text_to_textnodes(block)

        for text_node in text_nodes:
            node = text_node_to_html_node(text_node)
            nodes.append(node)

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
            print(f"Debug - raw code block: {repr(block)}")
            text = block[4:-3]
            print(f"Debug - extracted text: {repr(text)}")
            code = LeafNode("code", text)
            print(f"Debug - HTML output: {code.to_html()}")
            node = ParentNode("pre", [code])
            html_nodes.append(node)
    html_node = ParentNode("div", html_nodes)
    return html_node


