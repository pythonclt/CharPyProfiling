import re


# Third example. Back to using a regular dict. Try out a precompiled re


def word_gen(fn):
    with open(fn, 'rb') as text:
        splitter = re.compile(r'[\s.,?;!]+')
        for line in text:
            words = splitter.split(line)
            for word in words:
                yield word.lower()


def count_words(fn):
    counts = {}
    for word in word_gen(fn):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return [(w, c) for w, c in counts.iteritems()]


def top_ten(counts):
    s = sorted(counts, key=lambda x: x[1], reverse=True)
    return s[0:10]


def bottom_ten(counts):
    s = sorted(counts, key=lambda x: x[1])
    return s[0:10]

if __name__ == '__main__':
    word_counts = count_words('pg10.txt')
    print top_ten(word_counts)
    print bottom_ten(word_counts)