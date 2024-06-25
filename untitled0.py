# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:06:24 2024

@author: welcome
"""

import glassdoor_scraper as gs
import pandas as pd
path = "D:/Practice/ds_salary/chromedriver"

df = gs.get_jobs('data_scientist',15,False,path,15)