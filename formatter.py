import argparse
from pathlib import Path
import re

from wordlist import WordList

POS = [
    'ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM',
    'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X'
]

find_pos = lambda line: [pos for pos in POS if pos in line]

def rdrformat(in_fn, wl):
    '''Extract word and tag and apply normlization to word if required'''

    word_tags = ''
    is_next_shad = False
    is_prev_tsek = True

    with open(in_fn, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            match = re.findall('(.+?)\[', lines[i])

            # detect shea in next word
            is_next_shad = False

            if i+1 < len(lines):
                next_match = re.findall('(.+?)\[', lines[i+1])
                if next_match:
                    next_word = next_match[0].rstrip()
                    if next_word == '།':
                        is_next_shad = True

            if match:
                # strip the white-spaces
                word = match[0].rstrip()

                # put tsek if next word is shea
                if is_next_shad and i != 0 and word != '།':
                    word += '་'

                # find POS of the word
                tag = find_pos(lines[i])
                tag = 'X' if not tag else tag[0]

                # check for folding word - no tsek for prev word
                if not is_prev_tsek:
                    word = '_'+word
                    is_prev_tsek = True

                # Check for Normalization - word with no tsek and not PUNCT
                if not word.endswith('་') and not tag is 'PUNCT':
                    word = wl.normalize(word)
                    is_prev_tsek = False

                word_tags += f'{word}/{tag} '

    # create goldTrain format dataset
    data_dir = Path(in_fn).parent
    with open(data_dir/'goldTrain', 'w') as f:
        f.write(word_tags)


parser = argparse.ArgumentParser()
parser.add_argument('--input_data', help='dataset name to be formatted')

if __name__ == "__main__":
    args = parser.parse_args()

    # create wordlist
    fn = Path(__file__).parent/'resources'/'wordlist'/'mgd.txt'
    wl = WordList(fns=[fn])

    # convert to RDRPOSTagger format
    rdrformat(args.input_data, wl)
