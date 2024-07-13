import unittest
from maino import processcommand


class TestMaino(unittest.TestCase):

    def test_open_website(self):
        result = processcommand("open google")
        self.assertIn("Opening Google", result)  # Replace with actual expected result

    def test_search(self):
        result = processcommand("search OpenAI on google")
        self.assertIn("Searching for OpenAI", result)  # Replace with actual expected result

    def test_define_word(self):
        result = processcommand("define artificial intelligence")
        self.assertIn("is defined as", result)  # Replace with actual expected result

    def test_news(self):
        result = processcommand("news")
        self.assertIn("Here are the top news headlines", result)  # Replace with actual expected result


if __name__ == '__main__':
    unittest.main()
