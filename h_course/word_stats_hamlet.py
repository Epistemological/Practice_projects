import os
import pandas as pd
import numpy as np
from collections import Counter


def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

hamlets = pd.read_csv("hamlets.csv", index_col=0)

language, text = hamlets.iloc[0]



counted_text = count_words_fast(text)
word = pd.Series(list(counted_text.keys()))
count = pd.Series(list(counted_text.values()))
data = pd.concat([word, count], axis=1)
data = data.rename(columns={0: "word", 1: "count"})
data['length'] = data["word"].str.len()

for i in count:
    if count > 10:
        frequency = "frequent"
    elif 1 < count <= 10:
        frequency = "infrequent"
    elif count == 1:
        frequency = "unique"

data["frequency"] = frequency




