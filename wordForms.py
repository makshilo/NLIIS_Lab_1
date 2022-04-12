import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from spellchecker import SpellChecker
from nltk.corpus import words


# read text from file
def read_text(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    return text


def text_preprocessing(raw_text):
    raw_text = raw_text.lower()  # to lowercase

    raw_text = raw_text.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))  # remove punctuation

    word_tokenize(raw_text)  # tokenize

    raw_text = [word for word in word_tokenize(raw_text) if
                not any(char.isdigit() for char in word)]  # remove tokens with numbers

    spell = SpellChecker()  # correct misspelled words
    raw_text = [spell.correction(word) for word in raw_text]

    return raw_text


# add pos tags to word
def add_pos_tag(text):
    pos_tagged = nltk.pos_tag(text)
    return pos_tagged


# get pos tag
def get_pos_tag(word):
    return nltk.pos_tag([word])


# get nouns
def get_nouns(pos_tagged):
    nouns = []
    for word, pos in pos_tagged:
        if pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS':
            nouns.append(word)
    return nouns


# get verbs
def get_verbs(pos_tagged):
    verbs = []
    for word, pos in pos_tagged:
        if pos == 'VB' or pos == 'VBD' or pos == 'VBG' or pos == 'VBN' or pos == 'VBP' or pos == 'VBZ':
            verbs.append(word)
    return verbs


# get adjectives
def get_adjectives(pos_tagged):
    adjectives = []
    for word, pos in pos_tagged:
        if pos == 'JJ' or pos == 'JJR' or pos == 'JJS':
            adjectives.append(word)
    return adjectives


# get adverbs
def get_adverbs(pos_tagged):
    adverbs = []
    for word, pos in pos_tagged:
        if pos == 'RB' or pos == 'RBR' or pos == 'RBS':
            adverbs.append(word)
    return adverbs


def lemmatize_text(preprocessed_text):
    nouns = get_nouns(preprocessed_text)
    verbs = get_verbs(preprocessed_text)
    adjectives = get_adjectives(preprocessed_text)
    adverbs = get_adverbs(preprocessed_text)

    # lemmatize by pos tags
    lemmatizer = WordNetLemmatizer()
    nouns = [lemmatizer.lemmatize(word, pos='n') for word in nouns]
    verbs = [lemmatizer.lemmatize(word, pos='v') for word in verbs]
    adjectives = [lemmatizer.lemmatize(word, pos='a') for word in adjectives]
    adverbs = [lemmatizer.lemmatize(word, pos='r') for word in adverbs]

    return nouns + verbs + adjectives + adverbs  # unite into text


# # lemmatize word by pos tag
# def lemmatize_word(word):
#     pos_tag = get_pos_tag(word)[0][1]
#     if pos_tag == 'NN' or pos_tag == 'NNS' or pos_tag == 'NNP' or pos_tag == 'NNPS':
#         return WordNetLemmatizer().lemmatize(word, pos='n')
#     elif pos_tag == 'VB' or pos_tag == 'VBD' or pos_tag == 'VBG' or pos_tag == 'VBN' or pos_tag == 'VBP' or pos_tag == 'VBZ':
#         return WordNetLemmatizer().lemmatize(word, pos='v')
#     elif pos_tag == 'JJ' or pos_tag == 'JJR' or pos_tag == 'JJS':
#         return WordNetLemmatizer().lemmatize(word, pos='a')
#     elif pos_tag == 'RB' or pos_tag == 'RBR' or pos_tag == 'RBS':
#         return WordNetLemmatizer().lemmatize(word, pos='r')
#     else:
#         return word


general_prefixes = ['anti', 'auto', 'mid', 'post', 'pre', 'super', 'sub', 'de', 'over', 'under', 're', 'en', 'em',
                    'extra', 'inter']
negative_prefixes = ['un', 'im', 'in', 'il', 'ir', 'dis', 'mis']


def get_prefixes(word, prefixes):
    correct_prefixes = []
    for prefix in prefixes:
        if check_word_in_dictionary(add_prefix(word, prefix)):
            correct_prefixes.append(prefix)
    return correct_prefixes


def add_prefix(word, prefix):
    new_word = ''
    new_word += prefix + word
    return new_word


noun_suffixes = ['er', 'or', 'an', 'ian', 'ist', 'ant', 'ent', 'ee', 'ess', 'ity', 'ance', 'ence', 'ancy', 'ency',
                 'ism', 'hood', 'ure', 'ion', 'tion', 'sion', 'dom', 'ment', 'ness', 'ship', 'th']
adjective_suffixes = ['ful', 'less', 'able', 'ous', 'y', 'al', 'ar', 'ant', 'ent', 'ary', 'ory', 'ic', 'ive', 'ish',
                      'long']
verb_suffixes = ['ate', 'ify', 'fy', 'ise', 'ize', 'en', 'ish']
adverb_suffixes = ['ly', 'wise', 'ward', 'wards']


def get_suffixes(word, suffixes):
    correct_suffixes = []
    for suffix in suffixes:
        if check_word_in_dictionary(add_suffix(word, suffix)):
            correct_suffixes.append(suffix)
    return correct_suffixes


def add_suffix(word, suffix):
    new_word = ''
    new_word += word + suffix
    return new_word


def check_word_in_dictionary(word):
    if word in words.words():
        return True


# text = read_text('input.txt')
# text = text_preprocessing(text)
# text = add_pos_tag(text)
# text = lemmatize_text(text)
# text = list(set(text))
# text.sort()
#
#
# processed_words = []
# for word in text:
#     processed_words.append(ProcessedWord(word, get_pos_tag(word)[0][1],
#                                          get_prefixes(word, general_prefixes) + get_prefixes(word, negative_prefixes),
#                                          get_suffixes(word, noun_suffixes) + get_suffixes(word, adjective_suffixes) +
#                                          get_suffixes(word, verb_suffixes) + get_suffixes(word, adverb_suffixes)))
#
#
# # print processed words
# for word in processed_words:
#     print(word)
