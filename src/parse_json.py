import json
import glob

def main():
	files = glob.glob("../data/2012/json/*.json")
	parent_json = dict()
	lat_step = 15
	long_step = 3

	for lat in range(-90,90,lat_step):
		latitude = lat + (lat_step/2)
		parent_json[str(latitude)] = {}
		for lon in range(-120,-114,long_step):
			longitude = lon + (long_step/2)
			parent_json[str(latitude)][str(longitude)] = {}
			for i in range(1,13):
				parent_json[str(latitude)][str(longitude)][str(i)] = {}
				for j in range(1,32):
					parent_json[str(latitude)][str(longitude)][str(i)][str(j)] = {}
					for k in range(0,24):	
						parent_json[str(latitude)][str(longitude)][str(i)][str(j)][str(k)] = 0

	invalid_pairs = [('-82.5', '-118.5'), ('-82.5', '-115.5'), ('37.5', '-118.5'), ('37.5', '-115.5'), ('52.5', '-118.5'), ('52.5', '-115.5'), ('67.5', '-118.5')]
	valid_pairs = [('-70', '-138'), ('-70', '-138'), ('37.5', '-125'), ('37.5', '-125'), ('52.5', '-135'), ('52.5', '-135'), ('75', '-135')]
	

	for f in files:
		op = open(f,'r')
		d = str(op.read())
		data = json.loads(d[2:-1])
		ht = data["heights"]
		for h in ht:
			dm = h["date"][5:-5].split('T')
			month,day = [str(int(x)) for x in dm[0].split("-")]
			hour = str(int(dm[1].split(":")[0]))
			tmp = str(f).split("_")
			lat,lon = tmp[1], tmp[2]
			if (lat,lon) in valid_pairs:
				ids = [i for i, x in enumerate(valid_pairs) if x == (lat,lon)]
				for k in ids:
					parent_json[invalid_pairs[k][0]][invalid_pairs[k][1]][month][day][hour] = h["height"]					
			else:
				parent_json[lat][lon][month][day][hour] = h["height"]
	
	with open('tides.json', 'w') as fp:
		json.dump(parent_json, fp)

if __name__=="__main__":
	main()