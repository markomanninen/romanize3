#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: grc.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = True

data = OrderedDict()

"""

Data mapping between greek letters and their linguistic components

Resources:

- http://en.wikipedia.org/wiki/Greek_alphabet
- http://www.chlt.org/FirstGreekBook/JWW_FGB1.html
- http://www.webtopos.gr/eng/languages/greek/alphabet/alpha.htm
- http://www.class.uh.edu/mcl/faculty/pozzi/grnl1/intr/0.2.1.pract.vow.htm
- http://en.wikipedia.org/wiki/transliterationization_of_Greek
- http://en.citizendium.org/wiki/greek_alphabet

Segments:
- vowel
- consonant
- numeral (only)

Subsegments:
- semivowel (liquid, siblant and γ-nasal not specified on data table)
- double
- mute

Mutes (not specified on data table):

{class-order} {letter}

labial-smooth π
labial-middle β
labial-rought φ

palatal-smooth κ
palatal-middle γ
palatal-rought χ

lingual-smooth τ
lingual-middle δ
lingual-rought θ

Seven vowels: α ε η ι ο υ ω (a e ê i o u ô)

Numerals only: ϛ ϙ ϡ (6, 90, 900 or w, q, j)

"""

# letters from α to θ (1 to 9)
# alpha:http://en.wiktionary.org/wiki/ἄλφα
data['alpha'] = dict(letter=[u'α'], name=u'αλφα', segment='vowel', subsegment='short', transliteration=u'a', order=1)
# beta:http://en.wiktionary.org/wiki/βῆτα
data['beta'] = dict(letter=[u'β'], name=u'βητα', segment='consonant', subsegment='mute', transliteration=u'b', order=2)
# gamma:http://en.wiktionary.org/wiki/γάμμα
data['gamma'] = dict(letter=[u'γ'], name=u'γαμμα', segment='consonant', subsegment='mute', transliteration=u'g', order=3)
# delta:http://en.wiktionary.org/wiki/δέλτα
data['delta'] = dict(letter=[u'δ'], name=u'δελτα', segment='consonant', subsegment='mute', transliteration=u'd', order=4)
# epsilon:http://en.wiktionary.org/wiki/epsilon
data['epsilon'] = dict(letter=[u'ε', u'ϵ'], name=u'ε ψιλον', segment='vowel', subsegment='short', transliteration=u'e', order=5)
# digamma/stigma/episemon/wau:http://en.wikipedia.org/wiki/Digamma
data['digamma'] = dict(letter=[u'ϛ', u'ϝ'], name=u'διγαμμα', segment='numeral', subsegment='', transliteration=u'w', order=6)
#data['stigma'] = dict(letter=[u'ϛ'], name=u'στιγμα', segment='numeral', transliteration=u'w')
# zeta:http://en.wiktionary.org/wiki/ζῆτα
data['zeta'] = dict(letter=[u'ζ'], name=u'ζητα', segment='consonant', subsegment='double', transliteration=u'z', order=7)
# eta:http://en.wiktionary.org/wiki/ἦτα
data['eta'] = dict(letter=[u'η'], name=u'ητα', segment='vowel', subsegment='long', transliteration=u'ê', order=8)
# theta:http://en.wiktionary.org/wiki/θῆτα
data['theta'] = dict(letter=[u'θ', u'ϑ'], name=u'θητα', segment='consonant', subsegment='mute', transliteration=u'h', order=9)

# letters from ι to ϙ (10 to 90)
# iota:http://en.wiktionary.org/wiki/ἰῶτα
data['iota'] = dict(letter=[u'ι'], name=u'ιωτα', segment='vowel', subsegment='short', transliteration=u'i', order=10)
# kappa:http://en.wiktionary.org/wiki/κάππα
data['kappa'] = dict(letter=[u'κ'], name=u'καππα', segment='consonant', subsegment='mute', transliteration=u'k', order=11)
# lambda:http://en.wiktionary.org/wiki/λάμβδα
data['lambda'] = dict(letter=[u'λ'], name=u'λαμβδα', segment='consonant', subsegment='semivowel', transliteration=u'l', order=12)
# mu:http://en.wiktionary.org/wiki/mu
data['mu'] = dict(letter=[u'μ'], name=u'μυ', segment='consonant', subsegment='semivowel', transliteration=u'm', order=13)
# nu:http://en.wiktionary.org/wiki/νῦ
data['nu'] = dict(letter=[u'ν'], name=u'νυ', segment='consonant', subsegment='semivowel', transliteration=u'n', order=14)
# xi:http://en.wiktionary.org/wiki/ξεῖ
data['xi'] = dict(letter=[u'ξ'], name=u'ξει', segment='consonant', subsegment='double', transliteration=u'c', order=15)
# omicron:http://en.wiktionary.org/wiki/omicron
data['omicron'] = dict(letter=[u'ο'], name=u'ο μικρον', segment='vowel', subsegment='short', transliteration=u'o', order=16)
# pi:http://en.wiktionary.org/wiki/πεῖ
data['pi'] = dict(letter=[u'π'], name=u'πει', segment='consonant', subsegment='mute', transliteration=u'p', order=17)
# koppa:http://en.wikipedia.org/wiki/Koppa_(letter)
# http://www.webtopos.gr/eng/languages/greek/alphabet/earlyletters.htm
data['qoppa'] = dict(letter=[u'ϙ', u'ϟ'], name=u'κοππα', segment='numeral', subsegment='', transliteration=u'q', order=18)

