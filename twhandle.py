import os
import sys
from itertools import imap
from itertools import ifilter
from itertools import combinations_with_replacement
import string

import grequests


bulk_size = 100
available_url = "https://twitter.com/users/username_available"
tried_file = "tried.txt"
available_file = "available.txt"


def get_bulks(iterable):
    bulk = []
    for i, handle in enumerate(iterable):
        bulk.append(handle)
        if (i + 1) % bulk_size == 0:
            yield set(bulk)
            bulk = []
    if bulk:
        yield set(bulk)


class Finder(object):

    def __init__(self):
        self.tried = set()
        if os.path.exists(tried_file):
            with open(tried_file, "r") as f:
                self.tried = set(h.strip() for h in f.readlines())
        self.tried_file = open(tried_file, "a")
        self.available_file = open(available_file, "a")

    def add_trieds(self, handles):
        self.tried |= handles
        self.tried_file.write("\n".join(handles) + "\n")
        self.tried_file.flush()

    def add_available(self, handle):
        print "adding available", handle
        self.available_file.write(handle + "\n")
        self.available_file.flush()

    def bulk_filter(self, bulk):
        untried = bulk - self.tried
        if not untried:
            return set()
        print "trying", ", ".join(untried)
        rs = []
        headers = {"Accept-Language": "en-us"}
        taken = set()
        for handle in untried:
            data = {"username": handle}
            rs.append(grequests.get(available_url, data=data, headers=headers))
        responses = grequests.map(rs)
        for response in responses:
            available = False
            try:
                available = response.json["desc"] == "Available!"
            except:
                available = False
            handle = response.request.data["username"]
            if not available:
                taken.add(handle)
        self.add_trieds(untried)
        return untried - taken

    def find_letters(self, letters, length):
        with_replacement = combinations_with_replacement(letters, length)
        strings = imap(lambda x: "".join(x), with_replacement)
        self._find(strings)

    def find_words(self, max_length):
        with open("words.txt", "r") as f:
            all_words = [h.strip() for h in f.readlines()]
        short_words = ifilter(lambda w: len(w) <= max_length, all_words)
        lowercase_words = imap(lambda w: w.lower(), short_words)
        self._find(lowercase_words)

    def _find(self, iterable):
        for bulk in imap(self.bulk_filter, get_bulks(iterable)):
            for handle in bulk:
                self.add_available(handle)


def main():
    letters = sys.argv[1]
    length = int(sys.argv[2])
    finder = Finder()
    if letters == "ALL":
        letters = string.lowercase
        finder.find_letters(letters, length)
    elif letters == "WORDS":
        finder.find_words(length)
    else:
        finder.find_letters(letters, length)


if __name__ == "__main__":
    main()
