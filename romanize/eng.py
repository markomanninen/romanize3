#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: eng.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = True

data = OrderedDict()

data['a'] = dict(letter=[u'a'], name=u'a', segment='vowel',     subsegment='short', transliteration=u'a', order=1)
data['b'] = dict(letter=[u'b'], name=u'b', segment='consonant', subsegment='mute', transliteration=u'b', order=2)
data['c'] = dict(letter=[u'c'], name=u'c', segment='consonant', subsegment='mute', transliteration=u'c', order=3)
data['d'] = dict(letter=[u'd'], name=u'd', segment='consonant', subsegment='mute', transliteration=u'd', order=4)
data['e'] = dict(letter=[u'e'], name=u'e', segment='vowel',     subsegment='short', transliteration=u'e', order=5)
data['f'] = dict(letter=[u'f'], name=u'f', segment='consonant', subsegment='mute', transliteration=u'f', order=6)
data['g'] = dict(letter=[u'g'], name=u'g', segment='consonant', subsegment='mute', transliteration=u'g', order=7)
data['h'] = dict(letter=[u'h'], name=u'h', segment='consonant', subsegment='mute', transliteration=u'h', order=8)
data['i'] = dict(letter=[u'i'], name=u'i', segment='vowel',     subsegment='short', transliteration=u'i', order=9)
data['j'] = dict(letter=[u'j'], name=u'j', segment='consonant', subsegment='mute', transliteration=u'j', order=10)
data['k'] = dict(letter=[u'k'], name=u'k', segment='consonant', subsegment='mute', transliteration=u'k', order=11)
data['l'] = dict(letter=[u'l'], name=u'l', segment='consonant', subsegment='mute', transliteration=u'l', order=12)
data['m'] = dict(letter=[u'm'], name=u'm', segment='consonant', subsegment='mute', transliteration=u'm', order=13)
data['n'] = dict(letter=[u'n'], name=u'n', segment='consonant', subsegment='mute', transliteration=u'n', order=14)
data['o'] = dict(letter=[u'o'], name=u'o', segment='vowel',     subsegment='short', transliteration=u'o', order=15)
data['p'] = dict(letter=[u'p'], name=u'p', segment='consonant', subsegment='mute', transliteration=u'p', order=16)
data['q'] = dict(letter=[u'q'], name=u'q', segment='consonant', subsegment='mute', transliteration=u'q', order=17)
data['r'] = dict(letter=[u'r'], name=u'r', segment='consonant', subsegment='mute', transliteration=u'r', order=18)
data['s'] = dict(letter=[u's'], name=u's', segment='consonant', subsegment='mute', transliteration=u's', order=19)
data['t'] = dict(letter=[u't'], name=u't', segment='consonant', subsegment='mute', transliteration=u't', order=20)
data['u'] = dict(letter=[u'u'], name=u'u', segment='vowel',     subsegment='short', transliteration=u'u', order=21)
data['v'] = dict(letter=[u'v'], name=u'v', segment='consonant', subsegment='mute', transliteration=u'v', order=22)
data['w'] = dict(letter=[u'w'], name=u'w', segment='consonant', subsegment='mute', transliteration=u'w', order=23)
data['x'] = dict(letter=[u'x'], name=u'x', segment='consonant', subsegment='mute', transliteration=u'x', order=24)
data['y'] = dict(letter=[u'y'], name=u'y', segment='vowel',     subsegment='short', transliteration=u'y', order=25)
data['z'] = dict(letter=[u'z'], name=u'z', segment='consonant', subsegment='mute', transliteration=u'z', order=26)

r = romanizer(data, has_capitals)

# collect letters from data dictionary for preprocessing function
letters = ''.join(data.keys())
regex = re.compile('[^%s ]+' % letters)

def filter(string):
    """
    Preprocess string to remove all other characters but english ones

    :param string:
    :return:
    """
    # remove all unwanted characters
    return string

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
