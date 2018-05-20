#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: san.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = False

# https://en.wikipedia.org/wiki/Katapayadi_system

data = OrderedDict()

r = romanizer(data)

def filter(string):
    """
    Preprocess string to remove all other characters but sanskrit ones

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
    return string

def convert(string, sanitize=False):
    """
    Swap characters from script to transliterated version and vice versa.
    Optionally sanitize string by using preprocess function.

    :param sanitize:
    :param string:
    :return:
    """
    return r.convert(string, (preprocess if sanitize else False))
