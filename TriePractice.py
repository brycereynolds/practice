# This is our trie dictionary class
class Trie:
    def __init__(self):
        self.words = 0
        self.prefixes = 0
        self.edges = {}

    def add_word(self, trie, word):
        if len(word) is 0:
            # We are considering full words == to a prefix as well
            trie.prefixes += 1
            trie.words += 1
        else:
            trie.prefixes += 1
            k = word[0]
            if k not in trie.edges:
                trie.edges[k] = Trie()
            word = word[1:]
            trie.add_word(trie.edges[k], word)

    def count_prefix(self, trie, prefix):
        if len(prefix) is 0:
            return trie.prefixes

        k = prefix[0]
        
        if k not in trie.edges:
            return 0
        else:
            prefix = prefix[1:]
            return trie.count_prefix(trie.edges[k], prefix)

    def count_words(self, trie, word):
        if len(word) is 0:
            return trie.words

        k = word[0]

        if k not in trie.edges:
            return 0
        else:
            word = word[1:]
            return trie.count_words(trie.edges[k], word)


trie = Trie()

trie.add_word(trie, "apple")
trie.add_word(trie, "app")
trie.add_word(trie, "ape")
trie.add_word(trie, "happy")
trie.add_word(trie, "happiness")

tests = {
    "apple": {"words": 1, "prefix": 1},
    "app": {"words": 1, "prefix": 2},
    "ape": {"words": 1, "prefix": 1},
    "ap": {"words": 0, "prefix": 3},
    "happy": {"words": 1, "prefix": 1},
    "ha": {"words": 0, "prefix": 2},
    "happinesss": {"words": 0, "prefix": 0},
}

for val in tests:
    words = trie.count_words(trie, val)
    prefix = trie.count_prefix(trie, val)

    if words != tests[val]['words']:
        print("ERROR word: %s expected: %s actual: %s" % (val, tests[val]['words'], words))

    if prefix != tests[val]['prefix']:
        print("ERROR prefix: %s expected: %s actual: %s" % (val, tests[val]['prefix'], prefix))
