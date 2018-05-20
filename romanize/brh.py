#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: brh.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = False

data = OrderedDict()

# https://en.wikipedia.org/wiki/Aramaic_alphabet
# https://en.wikipedia.org/wiki/Brahmi_script

# letters from 𑀅 to 𑀣
# alef:http://en.wiktionary.org/wiki/
data['a'] = dict(letter=[u'𑀅'], name=u'𑀅', segment='vowel', subsegment='', transliteration=u'a', order=1)
# beth:http://en.wiktionary.org/wiki/
data['ba'] = dict(letter=[u'𑀩'], name=u'𑀩', segment='consonant', subsegment='', transliteration=u'b', order=2)
# gimel:http://en.wiktionary.org/wiki/
data['ga'] = dict(letter=[u'𑀕'], name=u'𑀕', segment='consonant', subsegment='', transliteration=u'g', order=3)
# daleth:http://en.wiktionary.org/wiki/
data['dha'] = dict(letter=[u'𑀥'], name=u'𑀥', segment='consonant', subsegment='', transliteration=u'd', order=4)
# he:http://en.wiktionary.org/wiki/
data['ha'] = dict(letter=[u'𑀳'], name=u'𑀳', segment='vowel', subsegment='', transliteration=u'e', order=5)
# vau:http://en.wikipedia.org/wiki/
data['va'] = dict(letter=[u'𑀯'], name=u'𑀯', segment='vowel', subsegment='', transliteration=u'w', order=6)
# zayin:http://en.wiktionary.org/wiki/
data['ja'] = dict(letter=[u'𑀚'], name=u'𑀚', segment='consonant', subsegment='', transliteration=u'z', order=7)
# heth:http://en.wiktionary.org/wiki/
data['gha'] = dict(letter=[u'𑀖'], name=u'𑀖', segment='consonant', subsegment='', transliteration=u'ê', order=8)
# teth:http://en.wiktionary.org/wiki/
data['tha'] = dict(letter=[u'𑀣'], name=u'𑀣', segment='consonant', subsegment='', transliteration=u'h', order=9)

# letters from 𑀬 to 𑀲
# yod:http://en.wiktionary.org/wiki/
data['ya'] = dict(letter=[u'𑀬'], name=u'𑀬', segment='vowel', subsegment='', transliteration=u'i', order=10)
# kaph:http://en.wiktionary.org/wiki/
data['ka'] = dict(letter=[u'𑀓'], name=u'𑀓', segment='consonant', subsegment='', transliteration=u'k', order=11)
# lamed:http://en.wiktionary.org/wiki/
data['la'] = dict(letter=[u'𑀮'], name=u'𑀮', segment='consonant', subsegment='', transliteration=u'l', order=12)
# mem:http://en.wiktionary.org/wiki/
data['ma'] = dict(letter=[u'𑀫'], name=u'𑀫', segment='consonant', subsegment='', transliteration=u'm', order=13)
# num:http://en.wiktionary.org/wiki/
data['na'] = dict(letter=[u'𑀦'], name=u'𑀦', segment='consonant', subsegment='', transliteration=u'n', order=14)
# samekh:http://en.wiktionary.org/wiki/
data['sha'] = dict(letter=[u'𑀰'], name=u'𑀰', segment='consonant', subsegment='', transliteration=u'x', order=15)
# ayin:http://en.wiktionary.org/wiki/
data['e'] = dict(letter=[u'𑀏'], name=u'𑀏', segment='vowel', subsegment='', transliteration=u'o', order=16)
# pe:http://en.wiktionary.org/wiki/
data['pa'] = dict(letter=[u'𑀧'], name=u'𑀧', segment='consonant', subsegment='', transliteration=u'p', order=17)
# tsade:http://en.wikipedia.org/wiki/
data['sa'] = dict(letter=[u'𑀲'], name=u'𑀲', segment='consonant', subsegment='', transliteration=u'c', order=18)

# letters from 𑀔 to 𑀢
# resh:http://en.wiktionary.org/wiki/
data['kha'] = dict(letter=[u'𑀔'], name=u'𑀔', segment='consonant', subsegment='', transliteration=u'q', order=19)
# shin:http://en.wiktionary.org/wiki/
data['ra'] = dict(letter=[u'𑀭'], name=u'𑀭', segment='consonant', subsegment='', transliteration=u'r', order=20)
# tau:http://en.wiktionary.org/wiki/
data['ssa'] = dict(letter=[u'𑀱'], name=u'𑀱', segment='consonant', subsegment='', transliteration=u's', order=21)
# final_tsade:http://en.wiktionary.org/wiki/
data['ta'] = dict(letter=[u'𑀢'], name=u'𑀢', segment='consonant', subsegment='', transliteration=u't', order=22)
# final_kaph:http://en.wiktionary.org/wiki/
#data['final_kap'] = dict(letter=[u'ⲫ'], name=u'ⲫ', segment='consonant', subsegment='', transliteration=u'K', order=23)
# final_mem, chi:http://en.wiktionⲣary.org/wiki/
#data['final_mem'] = dict(letter=[u'ⲭ'], name=u'ⲭ', segment='consonant', subsegment='', transliteration=u'M', order=24)
# final_nun:http://en.wiktionary.org/wiki/
#data['final_nun'] = dict(letter=[u'ⲯ'], name=u'ⲯ', segment='consonant', subsegment='', transliteration=u'N', order=25)
# final_pe:http://en.wiktionary.org/wiki/
#data['final_pe'] = dict(letter=[u'ⲱ'], name=u'ⲱ', segment='consonant', subsegment='', transliteration=u'P', order=26)
# final_tsade:http://en.wiktionary.org/wiki/
#data['final_sadhe'] = dict(letter=[u'ⳁ'], name=u'ⳁ', segment='consonant', subsegment='', transliteration=u'Y', order=27)

r = romanizer(data, False)

# collect brahmic and transliteration letters from data dictionary for preprocessing function
letters = ''.join([''.join(d['letter'])+d['transliteration'] for key, d in data.items()])
regex = re.compile('[^%s ]+' % letters)
regex2 = re.compile('[^%s\s]' % ''.join([''.join(d['letter']) for key, d in data.items()]))

r = romanizer(data)

def filter(string):
    """
    Preprocess string to remove all other characters but brahmic ones

    :param string:
    :return:
    """
    # remove all unwanted characters
    return regex2.sub(' ', string)

def preprocess(string):
    """
    Preprocess string to transform all diacritics and remove other special characters

    :param string:
    :return:
    """
    return regex.sub('', string)

def convert(string, sanitize=False):
    """
    Swap characters from script to transliterated version and vice versa.
    Optionally sanitize string by using preprocess function.

    :param sanitize:
    :param string:
    :return:
    """
    return r.convert(string, (preprocess if sanitize else False))
