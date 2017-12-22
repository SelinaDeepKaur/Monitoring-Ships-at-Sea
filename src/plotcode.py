import time
import random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings('ignore')
def uniqueish_color():
    """There're better ways to generate unique colors, but this isn't awful."""
    return plt.cm.gist_ncar(np.random.random())
#df = pd.read_csv('plot.csv')
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


#fig = plt.figure(figsize=(8, 8))
#m = Basemap(projection='lcc', resolution=None,
#            width=2E6, height=2E6, 
#            lat_0=30, lon_0=-120,)
#m.etopo(scale=0.5, alpha=0.5)
df = pd.read_csv('actual55.csv')
pf = pd.read_csv('predicted55.csv') 

xdata = []
ydata = [] 
Ydata = df['latitude']
Xdata = df['longitude']

pxdata =[]
pydata =[]
PYdata = pf['latitude']
PXdata = pf['longitude']
  
print("hi")
print (df['Timestamp'].count())
plt.axes()
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.xlim([-125, -110])
plt.ylim([25, 40])
t=0.01
for i in range(0,df['Timestamp'].count(),200):
    #xdata = Xdata[i]

    #ydata = Ydata[i]

    pxdata,pydata = (PXdata[i],PYdata[i])
    xdata,ydata = (Xdata[i],Ydata[i])
    
    #print (Xdata[i])
    #print (Ydata[i])
    #ydata = Ydata[i]
 
    plt.plot(xdata,ydata, marker='*', markersize=5, color = 'red')#uniqueish_color())
    plt.plot(pxdata,pydata, marker='*', markersize=5, color = 'black')
    #plt.text(x, y, ' Seattle', fontsize=12);

    plt.draw()
    plt.pause(1e-17)
    #time.sleep(1)
    print (i)
    #print (pxdata)
    #print (xdata)
print("hello")
 
# for i,f in df['Timestamp'].iteritems():
#     xdata.append(Xdata[i])
#     ydata.append(Ydata[i])
#     line.set_xdata(xdata)
#     line.set_ydata(ydata)
#     plt.draw()
#     plt.pause(1e-17)
#     time.sleep(0.0000001)
 
# add this if you don't want the window to disappear at the end
plt.show()
