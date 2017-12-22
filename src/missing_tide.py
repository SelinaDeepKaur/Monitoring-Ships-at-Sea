import json

def get_avg(val):
	s = 0
	c = 0
	for i in val:
		if i!=0:
			c+=1
			s+=1
	return s/c

def closest_nonzero(lst, start_index):
	left = 0
	right = 0
	for i in range(start_index+1, len(lst)):
		if lst[str(i)]!=0:
			right = i - start_index
	for i in range(start_index-1,0,-1):
		if lst[str(i)]!=0:
			left = start_index - i
	return lst[str(min(left,right))]

def main():
	fname = "tides.json"
	f = open(fname,'r')
	parent_json = json.loads(f.read())
	lat_step = 15
	long_step = 3

	for lat in range(-90,90,lat_step):
		latitude = lat + (lat_step/2)
		for lon in range(-120,-114,long_step):
			longitude = lon + (long_step/2)
			for i in range(1,13):
				for j in range(1,32):
					for k in range(0,24):	
						if parent_json[str(latitude)][str(longitude)][str(i)][str(j)][str(k)] == 0:
							parent_json[str(latitude)][str(longitude)][str(i)][str(j)][str(k)] = closest_nonzero(parent_json[str(latitude)][str(longitude)][str(i)][str(j)], k)

	with open('tides_missing_handled.json', 'w') as fp:
		json.dump(parent_json, fp)
	f.close()

if __name__=="__main__":
	main()