import os
from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode

def extract_title(markdown):
    title = ""
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            title = line.strip("# ").strip()
            break
    if title == "":
        raise Exception("file has no header")
    return title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html_node = markdown_to_html_node(markdown)
    content = html_node.to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    directory = os.path.dirname(dest_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(dest_path, "w") as f:
        f.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content = os.listdir(dir_path_content)
    for item in content:
        from_path = os.path.join(dir_path_content, item)
        if os.path.isdir(from_path):
            dest_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(from_path, template_path, dest_path)
        if os.path.isfile(from_path):
            file_split = item.split(".")
            new_file = file_split[0] + ".html"
            dest_path = os.path.join(dest_dir_path, new_file)
            generate_page(from_path, template_path, dest_path)