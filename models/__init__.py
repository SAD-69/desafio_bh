import os
import sys
import csv
from geopandas import GeoDataFrame
from pandas import DataFrame, read_csv
from functools import cached_property

sys.path.append(os.path.abspath(os.getcwd()))