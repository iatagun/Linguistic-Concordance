#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Mon May  2021

@author: ATAGUN

"""

from nltk import word_tokenize
from nltk.text import Text
from concordance.normalize import normalize


class Concordance:
    """
    Dilbilimcilerin ihtiyaçları doğrultusunda geliştirilen concordance aracı
    """

    def __init__(self, filename, concordance):
        """
        :param filename: Dosya ismi
        :param concordance: aranacak sözcük
        """
        self.filename = filename
        self.concordance = concordance

    def look_concordance(self):
        """
        :return: Concordance
        """
        tokens = word_tokenize(open(self.filename, 'r', encoding="utf8").read())  # read file
        normalized_text = normalize(tokens)  # removes punct and spaces
        conc = Text(normalized_text)  # special nltk funct
        result = conc.concordance_list(self.concordance, width=80, lines=25)  # object type list
        return result
