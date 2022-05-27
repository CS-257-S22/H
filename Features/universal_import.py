# STOP PYCACHE
import fileinput
import sys
sys.dont_write_bytecode = True

#------------------------------
# LIBRARIES

import path
import argparse
import csv
from fileinput import filename
import unittest

import pandas as pd
import datetime

import matplotlib

# fixed MacOS compatibility issue
import matplotlib.pyplot as plt
plt.switch_backend('Agg')

import seaborn as sns
# set desired graph size
sns.set(rc={'figure.figsize':(10,5)})
# set background color
sns.set(rc={"axes.facecolor":"white", "figure.facecolor":"white"})

from enum import unique
from logging import raiseExceptions

from flask import render_template, Flask, request, url_for

#------------------------------
# DATABASE IMPORT

import psycopg2
import psqlConfig as config

#------------------------------
# IMPORT FEATURES

# We do NOT import all features in the universal import file because we don't want a feature to call itself.