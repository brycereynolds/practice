class Trie:
    __slots__ = 'preffixes', 'edges'
    def __init__(self):
        self.preffixes = 0
        self.edges = {}

    def add(self, trie, word):
        if len(word) is 0:
            trie.preffixes += 1
        else:
            trie.preffixes += 1
            k = word[0]
            if k not in trie.edges:
                trie.edges[k] = Trie()

            trie.add(trie.edges[k], word[1:])

    def find_partial(self, trie, partial):
        if len(partial) is 0:
            return trie.preffixes

        k = partial[0]

        if k not in trie.edges:
            return 0
        else:
            return trie.find_partial(trie.edges[k], partial[1:])

a = Trie()
a.add(a, "hack")
a.add(a, "hackerrank")

print("PARTIALS %s" % a.find_partial(a, "hac"))
print("PARTIALS %s" % a.find_partial(a, "hak"))