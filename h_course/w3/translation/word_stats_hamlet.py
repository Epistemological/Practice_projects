import os
import pandas as pd
import numpy as np
from collections import Counter

### Exercise 1

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

### Exercise 2

language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)
word = pd.Series(list(counted_text.keys()))
count = pd.Series(list(counted_text.values()))
data = pd.concat([word, count], axis=1)
data = data.rename(columns={0: "word", 1: "count"})
data['length'] = data["word"].str.len()

### Exercise 3

frequency = []
for i in count:
    if i > 10:
        i = "frequent"
        frequency.append(i)
    elif 1 < i <= 10:
        i = "infrequent"
        frequency.append(i)
    elif i == 1:
        i = "unique"
        frequency.append(i)

data["frequency"] = pd.Series(frequency)

count_unique_words = data["frequency"].value_counts()
### Exercise 4

frequency_list = ["frequent", "infrequent", "unique"]
mean_word_length = data.groupby("frequency")["length"].mean()
sub_data = pd.DataFrame({"language" : language, "frequency": frequency_list, "mean_word_length": mean_word_length, "num_words": count_unique_words})

### Exercise 5

def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })

    data.loc[data["count"] > 10, "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1, "frequency"] = "unique"

    data["length"] = data["word"].apply(len)

    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent", "infrequent", "unique"],
        "mean_word_length": data.groupby(by="frequency")["length"].mean(),
        "num_words": data.groupby(by="frequency").size()
    })

    return (sub_data)

grouped_data = pd.DataFrame()

for i in range(hamlets.shape[0]):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    grouped_data = grouped_data.append(sub_data)
print(grouped_data)

### Exercise 6

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")

plt.show()















