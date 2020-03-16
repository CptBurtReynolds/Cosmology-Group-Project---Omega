import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.integrate as inte
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms


theta=(0.121311,0.093789,0.077343,0.066296,0.058366,0.052641,0.048140,0.044499,0.041766,0.039271,0.037130,0.035488,0.033844,0.032429,0.031307,0.030201,0.029289,0.028627)
z=np.arange(0.3,2.1,0.1)
a_z=1/(1+z)


#set the values for the BAO length (just a constant array)
l=np.zeros(len(theta))
for i in range(0,len(l)):
    l[i]=147.60

#assign constants    
c=299800
H_0 = 67.81

w_p_list = np.arange(-1,-0.4,0.01)
w_a_list = np.arange(-0.3,0.3,0.01)


def f(a,w,p,z):
    #takes the scale factor and baroropic parameters and calulates the function we integrate
    return 1/(math.sqrt(a)*math.sqrt(0.308 + 0.692*(1/a)**(3*(p+w))*np.exp(3*w*(a-1))))

def distance(a,b,z):
    #Function to return the distance to the BAO (at the lowest redshift). Takes w_a[0] and w_p[0] as arguments
    return c/H_0 * inte.quad(f, a_z[z], 1, args=(a,b,z))[0]

def chi_squared(a,b):
    #function to calculate the chi squared value for a given w_a, w_p, and z
    theta_th = np.zeros_like(z)
    for i in range(0,len(z)):
        theta_th[i]=l[i]/distance(a,b,i)
        
    return np.sum(((theta-theta_th)**2)/(0.0001**2))

Xlist=[]
for i in w_a_list:
    for j in w_p_list:
        Xlist.append([chi_squared(i,j),i,j])

Min=min(Xlist)[0]

sigmaalist=[]
sigmaplist=[]
for i in range(0,len(Xlist)):
    if Xlist[i][0] < Min+18.1:
        sigmaalist.append(Xlist[i][1])
        sigmaplist.append(Xlist[i][2])
sigmaa= abs(min(sigmaalist)-min(Xlist)[1])
sigmap= abs(min(sigmaplist)-min(Xlist)[2])


x=sigmaalist
y=sigmaplist

def eigsorted(cov):
    vals, vecs = np.linalg.eigh(cov)
    order = vals.argsort()[::-1]
    return vals[order], vecs[:,order]

nstd = 2
ax = plt.subplot(111)

cov = np.cov(x, y)
vals, vecs = eigsorted(cov)
theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
w, h = 2 * nstd * np.sqrt(vals)
ell = Ellipse(xy=(np.mean(x), np.mean(y)),
              width=w, height=h,
              angle=theta, linestyle=('--'), color='r',label=r'$1\sigma$')
ell.set_facecolor('none')
#ell.set_label('1-sigma')
ax.add_artist(ell)
ell2 = Ellipse(xy=(np.mean(x), np.mean(y)),
              width=w*2, height=h*2,
              angle=theta, color='b', linestyle=('-.'), label=r'$2\sigma$')
ell2.set_facecolor('none')
#ell2.set_label('2-sigma')
ax.add_artist(ell2)
plt.xlabel(r'$w_a$')
plt.ylabel(r'$w_p$')
plt.scatter(x, y, color='black', s=1)
plt.legend(handles=[ell,ell2])
plt.savefig('error ellipse CPL.png')
plt.show()


















