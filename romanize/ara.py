#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: ara.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = False

data = OrderedDict()

# https://en.wikipedia.org/wiki/Aramaic_alphabet
# https://en.wikipedia.org/wiki/Abjad_numerals

# letters from ا to ط
# https://en.wikipedia.org/wiki/%D8%A7
data['alif'] = dict(letter=[u'ا'], name=u'ا', segment='vowel', subsegment='', transliteration=u'a', order=1)
# https://en.wikipedia.org/wiki/%D8%A8
data['ba'] = dict(letter=[u'ب'], name=u'ب', segment='consonant', subsegment='', transliteration=u'b', order=2)
# https://en.wikipedia.org/wiki/%D8%AC
data['jim'] = dict(letter=[u'ج'], name=u'ج', segment='consonant', subsegment='', transliteration=u'j', order=3)
# https://en.wikipedia.org/wiki/%D8%AF
data['dal'] = dict(letter=[u'د'], name=u'د', segment='consonant', subsegment='', transliteration=u'd', order=4)
# https://en.wikipedia.org/wiki/%D9%87
data['ha'] = dict(letter=[u'ه'], name=u'ه', segment='vowel', subsegment='', transliteration=u'h', order=5)
# https://en.wikipedia.org/wiki/%D9%88
data['waw'] = dict(letter=[u'و'], name=u'و', segment='vowel', subsegment='', transliteration=u'w', order=6)
# https://en.wikipedia.org/wiki/%D8%B2
data['zayn'] = dict(letter=[u'ز'], name=u'ز', segment='consonant', subsegment='', transliteration=u'z', order=7)
# https://en.wikipedia.org/wiki/%D8%AD
data['ha'] = dict(letter=[u'ح'], name=u'ح', segment='consonant', subsegment='', transliteration=u'ḥ', order=8)
# https://en.wikipedia.org/wiki/%D8%B7
data['ta'] = dict(letter=[u'ط'], name=u'ط', segment='consonant', subsegment='', transliteration=u'ṭ', order=9)

# letters from ى to ص
# https://en.wikipedia.org/wiki/%D9%89
data['ya'] = dict(letter=[u'ى'], name=u'ى', segment='vowel', subsegment='', transliteration=u'i', order=10)
# https://en.wikipedia.org/wiki/%D9%83
data['kaf'] = dict(letter=[u'ك'], name=u'ك', segment='consonant', subsegment='', transliteration=u'k', order=11)
# https://en.wikipedia.org/wiki/%D9%84
data['lam'] = dict(letter=[u'ل'], name=u'ل', segment='consonant', subsegment='', transliteration=u'l', order=12)
# https://en.wikipedia.org/wiki/%D9%85
data['mim'] = dict(letter=[u'م'], name=u'م', segment='consonant', subsegment='', transliteration=u'm', order=13)
# https://en.wikipedia.org/wiki/%D9%86
data['nun'] = dict(letter=[u'ن'], name=u'ن', segment='consonant', subsegment='', transliteration=u'n', order=14)
# https://en.wikipedia.org/wiki/%D8%B3
data['sin'] = dict(letter=[u'س'], name=u'س', segment='consonant', subsegment='', transliteration=u's', order=15)
# https://en.wikipedia.org/wiki/%D8%B9
data['ayn'] = dict(letter=[u'ع'], name=u'ع', segment='consonant', subsegment='', transliteration=u'ʻ', order=16)
# https://en.wikipedia.org/wiki/%D9%81
data['fa'] = dict(letter=[u'ف'], name=u'ف', segment='consonant', subsegment='', transliteration=u'f', order=17)
# https://en.wikipedia.org/wiki/%D8%B5
data['sad'] = dict(letter=[u'ص'], name=u'ص', segment='consonant', subsegment='', transliteration=u'ṣ', order=18)

# letters from ق to غ
# https://en.wikipedia.org/wiki/%D9%82
data['qaf'] = dict(letter=[u'ق'], name=u'ق', segment='consonant', subsegment='', transliteration=u'q', order=19)
# https://en.wikipedia.org/wiki/%D8%B1
data['ra'] = dict(letter=[u'ر'], name=u'ر', segment='consonant', subsegment='', transliteration=u'r', order=20)
# https://en.wikipedia.org/wiki/%D8%B4
data['shin'] = dict(letter=[u'ش'], name=u'ش', segment='consonant', subsegment='', transliteration=u'š', order=21)
# https://en.wikipedia.org/wiki/%D8%AA
data['ta'] = dict(letter=[u'ت'], name=u'ت', segment='consonant', subsegment='', transliteration=u't', order=22)
# https://en.wikipedia.org/wiki/%D8%AB
data['tha'] = dict(letter=[u'ث'], name=u'ث', segment='consonant', subsegment='', transliteration=u'ṯ', order=23)
# https://en.wikipedia.org/wiki/%D8%AE
data['kha'] = dict(letter=[u'خ'], name=u'خ', segment='consonant', subsegment='', transliteration=u'ḵ', order=24)
# https://en.wikipedia.org/wiki/%D8%B0
data['dhal'] = dict(letter=[u'ذ'], name=u'ذ', segment='consonant', subsegment='', transliteration=u'ḏ', order=25)
# https://en.wikipedia.org/wiki/%D8%B6
data['dad'] = dict(letter=[u'ض'], name=u'ض', segment='consonant', subsegment='', transliteration=u'ḍ', order=26)
# https://en.wikipedia.org/wiki/%D8%B8
data['za'] = dict(letter=[u'ظ'], name=u'ظ', segment='consonant', subsegment='', transliteration=u'ẓ', order=27)
# https://en.wikipedia.org/wiki/%D8%BA
data['ghayn'] = dict(letter=[u'غ'], name=u'غ', segment='consonant', subsegment='', transliteration=u'g', order=28)

r = romanizer(data, False)

# collect arabic and transliteration letters from data dictionary for preprocessing function
letters = ''.join([''.join(d['letter'])+d['transliteration'] for key, d in data.items()])
regex = re.compile('[^%s ]+' % letters)
regex2 = re.compile('[^%s\s]' % ''.join([''.join(d['letter']) for key, d in data.items()]))

r = romanizer(data)

def filter(string):
    """
    Preprocess string to remove all other characters but arabic ones

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
