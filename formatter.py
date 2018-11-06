import argparse
import re
from pathlib import Path

POS = [
    'ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM',
    'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X'
]

find_pos = lambda line: [pos for pos in POS if pos in line]

def rdrformat(in_fn):

    # Extract word/tag
    word_tags = ''
    with open(in_fn, 'r') as f:
        count = 0
        for line in f.readlines():
            match = re.findall('(.+?)\[', line)
            if match:
                tg = find_pos(line)
                tg = 'X' if not tg else tg[0]
                word_tags += f'{match[0].rstrip()}/{tg} '

    # save the dataset
    data_dir = Path(in_fn).parent
    with open(data_dir/'goldTrain', 'w') as f:
        f.write(word_tags)


parser = argparse.ArgumentParser()
parser.add_argument('--input_data', help='dataset name to be formatted')

if __name__ == "__main__":
    args = parser.parse_args()
    rdrformat(args.input_data)
