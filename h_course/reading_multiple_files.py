import os

os.chdir("C:/Users/Dennis Besseling/PycharmProjects/work_projects/h_course/w3/translation")
book_dir = "./Books"

os.listdir(book_dir)

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + author)
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))