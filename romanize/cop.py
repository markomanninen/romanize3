#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: cop.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = True

data = OrderedDict()

# http://en.wikipedia.org/wiki/Coptic_alphabet

# letters from ⲁ to ⲑ (1 - 9)
# alef:http://en.wiktionary.org/wiki/
data['alpha'] = dict(letter=[u'ⲁ'], name=u'ⲁ', segment='vowel', subsegment='', transliteration=u'a', order=1)
# beth:http://en.wiktionary.org/wiki/
data['beth'] = dict(letter=[u'ⲃ'], name=u'ⲃ', segment='consonant', subsegment='', transliteration=u'b', order=2)
# gimel:http://en.wiktionary.org/wiki/
data['gamma'] = dict(letter=[u'ⲅ'], name=u'ⲅ', segment='consonant', subsegment='', transliteration=u'g', order=3)
# daleth:http://en.wiktionary.org/wiki/
data['delta'] = dict(letter=[u'ⲇ'], name=u'ⲇ', segment='consonant', subsegment='', transliteration=u'd', order=4)
# he:http://en.wiktionary.org/wiki/
data['ei'] = dict(letter=[u'ⲉ'], name=u'ⲉי', segment='vowel', subsegment='', transliteration=u'e', order=5)
# vau:http://en.wikipedia.org/wiki/
data['so'] = dict(letter=[u'ⲋ'], name=u'ⲋ', segment='numeral', subsegment='', transliteration=u'w', order=6)
# zayin:http://en.wiktionary.org/wiki/
data['zeta'] = dict(letter=[u'ⲍ'], name=u'ⲍ', segment='consonant', subsegment='', transliteration=u'z', order=7)
# heth:http://en.wiktionary.org/wiki/
data['eta'] = dict(letter=[u'ⲏ'], name=u'ⲏ', segment='vowel', subsegment='', transliteration=u'ê', order=8)
# teth:http://en.wiktionary.org/wiki/
data['theta'] = dict(letter=[u'ⲑ'], name=u'ⲑ', segment='consonant', subsegment='', transliteration=u'h', order=9)

# letters from י to ϥ (10 - 90)
# yod:http://en.wiktionary.org/wiki/
data['yota'] = dict(letter=[u'ⲓ'], name=u'ⲓ', segment='vowel', subsegment='', transliteration=u'i', order=10)
# kaph:http://en.wiktionary.org/wiki/
data['kappa'] = dict(letter=[u'ⲕ'], name=u'ⲕ', segment='consonant', subsegment='', transliteration=u'k', order=11)
# lamed:http://en.wiktionary.org/wiki/
data['lambda'] = dict(letter=[u'ⲗ'], name=u'ⲗ', segment='consonant', subsegment='', transliteration=u'l', order=12)
# mem:http://en.wiktionary.org/wiki/
data['me'] = dict(letter=[u'ⲙ'], name=u'ⲙ', segment='consonant', subsegment='', transliteration=u'm', order=13)
# num:http://en.wiktionary.org/wiki/
data['ne'] = dict(letter=[u'ⲛ'], name=u'ⲛ', segment='consonant', subsegment='', transliteration=u'n', order=14)
# samekh:http://en.wiktionary.org/wiki/
data['eksi'] = dict(letter=[u'ⲝ'], name=u'ⲝ', segment='consonant', subsegment='', transliteration=u'x', order=15)
# ayin:http://en.wiktionary.org/wiki/
data['o'] = dict(letter=[u'ⲟ'], name=u'ⲟ', segment='consonant', subsegment='', transliteration=u'o', order=16)
# pe:http://en.wiktionary.org/wiki/
data['pi'] = dict(letter=[u'ⲡ'], name=u'ⲡ', segment='consonant', subsegment='', transliteration=u'p', order=17)
# tsade:http://en.wikipedia.org/wiki/
data['fay'] = dict(letter=[u'ϥ'], name=u'ϥ', segment='numeral', subsegment='', transliteration=u'q', order=18)

# letters from ⲣ to ⳁ (100 - 900)
# resh:http://en.wiktionary.org/wiki/
data['ro'] = dict(letter=[u'ⲣ'], name=u'ⲣ', segment='consonant', subsegment='', transliteration=u'r', order=19)
# shin:http://en.wiktionary.org/wiki/
data['sima'] = dict(letter=[u'ⲥ'], name=u'ⲥ', segment='consonant', subsegment='', transliteration=u's', order=20)
# tau:http://en.wiktionary.org/wiki/
data['taw'] = dict(letter=[u'ⲧ'], name=u'ⲧו', segment='consonant', subsegment='', transliteration=u't', order=21)
# final_tsade:http://en.wiktionary.org/wiki/Tsade
data['epsilon'] = dict(letter=[u'ⲩ'], name=u'ⲩ', segment='vowel', subsegment='', transliteration=u'u', order=22)
# final_kaph:http://en.wiktionary.org/wiki/
data['fi'] = dict(letter=[u'ⲫ'], name=u'ⲫ', segment='consonant', subsegment='', transliteration=u'f', order=23)
# final_mem, chi:http://en.wiktionⲣary.org/wiki/
data['khe'] = dict(letter=[u'ⲭ'], name=u'ⲭ', segment='consonant', subsegment='', transliteration=u'c', order=24)
# final_nun:http://en.wiktionary.org/wiki/
data['epsi'] = dict(letter=[u'ⲯ'], name=u'ⲯ', segment='consonant', subsegment='', transliteration=u'y', order=25)
# final_pe:http://en.wiktionary.org/wiki/
data['ou'] = dict(letter=[u'ⲱ'], name=u'ⲱ', segment='vowel', subsegment='', transliteration=u'ô', order=26)
# final_tsade:http://en.wiktionary.org/wiki/Tsade
data['nine'] = dict(letter=[u'ⳁ'], name=u'ⳁ', segment='numeral', subsegment='', transliteration=u'j', order=27)

r = romanizer(data, False)

# collect coptic and transliteration letters from data dictionary for preprocessing function
letters = ''.join([''.join(d['letter'])+d['transliteration']+''.join(d['letter']).upper()+d['transliteration'].upper() for key, d in data.items()])
regex = re.compile('[^%s ]+' % letters)
regex2 = re.compile('[^%s\s]' % ''.join([''.join(d['letter'])+''.join(d['letter']).upper() for key, d in data.items()]))

r = romanizer(data)

def filter(string):
    """
    Preprocess string to remove all other characters but coptic ones

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
