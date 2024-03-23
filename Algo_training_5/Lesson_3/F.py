"""F. Замена слов"""

from collections import defaultdict
from typing import Iterable

LEAF = object()


def replace_words(words: list[str], prefixes: list[str]) -> Iterable[str]:
    def make_prefix_tree() -> defaultdict:
        return defaultdict(make_prefix_tree)

    prefix_tree = make_prefix_tree()

    for prefix in prefixes:
        node = prefix_tree
        for char in prefix:
            node = node[char]
        node[LEAF] = prefix

    for word in words:
        current_node = prefix_tree
        for char in word:
            if char not in current_node:
                yield word
                break
            current_node = current_node[char]
            if LEAF in current_node:
                yield current_node[LEAF]
                break
        else:
            yield word


if __name__ == '__main__':
    prefixes = input().split()
    words = input().split()
    print(*replace_words(words, prefixes), sep=' ')
