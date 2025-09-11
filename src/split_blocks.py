

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        if block.strip().startswith("```") and block.strip().endswith("```"):
            lines = block.split('\n')
            while lines and lines[0].strip() == '':
                lines.pop(0)
            while lines and lines[-1].strip() == '':
                lines.pop()
            block = '\n'.join(lines)
        else:
            block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks