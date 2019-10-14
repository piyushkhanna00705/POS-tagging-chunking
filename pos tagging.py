# -*- coding: utf-8 -*-


"""TAGGING"""

import nltk

sentence = "My name is Jocelyn"
token = nltk.word_tokenize(sentence)

nltk.pos_tag(token)


"""CHUNKING"""

sentence="Tony Stark snapped the powerful gauntlet to save the huge universe"

grammar = ('''
    NP: {<DT>?<JJ>*<NN>} # NP
    ''')

chunkParser = nltk.RegexpParser(grammar)
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))

tree=chunkParser.parse(tagged)

tree.draw()