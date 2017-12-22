import fiona
import csv
import datetime
import time
import subprocess
import pandas as pd
import os.path
from operator import itemgetter
import glob


def main():
	fd = dict()
	for fname in glob.glob("../data/*_vessel.csv"):
		data = pd.read_csv(fname, low_memory=False)
		fd[fname] = data.shape[0]
	tf = sorted(fd.items(), key=itemgetter(1), reverse=True)	
	print(tf[:20])
	

if __name__=="__main__":
	main()