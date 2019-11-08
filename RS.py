#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:28:50 2019

@author: findlaybowditch
"""
import csv

with open('data.csv') as f:
        # we are using DictReader because we want our information to be in dictionary format.
    reader = csv.DictReader(f)
        
        
