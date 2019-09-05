#     Ready for the stuff from
#     https://towardsdatascience.com/a-machine-learning-approach-to-author-identification-of-horror-novels-from-text-snippets-3f1ef5dba634
#
#   I merged my code from the Unsupervised Learning dataset into this, and got some great results.
#
import datetime
import string
import sys

import pandas as pd
import unicodedata
from nltk.corpus import stopwords
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Import necessary libraries
from sklearn.naive_bayes import MultinomialNB

# instantiating the model with MultinomialNNB
model = MultinomialNB()

lemmatiser = WordNetLemmatizer()

# Defining a module for Text Processing
def text_process(tex):
    # 1. Removal of Punctuation Marks
    nopunct = [char for char in tex if char not in string.punctuation]
    nopunct = ''.join(nopunct)

    # 2. Lemmatisation
    a = ''
    i = 0
    for i in range(len(nopunct.split())):
        b = lemmatiser.lemmatize(nopunct.split()[i], pos="v")
        a = a + b + ' '

    #3 Removal of Stopwords
    return [word for word in a.split() if word.lower() not in stopwords.words('english')]


def print_timestamp(displaytext):
    datetime_now = str(datetime.datetime.now())
    # print("{}: In: {} {} ".format(datetime_now, sys._getframe(1).f_code.co_name, displaytext))
    print("{}".format(datetime_now))

def shoehorn_unicode_into_ascii(s):
    return unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode('utf-8', 'ignore')

def remove_punctuation(string):
    # punctuation marks
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # traverse the given string and if any punctuation
    # marks occur replace it with null
    for x in string.lower():
        if x in punctuations:
            string = string.replace(x, "")
    return string

debug = None
big_paras = []

print_timestamp('\n' * 3 + 'End')
print_timestamp('\n' * 3 + 'Begin')

corpusdir = '..\\Thinkful\\Datafiles/UnsupervisedLearningCapstone\\fiction_corpus\\'
fiction_corpus = PlaintextCorpusReader(corpusdir, '.*.txt')
documents_stat = fiction_corpus.fileids()
if debug:    print("documents_stat={} and is a {} datatype".format(documents_stat, type(documents_stat)))
documents_stat_0 = []
# documents_stat_0.append(documents_stat[0])

if debug:    print("documents_stat_0 is a {} datatype".format(type(documents_stat)))
item_num = 0

book_block = []
word_counts = {}

for book in documents_stat:
    item_num += 1

    if debug:    print("item_num={}".format(item_num))
    #    big_fiction = fiction_corpus.raw(book)
    big_fiction_words = fiction_corpus.words(book)

    if debug:    print("big_fiction is a {} datatype".format(type(big_fiction_words)))
    #    big_fiction = str(big_fiction, 'utf-8', 'ignore')
    big_fiction_len = len(big_fiction_words)
    book_items = book.split('_')
    author = book_items[0]
    book_name = book_items[3]
    wordcount1 = len(big_fiction_words)
    if debug:    print("big_fiction is words={}".format(len(big_fiction_words)))

    t_list = []
    for i in range(1, 16):
        if i == 1:
            start = 1000
            end = start + 200
        else:
            start = start + 200
            end = start + 200
        length = 100
        interblock = 40
        #         t_list.append((start, start+length))

        big_fictionwords0 = big_fiction_words
        if debug:    print("big_fictionwords0 is a {} datatype".format(type(big_fictionwords0)))

        #         print("words {} thru {} are: {}".format(2000, 3000, " ".join(big_fiction_words[2000:3000])))
        if debug:
            print("start={}, length={}".format(start, length))
        book_text = " ".join(big_fiction_words[start:end]).lower()
        book_text = remove_punctuation(book_text)
        book_text = str(shoehorn_unicode_into_ascii(str(book_text)))

        book_block.append([int(author), book_name, int(i), str(book_text)])
        if debug and i == 5:
            print("book_name={}, book_text={}".format(book_name, book_text))

if debug:
    print("book_block length is {}".format(len(book_block)))

for book_block_item in book_block:
    if debug:    print("author = {}, book={}, block={}.".format(book_block_item[0],
                                                                book_block_item[1],
                                                                book_block_item[2]))
    book_block_key = str(book_block_item[0]) + str(book_block_item[1] + str(book_block_item[2]))
    word_counts[book_block_key] = len(book_block_item[3].split(' '))

if debug:
    for book, word_counted in word_counts.items():
        print("book={}, word_count = {}".format(book, word_counted))

with open(corpusdir + 'corpus_test.TXT', 'w') as corpustext:
    for file_lines in book_block:
        corpustext.writelines(str(file_lines[0]) + ',' + str(file_lines[1]) + ',' + str(file_lines[2]) + ',' + str(
            file_lines[3] + '\n'))

if debug:
    print("there were {} words in the book {}.".format(len(big_fiction_words), book))
    print("words {} thru {} are: {}".format(2000, 3000, " ".join(big_fiction_words[2000:3000])))

df_book_blocks = pd.DataFrame(book_block, columns=['author', 'book', 'book_block', 'block_text'])
df_book_blocks['block_text_lengt'] = df_book_blocks['block_text'].apply(len)
# print("## book_block:", df_book_blocks.head(10))

if debug:
    for index, row in df_book_blocks.sample(40).iterrows():
        print( row['author'], row['book'],row['book_block'], row['block_text'])



X = df_book_blocks['block_text']
y = df_book_blocks['author']

# 80-20 splitting the dataset (80%->Training, and 20%-> Validation)
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.20, random_state=57)

# defining the bag-of-words transformer on the text-processed corpus
# i.e. text_process(0 declared in II is executed
bow_transformer = CountVectorizer(analyzer=text_process).fit(X_train)

# transforming ito Bag-of-words and hence textual data to numeric
text_bow_train = bow_transformer.transform(X_train)# ONLY TRAINING DATA

# transforming into Bag-of-Words and hece textual data to numeric
text_bow_test = bow_transformer.transform(X_test) # TEST DATA

# Training the Model
model = model.fit(text_bow_train, y_train)

# Model performance analysis
model_score_train = model.score(text_bow_train,y_train)
print("model_score_train = {:.2%} ".format(model_score_train))

# Validation Accuracy
model_score_test = model.score(text_bow_test, y_test)
print("model_score_test = {:.2%}".format(model_score_test))

print("that is all for now, Lou.")
print_timestamp('\n' * 3 + 'End')

