import matplotlib.pyplot as plt
import numpy as np

om = 0.308
z = np.arange( 0.05, 5., 0.05)  #redshift
q = np.zeros_like(z)            #deceleration parameter for modified gravity, array of zeros same format as z to reassign later
l = np.zeros_like(z)            #same as above but for ΛCDM model

# the following loops across length of z array and calculates deceleration parameter for each z in the two models
# assigns deceleration parameter value to correct place in the zero arrays

for i in range(len(z)): 
    x = np.float_power((1.-om) , 2) + 4 * om * np.float_power((1+z[i]),  3) # makes q expression easier to type, splits it into two lines
    q[i] = (( 6 * om * np.float_power((1+z[i]) , 3) ) / ( np.sqrt( x ) * ( 1 - om + np.sqrt( x ) )     ) ) - 1 # performs calculation of q for a given z
    l[i] = 0.5 * ( 1 - ( 3 * (1 - om) ) / ( om * np.float_power((1+z[i]) , 3) + 1 - om ) ) # performs calculation of l for given z


#following is all plotting

plt.plot(z,q, color = 'b' , label = 'Modified Gravity')
plt.plot(z,l, color = 'r', linestyle = '--',  label = 'ΛCDM')
plt.ylabel('Deceleration Parameter')
plt.xlabel('Redshift')
plt.legend()
plt.savefig('z_decel_grav.png')
plt.show()
