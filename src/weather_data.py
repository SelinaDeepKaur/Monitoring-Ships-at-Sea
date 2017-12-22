from datetime import datetime, timedelta
import time
import subprocess
import urllib.request
import sys

#"https://www.worldtides.info/api?heights&lat=-70&lon=-138&start=1325710788&length=1209600&maxcalls=5&key=c3d7f3a1-4f01-4c39-8640-7478df536780"

def main():
	api_keys = ["ca2cdeb2-ffa9-4c7b-8dcc-e9ec031ecded","984695b0-01ed-4194-9a37-58053c95affb","6db2be05-8bc9-4758-b148-16fcdc7350d3","c3d7f3a1-4f01-4c39-8640-7478df536780",  "1213d622-67f5-4441-8c19-2dd3e9c95407"]
	latitude_range = [-90,90]
	longitude_range = [-120,-114]
	#timstamp_start = 
	#url = "http://history.openweathermap.org/data/2.5/history/city?lat="+latitude"&lon="+longitude+"&type=hour&start={start}&end={end}""
	lat_step = 15
	long_step = 3

	invalid_pairs = [(-82.5, -118.5), (-82.5, -115.5), (37.5, -118.5), (37.5, -115.5), (52.5, -118.5), (52.5, -115.5), (67.5, -118.5)]
	valid_pairs = [(-70, -138), (-70, -138), (37.5, -125), (37.5, -125), (52.5, -135), (52.5, -135), (75, -135)]
	invalid_count = 0
	credit = 0
	key = 0
	exec_count = 0
	
	for i in range(-90,90,lat_step):
		for j in range(-120,-114,long_step):
			start_time = 1325710788
			for k in range(1,27):
				exec_count +=1
				credit += 4
				if credit>950:
					key += 1
					credit = 0

				latitude = i + (lat_step/2)
				longitude = j + (long_step/2)
				if (latitude,longitude) in invalid_pairs:
					latitude,longitude = valid_pairs[invalid_pairs.index((latitude,longitude))] 
				
				#print(latitude, longitude)
				url = "https://www.worldtides.info/api?heights&lat="+str(latitude)+"&lon="+str(longitude)+"&start="+str(start_time)+"&length=1209600&maxcalls=5&key="+api_keys[key]
				fname = "../data/2012/json/" + str(start_time) + "_" + str(latitude) + "_" + str(longitude) + "_" + ".json"
				dt = datetime.fromtimestamp(start_time) + timedelta(days=14)
				start_time = int(time.mktime(dt.timetuple()))
				
				print(url)
				
				try:
					f = urllib.request.urlopen(url)
					data = f.read()
					tmp = open(fname, 'w+')
					tmp.write(str(data))
					tmp.close()
				except:
					invalid_count += 1
					print(data)
					print("Invalid ",start_time," ", latitude,",",longitude,"\n URL: ", url)
					sys.exit()

	print(invalid_count)
	print(exec_count)
	

if __name__=="__main__":
	main()