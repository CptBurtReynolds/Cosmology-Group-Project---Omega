import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
H_0 = 67.81
Omega_lamb = 0.692
Omega_mat = 0.308
c = 2.998*10**8
#constants
a_range = 1/3
values = []
while a_range < 1:
    values.append(a_range)
    a_range += 0.0001
#range of scale parameter (a) values
d_x = np.zeros(len(values))
d_L = np.zeros(len(values))
z = np.zeros(len(values))
for i in range(0,len(values)):
    z[i]=1/values[i] -1
def integrand(a):
    return (1/a**2)*(Omega_mat*a**(-3)+Omega_lamb)**(-1/2)
#defining the d_x integral for cosmo const
for i in range(0,len(values)):
    I = integrate.quad(integrand, values[i], 1)
    d_x[i]=(c*I[0]/H_0)
    d_L[i]=(1/values[i]*d_x[i])
#integrating the d_x integral for the range of scale parameter values for cosmo const, and geting the luminosity distance for each a/z
plt.plot(z, d_L, label = 'ΛCDM', linestyle = '--', color ='r')
#plotting cosmo constant
omega_p = 0
omega_f = -1
tau = 0.33
a_t = 0.5
def nasty_int(x):
    return (3/x)*(1+omega_f + (omega_p - omega_f)/(1 + (x/a_t)**(1/tau)))
def integrand(a):
    return (1/a**2)*(Omega_mat*a**(-3)+Omega_lamb*np.exp(-1*integrate.quad(nasty_int, 1, a)[0]))**(-1/2)
#defining the d_x integral for SFQ 1
for i in range(0,len(values)):
    I = integrate.quad(integrand, values[i], 1)
    d_x[i]=(c*I[0]/H_0)
    d_L[i]=(1/values[i]*d_x[i])
plt.plot(z, d_L, label = 'SFQ 1')
#plotting SFQ 1
omega_p = 0
omega_f = -1
tau = 0.33
a_t = 0.23
def integrand(a):
    return (1/a**2)*(Omega_mat*a**(-3)+Omega_lamb*np.exp(-1*integrate.quad(nasty_int, 1, a)[0]))**(-1/2)
#defining the d_x integral for SFQ 2
for i in range(0,len(values)):
    I = integrate.quad(integrand, values[i], 1)
    d_x[i]=(c*I[0]/H_0)
    d_L[i]=(1/values[i]*d_x[i])
plt.plot(z, d_L, label = 'SFQ 2')
#plotting SFQ 2
plt.xlabel('Redshift, z')
plt.ylabel('Luminosity Distance, d_L (kpc)')
plt.legend()
plt.savefig('Lum_Dis.png', bbox_inches='tight')
plt.show()
