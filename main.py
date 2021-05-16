#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Mon May  2021

@author: ATAGUN
"""
from concordance import Concordance
import pandas as pd


def conc2csv(file, word, idx):
    """
    conc2csv(): concordance to csv
    Concordance aranan sözcüğün önündeki ve arkasındaki dört sözcüğe bakıp
    excel dosyasına aktaran fonksiyon

    >>>from concordance import conc2csv

    >>>conc2csv('test.txt', 'bir', 4)

    :param idx: index parametresi
    :param file: concordance aranacak dosya adı
    :param word: concordance aranacak sözcük
    :return: csv (excel dosyası)
    """
    textlist = Concordance(file, word)
    data = []
    for i in textlist.look_concordance():
        before = [n for n in i[0]][-idx:]  # concordance arancak sözcükten önceki dört sözcük
        conc_word = [i[1]]  # concordance aranacak sözcük
        after = [n for n in i[2]][:idx]  # concordance arancak sözcükten sonraki dört sözcük
        all_together = before, conc_word, after
        data.append(all_together)
    df = pd.DataFrame(data, columns=['before', 'conc_word', 'after'])
    return df.to_csv('data.csv', encoding='utf-8-sig', sep=";")

