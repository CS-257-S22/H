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
import random

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

# a class to read from the psql database
class DataSource():
        
    #------------------------------

    def __init__(self):
        """
        Establish the first instance by connecting to the database
        """

        self.database = self.connect()

    #------------------------------

    def connect(self):
        """
        Connect to the team's database using the given credentials on perlman
        """


        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host = "localhost")
        
        except Exception as e:
            print("Connection error: ", e)
            exit()

        return connection

#------------------------------

# CREATE THE TEAM'S DATABASE OBJECT
teamh = DataSource()
cursor = teamh.database.cursor()

#------------------------------
# IMPORT FEATURES

# We do NOT import all features in the universal import file because we don't want a feature to call itself.