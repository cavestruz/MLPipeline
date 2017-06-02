from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras import losses
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.svm import SVR

seed = np.random.seed(seed=7)
f = open('x_results.csv')
data=f.readlines()
data.pop(0)
for i in range(len(data)):
	data[i]=data[i].split(',')
	if (data[i][5]=='QSO' or data[i][5]=='STAR'):
		data[i][5]=2
	else:
		data[i][5]=1
data=np.array(data)
data=data.astype(np.float)
mag=[]
for i in range(len(data)):
	if (data[i][5]==1):
		mag.append(data[i])

mag=np.array(mag)
for i in range(317512):
	if(mag[i][0]<0 or mag[i][0]>30 and mag[i][2]<0 or mag[i][2]>30 and mag[i][3]<0 or mag[i][3]>30 and mag[i][4]<0 or mag[i][4]>30):
		mag=np.delete(mag,i,axis=0)
ug=[0]*len(mag)
ur=[0]*len(mag)
ui=[0]*len(mag)
uz=[0]*len(mag)
gr=[0]*len(mag)
gi=[0]*len(mag)
gz=[0]*len(mag)
ri=[0]*len(mag)
rz=[0]*len(mag)
iz=[0]*len(mag)
colors=[0]*len(mag)
for i in range(len(mag)):
	ug[i] = mag[i][0]-mag[i][1]
	ur[i] = mag[i][0]-mag[i][2]
	ui[i] = mag[i][0]-mag[i][3]
	uz[i] = mag[i][0]-mag[i][4]
	gr[i] = mag[i][1]-mag[i][2]
	gi[i] = mag[i][1]-mag[i][3]
	gz[i] = mag[i][1]-mag[i][4]
	ri[i] = mag[i][2]-mag[i][3]
	rz[i] = mag[i][2]-mag[i][4]
	iz[i] = mag[i][3]-mag[i][4]
	colors[i]=[ug[i],ur[i],ui[i],uz[i],gr[i],gi[i],gz[i],ri[i],rz[i],iz[i]]
colors=np.array(colors)


Xmag=[mag[:,0],mag[:,1],mag[:,2],mag[:,3],mag[:,4]]
y = mag[:,6]
Xmag=np.array(Xmag).T
y=np.array(y)
Xmag_train, Xmag_test, ymag_train, ymag_test = train_test_split(Xmag, y, test_size=0.25, random_state=42)
clfmag=linear_model.SGDRegressor(loss='huber',n_iter=100)
clfmag.fit(Xmag_train,ymag_train)


 

Xcolors_train, Xcolors_test, ycolors_train, ycolors_test = train_test_split(colors, y,test_size=0.25, random_state=42)
clfcolors=linear_model.SGDRegressor(loss='huber',n_iter=100)
clfcolors.fit(Xcolors_train,ycolors_train)

def computeR(y_true,y_pred):
	u=((y_true-y_pred)**2).sum()
	v=((y_true-y_true.mean())**2).sum()
	return 1-(u/v)
#n_iter=[]
#n_iter2=[]
#for i in range(1,5):
	#clfcolors=linear_model.SGDRegressor(loss='huber',n_iter=10**i)
	#clfcolors.fit(Xcolors_train,ycolors_train)
	#n_iter.append(computeR(ycolors_test, clfcolors.predict(Xcolors_test)))
	#clfmag=linear_model.SGDRegressor(loss='huber',n_iter=10**i)
	#clfmag.fit(Xmag_train,ymag_train)
	#n_iter2.append(computeR(ymag_test, clfmag.predict(Xmag_test)))




def plot_data(i,xlabel,title):
	xlabel,title=str(xlabel),str(title)	
	plt.plot(Xmag_test[:,i],ymag_test,'bo',label='Test Data Set')
	plt.plot(Xmag_test[:,i],clfmag.predict(Xmag_test), 'ro', label='Predicted Redshift by SGD')
	plt.xlabel(xlabel)
	plt.ylabel('Redshift')
	plt.title(title)
	plt.legend()
	plt.show()

svmcolors=SVR(kernel='linear')
svmmag=SVR(kernel='linear')
svmmag.fit(Xmag_train,ymag_train)
svmcolors.fit(Xcolors_train,colors_train)


