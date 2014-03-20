import re
from collections import Counter


# Second example, using the Counter class from collections. I assumed this
# would be the faster way of doing things. It seems that it isn't.

def count_words(fn):
    counts = Counter()
    with open(fn, 'rb') as text:
        for line in text:
            words = re.split(r'[\s.,]+', line)
            counts.update([x for x in words if x != ''])

    return counts


if __name__ == '__main__':
    word_counts = count_words('pg10.txt')
    print word_counts.most_common(20)