# letters from ρ to ϡ (100 to 900)
# rho:http://en.wiktionary.org/wiki/ῥῶ
data['rho'] = dict(letter=[u'ρ'], name=u'ρω', segment='consonant', subsegment='semivowel', transliteration=u'r', order=19)
# sigma:http://en.wiktionary.org/wiki/σίγμα
data['sigma'] = dict(letter=[u'σ', u'ϲ', u'ς'], name=u'σιγμα', segment='consonant', subsegment='semivowel', transliteration=u's', order=20)
#data['san'] = dict(letter=[u'ϻ'], name=u'σαν', segment='consonant', subsegment='semivowel', transliteration=u's')
# tau:http://en.wiktionary.org/wiki/tau
data['tau'] = dict(letter=[u'τ'], name=u'ταυ', segment='consonant', subsegment='mute', transliteration=u't', order=21)
# upsilon:http://en.wiktionary.org/wiki/upsilon
data['upsilon'] = dict(letter=[u'υ', u'ϒ'], name=u'υ ψιλον', segment='vowel', subsegment='short', transliteration=u'u', order=22)
# phi:http://en.wiktionary.org/wiki/phi
data['phi'] = dict(letter=[u'φ'], name=u'φει', segment='consonant', subsegment='mute', transliteration=u'f', order=23)
# khi, chi:http://en.wiktionary.org/wiki/chi
data['chi'] = dict(letter=[u'χ'], name=u'χει', segment='consonant', subsegment='mute', transliteration=u'x', order=24)
# psi:http://en.wiktionary.org/wiki/psi
data['psi'] = dict(letter=[u'ψ'], name=u'ψει', segment='consonant', subsegment='double', transliteration=u'y', order=25)
# omega:http://en.wiktionary.org/wiki/omega
data['omega'] = dict(letter=[u'ω'], name=u'ω μεγα', segment='vowel', subsegment='long', transliteration=u'ô', order=26)
# sampi/disigma
# http://en.wikipedia.org/wiki/Sampi
# http://www.tlg.uci.edu/~opoudjis/unicode/other_nonattic.html#sampi
# http://www.parthia.com/fonts/sampi.htm
# http://www.jstor.org/stable/636031
data['sampi'] = dict(letter=[u'ϡ', u'ͳ'], name=u'σαμπι', segment='numeral', subsegment='', transliteration=u'j', order=27)
#data['disigma'] = dict(letter=[u'ϡ'], name=u'δισιγμα', segment='numeral', subsegment='', transliteration=u'j')

data['alpha_m'] = dict(letter=[u'ạ'], name=u'σαμπι', segment='numeral', subsegment='', transliteration=u'ạ', order=28)
# beta:http://en.wiktionary.org/wiki/βῆτα
data['beta_m'] = dict(letter=[u'ḅ'], name=u'βητα', segment='numeral', subsegment='', transliteration=u'ḅ', order=29)
# gamma:http://en.wiktionary.org/wiki/γάμμα
data['gamma_m'] = dict(letter=[u'ġ'], name=u'γαμμα', segment='numeral', subsegment='', transliteration=u'ġ', order=30)
# delta:http://en.wiktionary.org/wiki/δέλτα
data['delta_m'] = dict(letter=[u'ḍ'], name=u'δελτα', segment='numeral', subsegment='', transliteration=u'ḍ', order=31)
# epsilon:http://en.wiktionary.org/wiki/epsilon
data['epsilon_m'] = dict(letter=[u'ė'], name=u'ε ψιλον', segment='numeral', subsegment='', transliteration=u'ė', order=32)
# digamma/stigma/episemon/wau:http://en.wikipedia.org/wiki/Digamma
data['digamma_m'] = dict(letter=[u'ċ'], name=u'διγαμμα', segment='numeral', subsegment='', transliteration=u'ċ', order=33)
# zeta:http://en.wiktionary.org/wiki/ζῆτα
data['zeta_m'] = dict(letter=[u'ị'], name=u'ζητα', segment='numeral', subsegment='', transliteration=u'ị', order=34)
# eta:http://en.wiktionary.org/wiki/ἦτα
data['eta_m'] = dict(letter=[u'ḥ'], name=u'ητα', segment='numeral', subsegment='', transliteration=u'ḥ', order=35)
# theta:http://en.wiktionary.org/wiki/θῆτα
data['theta_m'] = dict(letter=[u'ṭ'], name=u'θητα', segment='numeral', subsegment='', transliteration=u'ṭ', order=36)

data['mu_m'] = dict(letter=[u'ṃ'], name=u'θητα', segment='numeral', subsegment='', transliteration=u'ṃ', order=37)

r = romanizer(data, has_capitals)

# accents / diacritics for simplified greek letters

_accents_ = {}

