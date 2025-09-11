from static_to_public import static_to_public
from generate_pages import generate_pages_recursive

def main():
    static_to_public(
        "static",
        "public"
        )
    
    generate_pages_recursive(
        "content",
        "template.html",
        "public"
    )

main()