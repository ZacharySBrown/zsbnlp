from collections import Counter, defaultdict
from itertools import chain, islice
from zsbnlp.core import DEFAULT_TOKENIZER
import spacy

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    "https://docs.python.org/release/2.3.5/lib/itertools-example.html "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result    
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def co_occurrance(texts, window_size=1, tokenizer=DEFAULT_TOKENIZER):
    tokenized = [tokenizer(text) for text in texts]
    pairs = [window(toks, window_size+1) for toks in tokenized]
    return list(pairs)
    



