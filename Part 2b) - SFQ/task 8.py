import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
#importing useful/required modules
H_0 = 67.81
Omega_lamb = 0.692
Omega_mat = 0.308
c = 2.998*10**8
#constants
a_t_range = 0.00000001
a_t_values = []
while a_t_range <= 1:
    a_t_values.append(a_t_range)
    a_t_range += 0.0001
    
a_range = 10/27
avalues = []
while a_range <= 5/6:
    avalues.append(a_range)
    a_range += 0.001
#range of scale parameter (a) values. Again using 1/3 to 1, approx range of WFIRST
z = np.zeros(len(avalues))
sigma1 = np.zeros(len(avalues))
sigma2 = np.zeros(len(avalues))
lambda_dx = np.zeros(len(avalues))    
lambda_dl = np.zeros(len(avalues))    
omega_p = 0
omega_f = -1
tau = 0.33    
truth = 0
#various model parameters defined    
def lambda_integrand(a):
    return (1/a**2)*(Omega_mat*a**(-3)+Omega_lamb)**(-1/2)
#defining the d_x integral for cosmo const
for i in range(0,len(avalues)):
    z[i]=1/avalues[i] -1
    sigma1[i] = 0.0018
    sigma2[i] = 0.0036
    I1 = integrate.quad(lambda_integrand, avalues[i], 1)
    lambda_dx[i]=(c*I1[0]/H_0)
    lambda_dl[i]=(1/avalues[i]*lambda_dx[i])
#integrating the d_x integral for the range of scale parameter values for cosmo const, and geting the luminosity distance for each a/z, and obtaining the z values    

    
    
for i in range(0,len(a_t_values)):
    SFQ_omegax = np.zeros(len(avalues))    
    SFQ_dx = np.zeros(len(avalues))    
    SFQ_dl = np.zeros(len(avalues))
    SFQ_frac_dl = np.zeros(len(avalues))    
    SFQ_a_t = a_t_values[i]
    #various model parameters defined
    print(i)
    

    def SFQ_omega_int(x):
        return (3/x)*(1+omega_f + (omega_p - omega_f)/(1 + (x/SFQ_a_t)**(1/tau)))
    def SFQ_integrand(a):
        return (1/a**2)*(Omega_mat*a**(-3)+Omega_lamb*np.exp(-1*integrate.quad(SFQ_omega_int, 1, a)[0]))**(-1/2)
    #defining the d_x integral for SFQ 1
    for j in range(0,len(avalues)):
        I2 = integrate.quad(SFQ_integrand, avalues[j], 1)
        SFQ_dx[j]=(c*I2[0]/H_0)
        SFQ_dl[j]=(1/avalues[j]*SFQ_dx[j])
        SFQ_frac_dl[j] = abs((SFQ_dl[j] - lambda_dl[j])/SFQ_dl[j])
        
        if SFQ_frac_dl[j] <= 0.0036:
            truth = 0
            break
        else:
            truth = 1
    if truth == 1:
        print(SFQ_a_t)
        break
#obtaining the dl values for SFQ 1 (SFQ) and then calculating the fractional deviation from LambdaCDM (lambda)




