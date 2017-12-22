import json
import glob
import datetime
import pandas as pd

def find_lat_long_ranges(lat, lon):
	lat_ranges = [i for i in range(-90,90,15)]
	long_ranges = [i for i in range(-120,-114,3)]
	lat_val = 0
	lon_val = 0
	
	for i in lat_ranges:
		if lat<=i:
			break
	lat_val = i + 7.5

	for i in long_ranges:
		if lon<=i:
			break
	lon_val = i + 1.5
	return (str(lat_val), str(lon_val))

def main():
	files = glob.glob("../data/2012/*.gdb.csv")
	
	f = open("tides_missing_handled.json",'r')
	tide_json = json.loads(f.read())
	print("loaded")
	
	fname = "../data/2012/Zone11_2012_07.gdb.csv"
	
	data = pd.read_csv(fname)
	print("read dataframe")
	data["tide"] = 0.0
	for i in range(0, len(data)):
		if i%100000==0:
			print(i)
		latitude, longitude = find_lat_long_ranges(float(data.iloc[i]["latitude"]),float(data.iloc[i]["longitude"]))
		timestamp = int(data.iloc[i]["Timestamp"])
		date = datetime.datetime.fromtimestamp(timestamp)
		#print(tide_json[latitude])
		#print(tide_json[latitude][longitude])
		#print(tide_json[latitude][longitude][str(date.month)])
		#print(tide_json[latitude][longitude][str(date.month)][str(date.day)])
		#print(tide_json[latitude][longitude][str(date.month)][str(date.day)][str(date.hour)])
		data.set_value(i,"tide",tide_json[latitude][longitude][str(date.month)][str(date.day)][str(date.hour)])   
	data.to_csv('Zone11_2012_07_tide.csv')

	'''
	for fname in files:
		data = pd.read_csv(fname)
		data["tide"] = 0.0
		for i in range(0, len(data)):
			latitude, longitude = find_lat_long_ranges(float(data.iloc[i]["latitude"]),float(data.iloc[i]["longitude"]))
			timestamp = int(data.iloc[i]["Timestamp"])
			date = datetime.fromtimestamp(timestamp)
			data.iloc[i]["tide"] = tide_json[latitude][longitude][date.month][date.day][date.hour]
	'''

if __name__=="__main__":
	main()