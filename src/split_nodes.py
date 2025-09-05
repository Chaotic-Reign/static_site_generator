from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_list = []
        value_list = node.text.split(delimiter)
        if len(value_list) % 2 == 0:
            raise Exception("Invalid markdown, formatted section not closed.")
        for i in range(len(value_list)):
            if value_list[i] == "":
                continue
            if i % 2 == 0:
                node_list.append(TextNode(value_list[i], TextType.TEXT))
            else:
                node_list.append(TextNode(value_list[i], text_type))
        new_nodes.extend(node_list)
    return new_nodes

def split_nodes_image(nodes):
    new_nodes = []
    for node in nodes:
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
        else:
            image_alt = images[0][0]
            image_url = images[0][1]
            value1, value2 = node.text.split(f"![{image_alt}]({image_url})", 1)
            nodes_list = [
                TextNode(value1, TextType.TEXT),
                TextNode(image_alt, TextType.IMAGE, image_url),
                ]
            new_nodes.extend(nodes_list)
            if value2 != "":
                node3 = TextNode(value2, TextType.TEXT)
                new_nodes.extend(split_nodes_image([node3]))
    return new_nodes

def split_nodes_link(nodes):
    new_nodes = []
    for node in nodes:
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
        else:
            link_text = links[0][0]
            link_url = links[0][1]
            value1, value2 = node.text.split(f"[{link_text}]({link_url})", 1)
            nodes_list = [
                TextNode(value1, TextType.TEXT),
                TextNode(link_text, TextType.LINK, link_url),
                ]
            new_nodes.extend(nodes_list)
            if value2 != "":
                node3 = TextNode(value2, TextType.TEXT)
                new_nodes.extend(split_nodes_link([node3]))
    return new_nodes