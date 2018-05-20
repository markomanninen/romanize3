#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: phn.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = False

data = OrderedDict()

# https://en.wikipedia.org/wiki/Aramaic_alphabet
# https://en.wikipedia.org/wiki/Phoenician_alphabet
# 1 = 𐤖 ‬
# 2 = 𐤚‬
# 3 = 𐤛
# 10 = 𐤗
# 20 = 𐤘
# 100 = 𐤙

# letters from 𐤀 to 𐤈
# alef:http://en.wiktionary.org/wiki/
data['alep'] = dict(letter=[u'𐤀'], name=u'𐤀', segment='vowel', subsegment='', transliteration=u'a', order=1)
# beth:http://en.wiktionary.org/wiki/
data['bet'] = dict(letter=[u'𐤁'], name=u'𐤁', segment='consonant', subsegment='', transliteration=u'b', order=2)
# gimel:http://en.wiktionary.org/wiki/
data['giml'] = dict(letter=[u'𐤂'], name=u'𐤂', segment='consonant', subsegment='', transliteration=u'g', order=3)
# daleth:http://en.wiktionary.org/wiki/
data['dalet'] = dict(letter=[u'𐤃'], name=u'𐤃', segment='consonant', subsegment='', transliteration=u'd', order=4)
# he:http://en.wiktionary.org/wiki/
data['he'] = dict(letter=[u'𐤄'], name=u'𐤄', segment='vowel', subsegment='', transliteration=u'h', order=5)
# vau:http://en.wikipedia.org/wiki/
data['waw'] = dict(letter=[u'𐤅'], name=u'𐤅', segment='vowel', subsegment='', transliteration=u'w', order=6)
# zayin:http://en.wiktionary.org/wiki/
data['zayin'] = dict(letter=[u'𐤆'], name=u'𐤆', segment='consonant', subsegment='', transliteration=u'z', order=7)
# heth:http://en.wiktionary.org/wiki/
data['het'] = dict(letter=[u'𐤇'], name=u'𐤇', segment='consonant', subsegment='', transliteration=u'ḥ', order=8)
# teth:http://en.wiktionary.org/wiki/
data['tet'] = dict(letter=[u'𐤈'], name=u'𐤈', segment='consonant', subsegment='', transliteration=u'ṭ', order=9)

# letters from 𐤉 to 𐤑‬
# yod:http://en.wiktionary.org/wiki/
data['yod'] = dict(letter=[u'𐤉'], name=u'𐤉', segment='vowel', subsegment='', transliteration=u'y', order=10)
# kaph:http://en.wiktionary.org/wiki/
data['kap'] = dict(letter=[u'𐤊'], name=u'𐤊', segment='consonant', subsegment='', transliteration=u'k', order=11)
# lamed:http://en.wiktionary.org/wiki/
data['lamed'] = dict(letter=[u'𐤋'], name=u'𐤋', segment='consonant', subsegment='', transliteration=u'l', order=12)
# mem:http://en.wiktionary.org/wiki/
data['mem'] = dict(letter=[u'𐤌'], name=u'𐤌', segment='consonant', subsegment='', transliteration=u'm', order=13)
# num:http://en.wiktionary.org/wiki/
data['nun'] = dict(letter=[u'𐤍'], name=u'𐤍', segment='consonant', subsegment='', transliteration=u'n', order=14)
# samekh:http://en.wiktionary.org/wiki/
data['semek'] = dict(letter=[u'𐤎'], name=u'𐤎', segment='consonant', subsegment='', transliteration=u's', order=15)
# ayin:http://en.wiktionary.org/wiki/
data['ayin'] = dict(letter=[u'𐤏'], name=u'𐤏', segment='vowel', subsegment='', transliteration=u'o', order=16)
# pe:http://en.wiktionary.org/wiki/
data['pe'] = dict(letter=[u'𐤐'], name=u'𐤐', segment='consonant', subsegment='', transliteration=u'p', order=17)
# tsade:http://en.wikipedia.org/wiki/
data['sade'] = dict(letter=[u'𐤑'], name=u'𐤑', segment='consonant', subsegment='', transliteration=u'ṣ', order=18)

# letters from 𐤒 to ܬ
# resh:http://en.wiktionary.org/wiki/
data['qop'] = dict(letter=[u'𐤒'], name=u'𐤒', segment='consonant', subsegment='', transliteration=u'q', order=19)
# shin:http://en.wiktionary.org/wiki/
data['res'] = dict(letter=[u'𐤓'], name=u'𐤓', segment='consonant', subsegment='', transliteration=u'r', order=20)
# tau:http://en.wiktionary.org/wiki/
data['sin'] = dict(letter=[u'𐤔'], name=u'𐤔', segment='consonant', subsegment='', transliteration=u'š', order=21)
# final_tsade:http://en.wiktionary.org/wiki/
data['taw'] = dict(letter=[u'𐤕'], name=u'𐤕', segment='consonant', subsegment='', transliteration=u't', order=22)
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

# collect phoenician and transliteration letters from data dictionary for preprocessing function
letters = ''.join([''.join(d['letter'])+d['transliteration'] for key, d in data.items()])
regex = re.compile('[^%s ]+' % letters)
regex2 = re.compile('[^%s\s]' % ''.join([''.join(d['letter']) for key, d in data.items()]))

def filter(string):
    """
    Preprocess string to remove all other characters but phoenician ones

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
