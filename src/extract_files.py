import glob
import os
import subprocess

for d in os.listdir("./"):
	zip_files = glob.glob(d+"/*.zip")
	for f in zip_files:
		subprocess.call("unzip "+f+" && rm "+f, shell=True)