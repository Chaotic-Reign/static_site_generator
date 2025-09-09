

def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    stripped_lines = []
    for line in lines:
        stripped_lines.append(line.strip())
    md = "\n".join(stripped_lines)
    blocks = md.split("\n\n")
    new_blocks = []
    for block in blocks:
        new_blocks.append(block.strip())
    return new_blocks