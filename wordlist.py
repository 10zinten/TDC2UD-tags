from pathlib import Path

class WordList:

    def __init__(self, fns):
        self.words = []
        self.fns = fns
        self._build_wordlist()
        self.follower = 'འ'    # only one case for folded
        self.tsek = '་'

    def _build_wordlist(self):
        for fn in self.fns:
            with open(fn, 'r') as f:
                words = f.read().split('\n')
                self.words.extend(words)

    def get_wordlist(self):
        return self.words

    def normalize(self, word):

        # check with the follower
        new_word = word+self.follower
        if new_word in self.words:
            return new_word+self.tsek

        # check without follower
        if word in self.words:
            return word+self.tsek

        # word not in the word list
        return word+self.tsek


if __name__ == '__main__':
    fn = Path(__file__).parent/'resources'/'wordlist'/'mgd.txt'
    wl = WordList(fns=[fn])
    assert wl.normalize('ཀུན་དག') == 'ཀུན་དགའ་'
