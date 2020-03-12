import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
#importing useful/required modules
H_0 = 67.81
Omega_lamb = 0.692
Omega_mat = 0.308
c = 2.998*10**8
#constants
a_range = 1/6
avalues = []
while a_range < 1:
    avalues.append(a_range)
    a_range += 0.0000001
#range of scale parameter (a) values. Note now between 1/6 and 1 instead of 1/3 and 1
model2_omegax = np.zeros(len(avalues))
model3_omegax = np.zeros(len(avalues))
model1_q = np.zeros(len(avalues))
model2_q = np.zeros(len(avalues))
model3_q = np.zeros(len(avalues))
z = np.zeros(len(avalues))
q_zerovalues = [2,2,2]
for i in range(0,len(avalues)):
    z[i]=1/avalues[i] -1
#converting scale parameter array to redshift, to be used in plotting
omega_p = 0
omega_f = -1
tau = 0.33
model2_a_t = 0.5
model3_a_t = 0.23
#various model parameters defined. Can be changed for different models
def model2_integrand(x):
    return (3/x)*(1+omega_f + (omega_p - omega_f)/(1 + (x/model2_a_t)**(1/tau)))
def model2_density(a):
    return np.exp(-1*integrate.quad(model2_density, 1, a)[0])
#SFQ 1, model 2 integrals + omegaX defined 
def model3_integrand(x):
    return (3/x)*(1+omega_f + (omega_p - omega_f)/(1 + (x/model3_a_t)**(1/tau)))
def model3_density(a):
    return np.exp(-1*integrate.quad(model3_integrand, 1, a)[0])
#SFQ 2, model 3 integrals + omegaX defined 
for i in range(0,len(avalues)):
    model1_q[i] = (1/2)*(1-3*Omega_lamb/(Omega_mat*avalues[i]**(-3) + Omega_lamb))
    if abs(model1_q[i-1]) < 0.0000003:
        q_zerovalues[0] = [model1_q[i-2], model1_q[i-1], model1_q[i], avalues[i-1], z[i-1]]
plt.plot(z, model1_q, label = 'ΛCDM', linestyle = '--', color = 'r')    
#calculating and plotting the cosmo constant (model1) deceleration parameter values for the range of a against the redshift
for i in range(0,len(avalues)):
    model2_omegax[i] = omega_f + (omega_p - omega_f)/(1 + (avalues[i]/model2_a_t)**(1/tau))
    I2 = integrate.quad(model2_integrand, 1, avalues[i])
    model2_q[i] = (1/2)*(1+3*model2_omegax[i]*Omega_lamb*np.exp(-1*I2[0])/(Omega_mat*avalues[i]**(-3) + Omega_lamb*np.exp(-1*I2[0])))
    if abs(model2_q[i-1]) < 0.000003:
        q_zerovalues[1] = [model2_q[i-2], model2_q[i-1], model2_q[i], avalues[i-1], z[i-1]]
plt.plot(z, model2_q, label = 'SFQ 1')
#calculating and plotting the SFQ1 (model2) deceleration parameter values for the range of a against the redshift
for i in range(0,len(avalues)):
    model3_omegax[i] = omega_f + (omega_p - omega_f)/(1 + (avalues[i]/model3_a_t)**(1/tau))
    I3 = integrate.quad(model3_integrand, 1, avalues[i])
    model3_q[i] = (1/2)*(1+3*model3_omegax[i]*Omega_lamb*np.exp(-1*I3[0])/(Omega_mat*avalues[i]**(-3) + Omega_lamb*np.exp(-1*I3[0])))
    if abs(model3_q[i-1]) < 0.0000003:
        q_zerovalues[2] = [model3_q[i-2], model3_q[i-1], model3_q[i], avalues[i-1], z[i-1]]
plt.plot(z, model3_q, label = 'SFQ 2')
#calculating and plotting the SFQ2 (model3) deceleration parameter values for the range of a against the redshift
plt.xlabel('Redshift, z')
plt.ylabel('Deceleration Parameter, q')
plt.legend()
plt.savefig('Decel_Param.png', bbox_inches='tight')
plt.show()
print(q_zerovalues)
