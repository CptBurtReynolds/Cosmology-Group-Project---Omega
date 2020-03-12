import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
#importing useful/required modules
H_0 = 67.81
Omega_lamb = 0.692
Omega_mat = 0.308
c = 2.998*10**8
#constants
a_range = 10/27
avalues = []
while a_range <= 5/6:
    avalues.append(a_range)
    a_range += 0.0001
#range of scale parameter (a) values. Again using 1/3 to 1, approx range of WFIRST
model2_omegax = np.zeros(len(avalues))
model3_omegax = np.zeros(len(avalues))
model1_dx = np.zeros(len(avalues))
model2_dx = np.zeros(len(avalues))
model3_dx = np.zeros(len(avalues))
model1_dl = np.zeros(len(avalues))
model2_dl = np.zeros(len(avalues))
model3_dl = np.zeros(len(avalues))
model2_frac_dl = np.zeros(len(avalues))
model3_frac_dl = np.zeros(len(avalues))
sigma1 = np.zeros(len(avalues))
sigma2 = np.zeros(len(avalues))
z = np.zeros(len(avalues))
for i in range(0,len(avalues)):
    z[i]=1/avalues[i] -1
#converting scale parameter array to redshift, to be used in plotting
omega_p = 0
omega_f = -1
tau = 0.33
model2_a_t = 0.5
model3_a_t = 0.23
#various model parameters defined. Can be changed for different models

def model1_integrand(a):
    return (1/a**2)*(Omega_mat*a**(-3)+Omega_lamb)**(-1/2)
#defining the d_x integral for cosmo const
for i in range(0,len(avalues)):
    I1 = integrate.quad(model1_integrand, avalues[i], 1)
    model1_dx[i]=(c*I1[0]/H_0)
    model1_dl[i]=(1/avalues[i]*model1_dx[i])
#integrating the d_x integral for the range of scale parameter values for cosmo const, and geting the luminosity distance for each a/z

def model2_omega_int(x):
    return (3/x)*(1+omega_f + (omega_p - omega_f)/(1 + (x/model2_a_t)**(1/tau)))
def model2_integrand(a):
    return (1/a**2)*(Omega_mat*a**(-3)+Omega_lamb*np.exp(-1*integrate.quad(model2_omega_int, 1, a)[0]))**(-1/2)
#defining the d_x integral for SFQ 1
for i in range(0,len(avalues)):
    I2 = integrate.quad(model2_integrand, avalues[i], 1)
    model2_dx[i]=(c*I2[0]/H_0)
    model2_dl[i]=(1/avalues[i]*model2_dx[i])
    model2_frac_dl[i] = abs((model2_dl[i] - model1_dl[i])/model2_dl[i])
    sigma1[i] = 0.0018
    sigma2[i] = 0.0036
#obtaining the dl values for SFQ 1 (model2) and then calculating the fractional deviation from LambdaCDM (model1)
plt.plot(z, model2_frac_dl, label = 'SFQ 1')
plt.plot(z, sigma1, label = '1σ error', linestyle = '--', color ='r')
plt.plot(z, sigma2, label = '2σ error', linestyle = '--', color ='c')
plt.xlabel('Redshift, z')
plt.ylabel('Fractional Deviation from ΛCDM, Δd_L/d_L')
plt.legend()
plt.savefig('Frac_Devia_SFQ1.png', bbox_inches='tight')
plt.show()

def model3_omega_int(x):
    return (3/x)*(1+omega_f + (omega_p - omega_f)/(1 + (x/model3_a_t)**(1/tau)))
def model3_integrand(a):
    return (1/a**2)*(Omega_mat*a**(-3)+Omega_lamb*np.exp(-1*integrate.quad(model3_omega_int, 1, a)[0]))**(-1/2)
#defining the d_x integral for SFQ 1
for i in range(0,len(avalues)):
    I3 = integrate.quad(model3_integrand, avalues[i], 1)
    model3_dx[i]=(c*I3[0]/H_0)
    model3_dl[i]=(1/avalues[i]*model3_dx[i])
    model3_frac_dl[i] = abs((model3_dl[i] - model1_dl[i])/model3_dl[i])
#obtaining the dl values for SFQ 2 (model3) and then calculating the fractional deviation from LambdaCDM (model1)
plt.plot(z, model3_frac_dl, label = 'SFQ 2', color = 'darkorange')
plt.plot(z, sigma1, label = '1σ error', linestyle = '--', color ='r')
plt.plot(z, sigma2, label = '2σ error', linestyle = '--', color ='c')
plt.xlabel('Redshift, z')
plt.ylabel('Fractional Deviation from ΛCDM, Δd_L/d_L')
plt.legend()
plt.savefig('Frac_Devia_SFQ2.png', bbox_inches='tight')
plt.show()




