import fiona
import csv
import datetime
import time
import subprocess
import pandas as pd
import os.path

def main():
	year = '2014'
	ids = ['11','10','35','12','5','9','4','21','3','24']
	for zone in range(1,11):
		for count in range(4,5):
			fname = "Zone" + str(zone) + "_" + str(year) + "_" + str(count).zfill(2) + ".csv"
			data = pd.read_csv(fname)
			#print(data.columns)
			#for i in data["VoyageID"].unique():
			for i in ids:
				zone_file = "../data/2014_04/"+str(i)+"_vessel.csv"
				#print(zone_file)
				
				if not os.path.exists(zone_file):
					zdf = open(zone_file,"w")
					zdf.close()
					ais_data = [['id','latitude','longitude','SOG','COG','Heading','ROT','Timestamp','Status','VoyageID','MMSI','ReceiverType','ReceiverID']]
					with open(zone_file, "w") as f:
						writer = csv.writer(f)	
						writer.writerows(ais_data)
				tmp_df = data.loc[data["VoyageID"] == int(i)]
				#print(len(tmp_df.values.tolist()))
				with open(zone_file, "a") as f:
					writer = csv.writer(f)	
					writer.writerows(tmp_df.values.tolist())
				
				

if __name__=="__main__":
	main()