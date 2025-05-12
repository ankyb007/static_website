from extracttitle import extract_title
import unittest

class TestExtractTitle(unittest.TestCase):

    def test_extract_title(self):
        self.assertEqual(extract_title("#  Hello"), "Hello")

    def test_empty_string(self):
        with self.assertRaises(Exception):
            extract_title("   ")


if __name__ == "__main__":
    unittest.main()