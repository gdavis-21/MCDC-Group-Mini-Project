import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
import requests, lxml

try:
    df = pd.read_pickle("./MCDC-Data.pkl")
except FileNotFoundError:
    print("File Not Found")