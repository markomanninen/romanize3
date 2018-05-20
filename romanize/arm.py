#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: arm.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = False

data = OrderedDict()

# https://en.wikipedia.org/wiki/Aramaic_alphabet

# letters from 𐡀 to 𐡈
# alef:http://en.wiktionary.org/wiki/
data['alap'] = dict(letter=[u'𐡀'], name=u'𐡀', segment='vowel', subsegment='', transliteration=u'a', order=1)
# beth:http://en.wiktionary.org/wiki/
data['beth'] = dict(letter=[u'𐡁‬'], name=u'𐡁‬', segment='consonant', subsegment='', transliteration=u'b', order=2)
# gimel:http://en.wiktionary.org/wiki/
data['gamal'] = dict(letter=[u'𐡂'], name=u'𐡂', segment='consonant', subsegment='', transliteration=u'g', order=3)
# daleth:http://en.wiktionary.org/wiki/
data['dalath'] = dict(letter=[u'𐡃‬'], name=u'𐡃‬', segment='consonant', subsegment='', transliteration=u'd', order=4)
# he:http://en.wiktionary.org/wiki/
data['he'] = dict(letter=[u'𐡄'], name=u'𐡄', segment='vowel', subsegment='', transliteration=u'h', order=5)
# vau:http://en.wikipedia.org/wiki/
data['waw'] = dict(letter=[u'𐡅‬'], name=u'𐡅‬', segment='vowel', subsegment='', transliteration=u'w', order=6)
# zayin:http://en.wiktionary.org/wiki/
data['zain'] = dict(letter=[u'𐡆‬'], name=u'𐡆‬', segment='consonant', subsegment='', transliteration=u'z', order=7)
# heth:http://en.wiktionary.org/wiki/
data['heth'] = dict(letter=[u'𐡇‬'], name=u'𐡇‬', segment='consonant', subsegment='', transliteration=u'ḥ', order=8)
# teth:http://en.wiktionary.org/wiki/
data['teth'] = dict(letter=[u'𐡈'], name=u'𐡈', segment='consonant', subsegment='', transliteration=u'ṭ', order=9)

# letters from 𐡉 to 𐡑‬
# yod:http://en.wiktionary.org/wiki/
data['yodh'] = dict(letter=[u'𐡉'], name=u'𐡉', segment='vowel', subsegment='', transliteration=u'i', order=10)
# kaph:http://en.wiktionary.org/wiki/
data['kap'] = dict(letter=[u'𐡊'], name=u'𐡊', segment='consonant', subsegment='', transliteration=u'k', order=11)
# lamed:http://en.wiktionary.org/wiki/
data['lamadh'] = dict(letter=[u'𐡋'], name=u'𐡋', segment='consonant', subsegment='', transliteration=u'l', order=12)
# mem:http://en.wiktionary.org/wiki/
data['mem'] = dict(letter=[u'𐡌'], name=u'𐡌', segment='consonant', subsegment='', transliteration=u'm', order=13)
# num:http://en.wiktionary.org/wiki/
data['num'] = dict(letter=[u'𐡍‬'], name=u'𐡍‬', segment='consonant', subsegment='', transliteration=u'n', order=14)
# samekh:http://en.wiktionary.org/wiki/
data['semkath'] = dict(letter=[u'𐡎'], name=u'𐡎', segment='consonant', subsegment='', transliteration=u's', order=15)
# ayin:http://en.wiktionary.org/wiki/
data['e'] = dict(letter=[u'𐡏‬'], name=u'𐡏‬', segment='vowel', subsegment='', transliteration=u'o', order=16)
# pe:http://en.wiktionary.org/wiki/
data['pe'] = dict(letter=[u'𐡐'], name=u'𐡐', segment='consonant', subsegment='', transliteration=u'p', order=17)
# tsade:http://en.wikipedia.org/wiki/
data['sadhe'] = dict(letter=[u'𐡑‬'], name=u'𐡑‬', segment='consonant', subsegment='', transliteration=u'ṣ', order=18)

# letters from 𐡒 to 𐡕
# resh:http://en.wiktionary.org/wiki/
data['qop'] = dict(letter=[u'𐡒'], name=u'𐡒', segment='consonant', subsegment='', transliteration=u'q', order=19)
# shin:http://en.wiktionary.org/wiki/
data['resh'] = dict(letter=[u'𐡓'], name=u'𐡓', segment='consonant', subsegment='', transliteration=u'r', order=20)
# tau:http://en.wiktionary.org/wiki/
data['shin'] = dict(letter=[u'𐡔'], name=u'𐡔', segment='consonant', subsegment='', transliteration=u'š', order=21)
# final_tsade:http://en.wiktionary.org/wiki/
data['taw'] = dict(letter=[u'𐡕'], name=u'𐡕', segment='consonant', subsegment='', transliteration=u't', order=22)
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

# collect aramaic and transliteration letters from data dictionary for preprocessing function
letters = ''.join([''.join(d['letter'])+d['transliteration'] for key, d in data.items()])
regex = re.compile('[^%s ]+' % letters)
regex2 = re.compile('[^%s\s]' % ''.join([''.join(d['letter']) for key, d in data.items()]))

r = romanizer(data)

def filter(string):
    """
    Preprocess string to remove all other characters but aramaic ones

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
