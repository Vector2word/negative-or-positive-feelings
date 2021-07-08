# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 22:14:02 2021

@author: My Lenovo
"""

import pickle
counter = pickle.load( open( "count_vect.p", "rb" ) )
training_counts =  pickle.load( open( "train.p", "rb" ) )