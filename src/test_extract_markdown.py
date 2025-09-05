import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with not ![one](www.cookiebake.org/gal/04-05-19) but ![two](www.cookiebake.org/gal/05-05-19) images."
        )
        self.assertEqual([("one", "www.cookiebake.org/gal/04-05-19"), ("two", "www.cookiebake.org/gal/05-05-19")], matches)

    def test_images_and_links(self):
        matches = extract_markdown_images(
            "This text has an ![image](www.cookiebake.org/gal/03-06-21) and a [link](www.cookiebake.org/arch/04-07-21) and a ![second image](www.cookiebake.org/gal/08-02-22)"
        )
        self.assertEqual([("image", "www.cookiebake.org/gal/03-06-21"), ("second image", "www.cookiebake.org/gal/08-02-22")], matches)

class TestExtractMarkdownLinks(unittest.TestCase):

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This text has a [link](www.cookiebake.org)"
        )
        self.assertEqual([("link", "www.cookiebake.org")], matches)

    def test_multiple_links(self):
        matches = extract_markdown_links(
            "This text has [multiple](www.cookiebake.org/arch/03-12-23) [links](www.cookiebake.org/arch/15-02-21)"
        )
        self.assertEqual([("multiple", "www.cookiebake.org/arch/03-12-23"), ("links", "www.cookiebake.org/arch/15-02-21")], matches)

    def test_links_and_images(self):
        matches = extract_markdown_links(
            "This text has [one link](www.cookiebake.org/arch/14-08-21), ![one image](www.cookiebake.org/gal/04-07-19), and a [second link](www.cookiebake.org/arch/04-09-21)"
        )
        self.assertEqual([("one link", "www.cookiebake.org/arch/14-08-21"), ("second link", "www.cookiebake.org/arch/04-09-21")], matches)

if __name__ == "__main__":
    unittest.main()