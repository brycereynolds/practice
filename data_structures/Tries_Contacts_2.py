class Trie:
    def __init__(self):
        self._edges = {}
        self._words = 0
        self._partials = 0

    def add(self, word):
        return self._add(self, word)

    def find(self, word):
        return self._find_word(self, word)

    def find_partial(self, partial):
        return self._find_partial(self, partial)

    def _add(self, trie, word):
        if len(word) == 0:
            trie._words += 1
            trie._partials += 1
        else:
            trie._partials += 1
            k = word[0]

            if k not in trie._edges:
                trie._edges[k] = Trie()

            trie._edges[k].add(word[1:])

    def _find_word(self, trie, word):
        if len(word) == 0:
            return trie._words
        else:
            k = word[0]
            if k not in trie._edges:
                return 0
            return trie._edges[k].find(word[1:])

    def _find_partial(self, trie, partial):
        if len(partial) == 0:
            return trie._partials
        else:
            k = partial[0]
            if k not in trie._edges:
                return 0
            return trie._edges[k].find_partial(partial[1:])



contacts = Trie()

contacts.add('hack')
contacts.add('hackerrank')

print(contacts.find('hac'))
print(contacts.find_partial('hac'))
print(contacts.find('hack'))
print(contacts.find_partial('hack'))