#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
__author__ = 'adrienpacifico'

import csv
import os
import pkg_resources

#import os
#dir = os.path.dirname(__file__)
#file_path = os.path.join(dir, './valeurs/Valeurs.csv')


import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )



#table = open(file_path)
csv_file_path = os.path.join(
    pkg_resources.get_distribution('real_value').location,
    "real_value",
    "valeurs",
    "Valeurs.csv",
)
table = open(csv_file_path)
csv_table = csv.reader(table, delimiter=';')

real_value_dict = dict()
for obs in csv_table:
    if obs[0][0].isdigit() == True:

        year, value = obs
        real_value_dict[year] = locale.atoi(value)

euro_franc_rate = 6.55957

def french_real_value(base_year, value, target_year):
    '''
    How does in base_year is valuated value of target_year
    '''
    return (real_value_dict[str(base_year)] / real_value_dict[str(target_year)])*value

def french_real_value_franc_to_euro(base_year, value, target_year):
    return (real_value_dict[str(base_year)] / real_value_dict[str(target_year)])*value
