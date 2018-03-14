"""Retrieve and print words from a URL.

Usage:
    from cmd line:
        python3 words.py <URL>

    from REPL:
        >>> from pymodules import (fetch_words_from_url, print_items,main)
        >>> main('http://sixty-north.com/c/t.txt')
"""

import sys
from urllib.request import urlopen


def fetch_words_from_url(url):
    '''
    fetches list of sentences from a url

    :Args
        url: URL of utf-8 text document

    :return:
        List of sentences containing words from documents
    '''
    with urlopen(url) as url_response:
        return [line.decode("utf-8").split() for line in url_response]


def print_items(items):
    """Print items one per line.

    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words_from_url(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
