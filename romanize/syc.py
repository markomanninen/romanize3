#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: syc.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = False

data = OrderedDict()

# https://en.wikipedia.org/wiki/Aramaic_alphabet

# letters from ܐ to ܛ
# alef:http://en.wiktionary.org/wiki/
data['alap'] = dict(letter=[u'ܐ'], name=u'ܐ', segment='vowel', subsegment='', transliteration=u'a', order=1)
# beth:http://en.wiktionary.org/wiki/
data['beth'] = dict(letter=[u'ܒ'], name=u'ܒ', segment='consonant', subsegment='', transliteration=u'b', order=2)
# gimel:http://en.wiktionary.org/wiki/
data['gamal'] = dict(letter=[u'ܓ'], name=u'ܓ', segment='consonant', subsegment='', transliteration=u'g', order=3)
# daleth:http://en.wiktionary.org/wiki/
data['dalath'] = dict(letter=[u'ܕ'], name=u'ܕ', segment='consonant', subsegment='', transliteration=u'd', order=4)
# he:http://en.wiktionary.org/wiki/
data['he'] = dict(letter=[u'ܗ'], name=u'ܗ', segment='vowel', subsegment='', transliteration=u'e', order=5)
# vau:http://en.wikipedia.org/wiki/
data['waw'] = dict(letter=[u'ܘ'], name=u'ܘ', segment='vowel', subsegment='', transliteration=u'w', order=6)
# zayin:http://en.wiktionary.org/wiki/
data['zain'] = dict(letter=[u'ܙ'], name=u'ܙ', segment='consonant', subsegment='', transliteration=u'z', order=7)
# heth:http://en.wiktionary.org/wiki/
data['heth'] = dict(letter=[u'ܚ'], name=u'ܚ', segment='consonant', subsegment='', transliteration=u'ê', order=8)
# teth:http://en.wiktionary.org/wiki/
data['teth'] = dict(letter=[u'ܛ'], name=u'ܛ', segment='consonant', subsegment='', transliteration=u'h', order=9)

# letters from ܝ to ܨ
# yod:http://en.wiktionary.org/wiki/
data['yodh'] = dict(letter=[u'ܝ'], name=u'ܝ', segment='vowel', subsegment='', transliteration=u'i', order=10)
# kaph:http://en.wiktionary.org/wiki/
data['kap'] = dict(letter=[u'ܟ'], name=u'ܟ', segment='consonant', subsegment='', transliteration=u'k', order=11)
# lamed:http://en.wiktionary.org/wiki/
data['lamadh'] = dict(letter=[u'ܠ'], name=u'ܠ', segment='consonant', subsegment='', transliteration=u'l', order=12)
# mem:http://en.wiktionary.org/wiki/
data['mem'] = dict(letter=[u'ܡ'], name=u'ܡ', segment='consonant', subsegment='', transliteration=u'm', order=13)
# num:http://en.wiktionary.org/wiki/
data['num'] = dict(letter=[u'ܢ'], name=u'ܢ', segment='consonant', subsegment='', transliteration=u'n', order=14)
# samekh:http://en.wiktionary.org/wiki/
data['semkath'] = dict(letter=[u'ܣ'], name=u'ܣ', segment='consonant', subsegment='', transliteration=u'x', order=15)
# ayin:http://en.wiktionary.org/wiki/
data['e'] = dict(letter=[u'ܥ'], name=u'ܥ', segment='consonant', subsegment='', transliteration=u'o', order=16)
# pe:http://en.wiktionary.org/wiki/
data['pe'] = dict(letter=[u'ܦ'], name=u'ܦ', segment='consonant', subsegment='', transliteration=u'p', order=17)
# tsade:http://en.wikipedia.org/wiki/
data['sadhe'] = dict(letter=[u'ܨ'], name=u'ܨ', segment='consonant', subsegment='', transliteration=u'c', order=18)

# letters from ܩ to ܬ
# resh:http://en.wiktionary.org/wiki/
data['qop'] = dict(letter=[u'ܩ'], name=u'ܩ', segment='consonant', subsegment='', transliteration=u'q', order=19)
# shin:http://en.wiktionary.org/wiki/
data['resh'] = dict(letter=[u'ܪ'], name=u'ܪ', segment='consonant', subsegment='', transliteration=u'r', order=20)
# tau:http://en.wiktionary.org/wiki/
data['shin'] = dict(letter=[u'ܫ'], name=u'ܫ', segment='consonant', subsegment='', transliteration=u's', order=21)
# final_tsade:http://en.wiktionary.org/wiki/
data['taw'] = dict(letter=[u'ܬ'], name=u'ܬ', segment='consonant', subsegment='', transliteration=u't', order=22)
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

r = romanizer(data, has_capitals)

# collect syriaic and transliteration letters from data dictionary for preprocessing function
letters = ''.join([''.join(d['letter'])+d['transliteration'] for key, d in data.items()])
regex = re.compile('[^%s ]+' % letters)
regex2 = re.compile('[^%s\s]' % ''.join([''.join(d['letter']) for key, d in data.items()]))

def filter(string):
    """
    Preprocess string to remove all other characters but syriaic ones

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
