import scipy.integrate as integrate
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import quad

z = np.arange(0.,2.01,0.01) # creates an array of z values
d_grav = np.zeros_like(z) # creates array of zeros with same layout as z
d_lambda = np.zeros_like(z) # same as above

def integrand_grav(a,H,c,O): # Function to perform integration required to calculate luminosity distance for a given redshift for DGP modified gravity model
    return (2*c)/( H * np.float_power(a,2) * ( (1-O) + np.sqrt( np.float_power((1-O),2) + 4 * O * np.float_power(a, -3) ) ) )

def integrand_lambda(a,H,c,O): # Similar to the above function but for the more simple ΛCDM model 
    return c/(H * np.float_power(a,2) * np.sqrt(1-O+O*np.float_power(a,-3)))

# float_power had to be used in the integration functions to avoid an error with raising floats to a power using standard power functions

for i in range(len(z)): # iterates over all z values and calculates the two lumiosity distances for each one
    
    c = 3e5 # defining constants to be used in integration
    H = 67.81
    O = 0.308
    
    # 0 index used for integration since it returns a pair of values, integration result and error on the result
    # these errors are so small for this integration they are being ignored, the errors are of the order of 10^-16
    
    d_grav[i] = quad(integrand_grav, 1/(1+z[i]), 1, args = (H,c,O))[0] # assigns the integration result to the correct spot in gravity array
    d_lambda[i] = quad(integrand_lambda, 1/(1+z[i]), 1, args = (H,c,O))[0] # same as above but for ΛCDM instead

# the following is all self explanatory plotting
# note that savefig must come before show in order to save the plot

plt.plot(z, d_grav, color = 'b', label = 'Modified Gravity')
plt.plot(z, d_lambda, linestyle = '--', color = 'r', label = 'ΛCDM')
plt.ylabel('Luminosity Distance (MPc)')
plt.xlabel('Redshift')
plt.legend()
plt.savefig('z_ldist_grav.png')
plt.show()
