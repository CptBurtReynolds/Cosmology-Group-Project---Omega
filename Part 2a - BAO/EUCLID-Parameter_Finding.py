import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.integrate as inte


#assign the given data
theta=(0.076963, 0.058244, 0.047934, 0.041425, 0.036949, 0.033683, 0.031197, 0.029240)
z=[0.5,0.7,0.9,1.1,1.3,1.5,1.7,1.9]

#set the values for the scale factor 
a_z=np.zeros(len(z))
for i in range(0,len(z)):
    a_z[i]=1/(1+z[i])

#set the values for the BAO length (just a constant array)
l=np.zeros(len(theta))
for i in range(0,len(l)):
    l[i]=147.60

#assign constants    
c=299800
H_0 = 67.81

    
def f(a,w,p,z):
    #takes the scale factor and baroropic parameters and calulates the function we integrate
    return 1/(math.sqrt(a)*math.sqrt(0.308 + 0.692*(1/a)**(3*(p+w))*np.exp(3*w*(a-1))))

def distance(a,b,z):
    #Function to return the distance to the BAO (at the lowest redshift). Takes w_a[0] and w_p[0] as arguments
    return c/H_0 * inte.quad(f, a_z[z], 1, args=(a,b,z))[0]

def difference(a,b,z):
    #function to caluculate the difference between the theoretical and simulated distances
    return abs(distance(a,b,z)-l[z]/theta[z])

w_a_list = np.arange(-0.25,0.25,0.001)
w_p_list = np.arange(-1.15,-0.85,0.001)
w_a = []
w_p = []
#assign the limiting difference
low = 0.1
for i in range(0,len(w_a_list)):
    for j in range(0,len(w_p_list)):
        #iterate through each value of w_a and w_p. and test the difference for each redshift 
        if (difference(w_a_list[i], w_p_list[j], 0)) < low:
            if (difference(w_a_list[i], w_p_list[j], 1)) < low:
                if (difference(w_a_list[i], w_p_list[j], 2)) < low:
                    if (difference(w_a_list[i], w_p_list[j], 3)) < low: 
                        if (difference(w_a_list[i], w_p_list[j], 4)) < low:
                            if (difference(w_a_list[i], w_p_list[j], 5)) < low:
                                if (difference(w_a_list[i], w_p_list[j], 6)) < low:
                                    if (difference(w_a_list[i], w_p_list[j], 7)) < low:
                                        w_a.append(w_a_list[i])
                                        w_p.append(w_p_list[j])

#create some empty lists we can edit
I=np.zeros(len(a_z))            
d_z=np.zeros_like(I)

#calculate the distance to the BAO using the found barotropic parameters
for i in range (0,len(I)):
    #I[i] = inte.quad(f, a_z[i], 1,args=(w_a[0],w_p[0],i))[0]
    d_z[i] = distance(w_a[0],w_p[0],i)
plt.plot(z, d_z, label="w")
plt.plot(z, l/theta, label="Theory")
plt.legend()
plt.show()