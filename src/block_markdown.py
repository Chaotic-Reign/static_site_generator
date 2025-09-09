from enum import Enum

class BlockType(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNLIST = "unordered list"
    ORLIST = "ordered list"

def block_to_block_type(block):
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
        ):
        return BlockType.HEAD
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        lines = block.split("\n")
        quote = True
        for line in lines:
            if not line.startswith(">"):
                quote = False
        if quote == True:
            return BlockType.QUOTE
    if block.startswith("- "):
        lines = block.split("\n")
        unlist = True
        for line in lines:
            if not line.startswith("- "):
                unlist = False
        if unlist == True:
            return BlockType.UNLIST
    if block.startswith("1. "):
        lines = block.split("\n")
        orlist = True
        for i in range(len(lines)):
            num = i + 1
            if not lines[i].startswith(f"{num}. "):
                orlist = False
        if orlist == True:
            return BlockType.ORLIST
    return BlockType.PARA