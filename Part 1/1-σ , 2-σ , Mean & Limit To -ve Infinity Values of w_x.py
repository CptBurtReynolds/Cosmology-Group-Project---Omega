import scipy.integrate as integral
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


# This Piece of Code Is Designed Firstly To Integrate the Fuction g(a) For Various Values of Omega_m_0 & w_x , and Then To Use These
                                                                            #   Values To Plot Values of t_0 Where t_0 = 1/H_0*f(a)

w_x = np.arange(-1.35,0.01,0.05)
O = np.arange(0.2,1.0,0.01)
t0 = np.zeros((len(w_x),len(O)))
h0 = 0.07474032
def integrand(a,O,w_x):
    return ((O*(a**(-1)-a**(-(1+3*w_x)))+a**(-(1+3*w_x)))**(-1/2))      # Here the Function That Is Being Integrated Over Is Defined.



y = np.zeros_like(O)

for i in range(len(O)):
    y[i] = 2/(3*h0*(O[i])**(0.5))      # This Creates a Plot For the Theoretical Minimum Value of w_X   i.e. When w_X --> -∞



for i in range(len(w_x)):
    for j in range(len(O)):
    
    
        t0[i][j]= (quad(integrand,0,1,args=(O[j],w_x[i])) [0])/h0      # This "for" 'Loop' Integrates the Function Over the Desired Ranges
                                                                                                            #    For All Values of w_x



t_two_sigma_minus = 10.6                # IMPORTANT VALUES: For 1+- & 2+- S.D.s & For the Mean 't0'
t_one_sigma_minus = 11.7
tmean = 12.8
t_one_sigma_plus = 13.9
t_two_sigma_plus = 15.0


t_2sig_minus = np.zeros_like(O)         # This Block Plots a Constant Horizontal Line For 't0 = 10.6 Gyrs'
for i in range (len(O)):
    t_2sig_minus[i] = t_two_sigma_minus
plt.plot(O, t_2sig_minus, 'm:', alpha = 0.5)


t_1sig_minus = np.zeros_like(O)         # This Block Plots a Constant Horizontal Line For 't0 = 11.7 Gyrs'
for i in range (len(O)):
    t_1sig_minus[i] = t_one_sigma_minus
plt.plot(O, t_1sig_minus, 'm--', alpha = 0.5)


t_mean = np.zeros_like(O)               # This Block Plots a Constant Horizontal Line For the Mean 't0 = 12.8 Gyrs'
for i in range (len(O)):
    t_mean[i] = tmean
plt.plot(O, t_mean, 'm-', alpha = 0.5)


t_1sig_plus = np.zeros_like(O)          # This Block Plots a Constant Horizontal Line For 't0 = 13.9 Gyrs'
for i in range (len(O)):
    t_1sig_plus[i] = t_one_sigma_plus
plt.plot(O, t_1sig_plus, 'm--', alpha = 0.35)


t_2sig_plus = np.zeros_like(O)          # This Block Plots a Constant Horizontal Line For 't0 = 15.0 Gyrs'
for i in range (len(O)):
    t_2sig_plus[i] = t_two_sigma_plus 
plt.plot(O, t_2sig_plus, 'm:', alpha = 0.5)



O_two_sigma_minus = 0.25                # IMPORTANT VALUES: For 1+- & 2+- S.D.s & For the Mean 'O_m_0'
O_one_sigma_minus = 0.30
Omean = 0.35
O_one_sigma_plus = 0.40
O_two_sigma_plus = 0.45


O_2sig_minus = np.zeros_like(t0)        # This Block Plots a Constant Vertical Line For 'O_m_0 = 0.25'
for i in range (len(t0)):
    O_2sig_minus[i] = O_two_sigma_minus
plt.plot(O_2sig_minus, t0, 'k:', alpha = 0.15)


O_1sig_minus = np.zeros_like(t0)        # This Block Plots a Constant Vertical Line For 'O_m_0 = 0.30'
for i in range (len(t0)):
    O_1sig_minus[i] = O_one_sigma_minus          
plt.plot(O_1sig_minus, t0, 'k--', alpha = 0.15)


O_mean = np.zeros_like(t0)              # This Block Plots a Constant Vertical Line For 'O_m_0 = 0.35'
for i in range (len(t0)):
    O_mean[i] = Omean
plt.plot(O_mean, t0, 'k-', alpha = 0.15)


O_1sig_plus = np.zeros_like(t0)         # This Block Plots a Constant Vertical Line For 'O_m_0 = 0.40'
for i in range (len(t0)):
    O_1sig_plus[i] = O_one_sigma_plus
plt.plot(O_1sig_plus, t0, 'k--', alpha = 0.15)


O_2sig_plus = np.zeros_like(t0)         # This Block Plots a Constant Vertical Line For 'O_m_0 = 0.45'
for i in range (len(t0)):
    O_2sig_plus[i] = O_two_sigma_plus
plt.plot(O_2sig_plus, t0, 'k:', alpha = 0.15)




plt.plot(O,y, 'r-', color = 'red', label = 'w_x → -∞')

plt.plot(O,t0[0], label = 'Mean of w_x = -1.35')
plt.plot(O,t0[16], color = 'orange', label = '1-σ of w_x = -0.55')
plt.plot(O,t0[22], color = 'green', label = '2-σ of w_x = -0.25')



plt.scatter(0.35, 12.8, marker = 'o', color = 'magenta')       # These Plot Marks & Label At Specific Points On the Plot That Will Be Used For the Analysis
plt.text(0.323, 12.35, "M")

plt.scatter(0.3, 11.7, marker = 'o', color = 'magenta')
plt.text(0.275, 11.3, "A")

plt.scatter(0.4, 13.9, marker = 'o', color = 'magenta')
plt.text(0.375, 13.45, "A")

plt.scatter(0.25, 10.6, marker = 'o', color = 'magenta')
plt.text(0.225, 10.2, "B")

plt.legend()
plt.ylabel('t_0')
plt.xlabel('Omega_m_o')
plt.show()