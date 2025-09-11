import unittest
from generate_pages import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_extract_title_1(self):

        md = """# Tolkien Fan Club

    ![JRR Tolkien sitting](/images/tolkien.png)

    Here's the deal, **I like Tolkien**.

    > "I am in fact a Hobbit in all but size."
    >
    > -- J.R.R. Tolkien

    ## Blog posts

    - [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
    - [Why Tom Bombadil Was a Mistake](/blog/tom)
    - [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)

    ## Reasons I like Tolkien

    - You can spend years studying the legendarium and still not understand its depths
    - It can be enjoyed by children and adults alike
    - Disney _didn't ruin it_ (okay, but Amazon might have)
    - It created an entirely new genre of fantasy

    ## My favorite characters (in order)

    1. Gandalf
    2. Bilbo
    3. Sam
    4. Glorfindel
    5. Galadriel
    6. Elrond
    7. Thorin
    8. Sauron
    9. Aragorn

    Here's what `elflang` looks like (the perfect coding language):

    ```
    func main(){
        fmt.Println("Aiya, Ambar!")
    }
    ```

    Want to get in touch? [Contact me here](/contact).

    This site was generated with a custom-built [static site generator](https://www.boot.dev/courses/build-static-site-generator-python) from the course on [Boot.dev](https://www.boot.dev)."""
    
        self.assertEqual(extract_title(md), "Tolkien Fan Club")

    def test_extract_title_2(self):
        md = """I'm putting a paragraph
    before the header,
    just to test my function.
        
    # Heading!
        
    a second paragraph,
    just because.
    no, I'm not doing any markdown formatting
    for this test,
    because I'm lazy and it doesn't matter."""

        self.assertEqual(extract_title(md), "Heading!")

    def test_extract_title_3(self):
        md = """do I really need to make a **third** test for this?
    it's a pretty _simple_ function.
    like, honestly, how many _cases_ are there even for me to test?
    
    # anyway, the heading is at the end this time"""

        self.assertEqual(extract_title(md), "anyway, the heading is at the end this time")
    
