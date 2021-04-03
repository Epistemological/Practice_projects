
def read_book(title_path):
    """Read a book and return it as a string"""
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text.replace("\n", "").replace("\r", "")
    return text

text = read_book("./Books_EngFr/Books_EngFr/English/shakespeare/Romeo and Juliet.txt")

print(len(text))

ind = text.find("What's in a name?")
print(ind)

sample_text = text[ ind: ind + 1000]
print(sample_text)


