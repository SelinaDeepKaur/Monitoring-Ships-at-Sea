import fiona
import csv
from datetime import datetime
import time
import subprocess
import pandas as pd
import os.path
from operator import itemgetter
import glob

def main():
	#csv_files = [('../data/11_vessel.csv', 488056), ('../data/35_vessel.csv', 435775), ('../data/10_vessel.csv', 403414), ('../data/12_vessel.csv', 400891), ('../data/5_vessel.csv', 394976), ('../data/9_vessel.csv', 392663), ('../data/4_vessel.csv', 388618), ('../data/21_vessel.csv', 381673), ('../data/3_vessel.csv', 378573), ('../data/24_vessel.csv', 363456)]
	#csv_files = [('../data/2014_04/11_vessel.csv', 488056), ('../data/2014_04/35_vessel.csv', 435775), ('../data/2014_04/10_vessel.csv', 403414), ('../data/2014_04/12_vessel.csv', 400891), ('../data/2014_04/5_vessel.csv', 394976), ('../data/2014_04/9_vessel.csv', 392663), ('../data/2014_04/4_vessel.csv', 388618), ('../data/2014_04/21_vessel.csv', 381673), ('../data/2014_04/3_vessel.csv', 378573), ('../data/2014_04/24_vessel.csv', 363456)]
	csv_files = [('../data/35_vessel.csv', 0)]
	df_rows = [['id','latitude','longitude','SOG','COG','Heading','ROT','Timestamp','Status','VoyageID','MMSI','ReceiverType','ReceiverID','Year','Month','Day','Hour','Min','Second']]
	for fname in csv_files:
		data = pd.read_csv(fname[0], low_memory=False)
		for row in data.values.tolist():
			tmp = datetime.fromtimestamp(int(row[7]))
			df_rows.append(row + [tmp.year, tmp.month, tmp.day, tmp.hour, tmp.minute, tmp.second])
	with open("ais_vessel_data_35.csv", "w") as f:
		writer = csv.writer(f)	
		writer.writerows(df_rows)

if __name__=="__main__":
	main()