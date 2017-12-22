import fiona
import csv
import datetime
import time
import subprocess

def main():
	'''
	filename_zone = "../data/Zone" 
	filename_format = ".gdb"
	for year in range(2009, 2015):
		for zone in range(1,13):
			for count in range(1,17):
				final = filename_zone + str(zone) + "_" + str(year) + "_" + str(count).zfill(2) + filename_format
				print(final)
	
	filename_zone = "../data/2009/01_January_2009/" 
	for zone in range(1,19):
			final = filename_zone + str(zone) + "_2009_01.gdb"
	
	'''

	year = '2012'
	months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
	for zone in range(11,12):
		for count in range(1,13):
			ais_data = [['id','latitude','longitude','SOG','COG','Heading','ROT','Year','Month','Day','Hour','Min','Sec','Status','VoyageID','MMSI','ReceiverType','ReceiverID']]
			fname = "Zone" + str(zone) + "_" + str(year) + "_" + str(count).zfill(2) + ".gdb.zip"
			#fn_url = "https://coast.noaa.gov/htdata/CMSP/AISDataHandler/"+year+"/"+str(count).zfill(2)+"_"+str(months[count-1])+"_"+year+"/" + fname
			fn_url = "https://coast.noaa.gov/htdata/CMSP/AISDataHandler/"+year+"/"+str(count).zfill(2)+"/" + fname 

			#"https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2010/02_February_2010/Zone17_2010_02.zip"
			#print("wget "+fn_url)
			#print("unzip "+ fname)
			#print("rm "+fname)
			#print("rm "+fname[:-3]+"gdb")
			
			subprocess.call("wget "+fn_url, shell=True)
			subprocess.call("unzip "+fname, shell=True)
			subprocess.call("rm "+fname, shell=True)
			gdb_data = fiona.open(fname[:-4])
			ais_data = [['id','latitude','longitude','SOG','COG','Heading','ROT','Timestamp','Status','VoyageID','MMSI','ReceiverType','ReceiverID']]
			for row in gdb_data:
				val = row['properties']['BaseDateTime'].split('-')
				val.extend(val[2][3:].split(':'))
				val[2] = val[2][:2]
				y,m,d,h,mn,s = [int(x) for x in val]
				dt = datetime.datetime(year=y, month=m, day=d, hour=h, minute=mn, second=s)
				dt = int(time.mktime(dt.timetuple()))
				ais_data.append([str(x) for x in [row['id'], row['geometry']['coordinates'][1], row['geometry']['coordinates'][0], row['properties']['SOG'], row['properties']['COG'], row['properties']['Heading'], row['properties']['ROT'],dt, row['properties']['Status'], row['properties']['VoyageID'], row['properties']['MMSI'], row['properties']['ReceiverType'], row['properties']['ReceiverID']]])
			subprocess.call("rm -rf "+fname[:-3]+"gdb", shell=True)
			with open(fname[:-3]+"csv", "w") as f:
				writer = csv.writer(f)
				writer.writerows(ais_data)
			
	'''
	gdb_data = fiona.open("../data/Zone1_2014_01.gdb")
	print(gdb_data.schema)
	print(len(gdb_data))
	
	#ais_data = [['id','latitude','longitude','SOG','COG','Heading','ROT','Year','Month','Day','Hour','Min','Sec','Status','VoyageID','MMSI','ReceiverType','ReceiverID']]
	ais_data = [['id','latitude','longitude','SOG','COG','Heading','ROT','Timestamp','Status','VoyageID','MMSI','ReceiverType','ReceiverID']]
	for row in gdb_data:
		val = row['properties']['BaseDateTime'].split('-')
		val.extend(val[2][3:].split(':'))
		val[2] = val[2][:2]
		y,m,d,h,mn,s = [int(x) for x in val]
		dt = datetime.datetime(year=y, month=m, day=d, hour=h, minute=mn, second=s)
		dt = int(time.mktime(dt.timetuple()))
		#ais_data.append([str(x) for x in [row['id'], row['geometry']['coordinates'][1], row['geometry']['coordinates'][0], row['properties']['SOG'], row['properties']['COG'], row['properties']['Heading'], row['properties']['ROT'], y,m,d,h,mn,s, row['properties']['Status'], row['properties']['VoyageID'], row['properties']['MMSI'], row['properties']['ReceiverType'], row['properties']['ReceiverID']]])
		ais_data.append([str(x) for x in [row['id'], row['geometry']['coordinates'][1], row['geometry']['coordinates'][0], row['properties']['SOG'], row['properties']['COG'], row['properties']['Heading'], row['properties']['ROT'],dt, row['properties']['Status'], row['properties']['VoyageID'], row['properties']['MMSI'], row['properties']['ReceiverType'], row['properties']['ReceiverID']]])
		
	print(len(ais_data))
	with open("../data/Zone1_2014_01.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(ais_data)
	'''

#https://coast.noaa.gov/htdata/CMSP/AISDataHandler/AIS_FGDBs/Zone1/Zone1_2009_01.zip

#{'type': 'Feature', 'id': '64963', 'geometry': {'type': 'Point', 'coordinates': (-177.529652, 51.07158000000001)}, 'properties': OrderedDict([('SOG', 13.199999809265137), ('COG', 79.4000015258789), ('Heading', 75.0), ('ROT', 0.0), ('BaseDateTime', '2014-01-31T23:59:28'), ('Status', 0), ('VoyageID', 526), ('MMSI', 311700007), ('ReceiverType', 'r'), ('ReceiverID', '17MADA1')])}

if __name__=="__main__":
	main()