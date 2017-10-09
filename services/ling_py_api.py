import nltk

sentence = "The quick brown fox jumped over the lazy river river rive quicks."


# Tokenize a sentence. turn each work AND punctuation mark into an item in a list.
def tokenize_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    print("RESULT = {}.".format(tokens))
    return tokens

tokens = tokenize_sentence(sentence)

# tokenize a sentence and identify part of speech for each token
def tag_sentence(sentence):
    tokens = tokenize_sentence(sentence)
    tagged = nltk.pos_tag(tokens)
    print("RESULT = {}.".format(tagged))
    return tagged
