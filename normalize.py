#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Mon May  2021

@author: ATAGUN

"""
import string


def normalize(sent):
    """
    Noktalama işretlerini kaldıran fonksiyon

    :param sent: Tokenleştirilmiş sözcük listesi
    :return: liste
    """
    tokens_without_punct = [''.join(c for c in s if c not in string.punctuation) for s in sent]  # removes punct
    tokens_without_punct_spaces = [s for s in tokens_without_punct if s]  # removes spaces

    return tokens_without_punct_spaces
