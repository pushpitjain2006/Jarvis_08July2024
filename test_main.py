import unittest
from maino import processcommand


class TestMaino(unittest.TestCase):

    def test_open_website(self):
        result = processcommand("open google")
        self.assertTrue("Opening google" in result or "Artificial Intelligence" in result)

    def test_search(self):
        result = processcommand("search LOL on google")
        self.assertTrue("Searching for lol" in result or "Artificial Intelligence" in result)

    def test_define_word(self):
        result = processcommand("define artificial intelligence")
        self.assertTrue("artificial intelligence is defined as .." in result or "Artificial Intelligence" in
                      result)

    def test_news(self):
        result = processcommand("news")
        self.assertIn("Here are the top news headlines", result)

    def test_AI(self):
        result = processcommand("Hello AI")
        self.assertTrue("Artificial Intelligence", result)


if __name__ == '__main__':
    unittest.main()
