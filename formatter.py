import argparse
import random
import re

POS = [
    'ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM',
    'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X'
]

find_pos = lambda line: [pos for pos in POS if pos in line]

def rdrformat(in_fn):

    # Extract word/tag
    word_tags = []
    with open(in_fn, 'r') as f:
        count = 0
        for line in f.readlines():
            match = re.findall('(.+?)\[', line)
            if match:
                tg = find_pos(line)
                tg = 'X' if not tg else tg[0]
                word_tags.append('{}/{}'.format(match[0].rstrip(), tg))

    # shuffle the dataset
    random.seed(42)
    random.shuffle(word_tags)

    # split the dataset to train and test dataset
    split = int(0.9 * len(word_tags))
    train_set = word_tags[:split]
    test_set = word_tags[split:]

    # save the train and test dataset
    with open('goldTrain', 'w') as f:
        f.write(' '.join(train_set))

    with open('goldTest', 'w') as f:
        f.write(' '.join(test_set))


parser = argparse.ArgumentParser()
parser.add_argument('--input_data', help='dataset name to be formatted')

if __name__ == "__main__":
    args = parser.parse_args()
    rdrformat(args.input_data)
