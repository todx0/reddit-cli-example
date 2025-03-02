import pytest
from input_parser import InputParser

# Test cases
@pytest.mark.parametrize("input_str,expected", [
    ("https://www.reddit.com/r/xbiking/", "xbiking"),
    ("http://www.reddit.com/r/xbiking/", "xbiking"),
    ("www.reddit.com/r/xbiking/", "xbiking"),
    ("reddit.com/r/xbiking/", "xbiking"),
    ("https://reddit.com/r/xbiking/", "xbiking"),
    ("/r/xbiking/", "xbiking"),
    ("r/xbiking/", "xbiking"),
    ("xbiking", "xbiking"),
    ("https://www.reddit.com/r/xbiking/comments/123", "xbiking"),
    ("https://www.reddit.com/r/", None),
    ("https://www.reddit.com/", None),
    ("https://notreddit.com/r/test", None),
    ("invalid/url", None),
    ("", None),
    (" ", None),
    ("/r/", None),
    ("r/", None),
])
def test_extract_subreddit(input_str, expected):
    result = InputParser.extract_subreddit(input_str)
    assert result == expected, f"Failed for '{input_str}': expected '{expected}', got '{result}'"

def test_extract_subreddit_additional_cases():
    assert InputParser.extract_subreddit("r/xbiking_with_underscore") == "xbiking_with_underscore"
    assert InputParser.extract_subreddit("/r/xbiking123") == "xbiking123"
    assert InputParser.extract_subreddit("https://www.reddit.com/r/XBIKING/") == "XBIKING"
    assert InputParser.extract_subreddit("https://www.example.com") is None
    assert InputParser.extract_subreddit("not_a_subreddit!!!") is None
    assert InputParser.extract_subreddit("/r/xbiking/extra") == "xbiking"