import scipy.integrate as integrate
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import quad

z = np.arange(0.01,2.01,0.01) # creates an array of z values
d_grav = np.zeros_like(z) # creates array of zeros with same layout as z
d_lambda = np.zeros_like(z) # same as above 
sig_1 = np.zeros_like(z) # same as above 
sig_2 = np.zeros_like(z) # same as above 

def integrand_grav(a,H,c,O): # Function to perform integration required to calculate luminosity distance for a given redshift for DGP modified gravity model
    return (2*c)/( H * np.float_power(a,2) * ( (1-O) + np.sqrt( np.float_power((1-O),2) + 4 * O * np.float_power(a, -3) ) ) )

def integrand_lambda(a,H,c,O): # Similar to the above function but for the more simple ΛCDM model 
    return c/(H * np.float_power(a,2) * np.sqrt(1-O+O*np.float_power(a,-3)))
# float_power had to be used in the integration functions to avoid an error with raising floats to a power using standard power functions

for i in range(len(z)):
    c = 3e5 # defines constants
    H = 67.81
    O = 0.308

    # 0 index used for integration since it returns a pair of values, integration result and error on the result
    # these errors are so small for this integration they are being ignored, the errors are of the order of 10^-16
    
    d_grav[i] = quad(integrand_grav, 1/(1+z[i]), 1, args = (H,c,O))[0] # assigns the integration result to the correct spot in gravity array
    d_lambda[i] = quad(integrand_lambda, 1/(1+z[i]), 1, args = (H,c,O))[0] # same as above but for ΛCDM instead
    
    sig_1[i] = 0.0018 # sigma values are constant so no calculation required
    sig_2[i] = 0.0036

delta_d = abs(d_lambda-d_grav)/d_grav # creates an array of fractional difference between both models
# the following is plotting
plt.plot(z, delta_d, 'b', label = 'Fractional Difference')
plt.plot(z, sig_1, linestyle =  '--', color = 'r', label = 'WFIRST 1σ')
plt.plot(z, sig_2, linestyle =  '-.', color = 'r', label = 'WFIRST 2σ' )
plt.xlabel('Redshift')
plt.ylabel('Fractional Difference')
plt.legend()
plt.savefig('z_frac_grav.png')
plt.show()