_accents_[u'Α'] = u"ᾏ Ἂ ᾈ Ἇ ᾊ Ἅ Ἀ Ἃ ᾉ Ὰ ᾋ Ἄ Ά Ἁ ᾼ ᾎ ᾌ ᾍ Ἆ Ᾰ Ᾱ Ά"
_accents_[u'α'] = u"ἄ ἂ ᾀ ᾷ ἁ ὰ ᾴ ἀ ἇ ᾄ ἅ ά ᾂ ᾆ ἆ ᾳ ᾲ ᾅ ᾃ ᾶ ᾁ ᾇ ἃ ά ᾰ ᾱ"

_accents_[u'Ε'] = u"Έ Ἑ Ἕ Ἓ Ὲ Ἐ Ἔ Ἒ Έ"
_accents_[u'ε'] = u"έ ἐ ὲ ἑ ἒ ἓ ἔ ἕ έ"

_accents_[u'Η'] = u"ᾚ ᾞ Ἠ Ἤ Ἢ Ἦ Ή Ἡ Ἥ Ἣ Ἧ Ὴ ῌ ᾙ ᾝ ᾛ ᾟ ᾘ ᾜ Ή"
_accents_[u'η'] = u"ᾖ ῇ ῄ ᾑ ἠ ἧ ἦ ἤ ᾐ ῂ ῃ ἣ ὴ ή ῆ ᾕ ᾓ ἥ ἢ ᾔ ᾗ ἡ ᾒ ή"

_accents_[u'Ι'] = u"Ὶ Ἶ Ἵ Ί Ἰ Ἱ Ἲ Ἴ Ἳ Ἷ Ί Ῑ Ῐ"
_accents_[u'ι'] = u"î ἴ ἰ ἵ ῒ ἲ ί ῗ ἱ ἳ ϊ ὶ ΐ ἷ ῖ ì ἶ ῐ ῑ ΐ ί"

_accents_[u'Ο'] = u"Ό Ὁ Ὅ Ὃ Ὸ Ὀ Ὄ Ὂ Ό"
_accents_[u'ο'] = u"ὁ ὂ ὀ ó ò ὅ ὄ ὃ ό ὸ ό"

_accents_[u'Ρ'] = u"Ῥ"
_accents_[u'ρ'] = u"ῥ ῤ"

_accents_[u'ϒ'] = u"Ύ Ὑ Ὕ Ὓ Ὗ Ὺ Ῡ Ύ Ῠ"
_accents_[u'υ'] = u"ῡ ΰ ῠ ῢ ὑ ὒ ὗ ὕ ύ ῦ ὐ ù ϋ ὺ ὓ ὖ ῧ ὔ ΰ ύ"

_accents_[u'Ω'] = u"ᾪ ᾮ Ὠ Ὤ Ὢ Ὦ Ώ Ὡ Ὥ Ὣ Ὧ Ὼ ῼ ᾩ ᾭ ᾫ ᾯ ᾨ ᾬ Ώ"
_accents_[u'ω'] = u"ῳ ᾧ ὥ ῷ ᾡ ὤ ᾦ ᾥ ῴ ᾢ ᾣ ᾤ ὣ ώ ῶ ὡ ᾠ ὢ ὦ ῲ ὼ ὠ ὧ ώ"

accents = {}

for letter, values in _accents_.items():
    for value in values.split():
        accents[value] = letter

regex1 = re.compile('|'.join(accents.keys()))
# collect greek and transliteration letters from data dictionary
letters = ''.join([''.join(d['letter'])+\
          ''.join(d['letter']).upper()+\
          d['transliteration']+\
          d['transliteration'].upper() for key, d in data.items()])
regex2 = re.compile('[^%s ]+' % letters)

regex3 = re.compile('[^%s%s\s]' % (''.join(accents.keys()), "ΑαΒβΓγΔδΕεϵΖζΗηΘθϑΙιΚκΛλΜμΝνΞξΟοΠπΡρΣϹσϲςΤτΥυϒΦφΧχΨψΩωϚϜϛϝϞϘϟϙϠͲϡͳ"))

def deaccent(string):
    """
    Remove diacritics (accents), keep base forms of Greek letters

    :param string:
    :return:
    """
    # convert diacritics to simpler forms
    return regex1.sub(lambda x: accents[x.group()], string)

def filter(string):
    """
    Preprocess string to remove all other characters but Greek ones and whitespace

    :param string:
    :return:
    """
    # remove all unwanted characters by replacing them with empty space
    # if removing all other characters then word divisioning might get lost and further
    # processing text would get difficult if not impossible
    return regex3.sub(' ', string)

def preprocess(string):
    """
    Preprocess string to transform all diacritics and remove other special characters than appropriate

    :param string:
    :return:
    """
    # convert diacritics to simpler forms
    string = regex1.sub(lambda x: accents[x.group()], string)
    # remove all rest of the unwanted characters
    return regex2.sub('', string)

def convert(string, sanitize=False):
    """
    Swap characters from script to transliterated version and vice versa.
    Optionally sanitize string by using preprocess function.

    :param sanitize:
    :param string:
    :return:
    """
    return r.convert(string, (preprocess if sanitize else False))
