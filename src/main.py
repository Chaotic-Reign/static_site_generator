from static_to_public import static_to_public
from generate_pages import generate_pages_recursive
import sys

def main():
    if __name__ == "__main__":
        if len(sys.argv) > 1 :
            basepath = sys.argv[1]
        else:
            basepath = "/"

    static_to_public(
        "static",
        "docs"
        )
    
    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath
    )

main()