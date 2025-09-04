from textnode import TextNode, TextType

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