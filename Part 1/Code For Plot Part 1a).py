import math
import numpy as np
import matplotlib.pyplot as plt     # This is Equivalent To: "from matplotlib import pyplot as plt"
                                    # Matplotlib = a 'Package' ; Pyplot = a 'Module' (i.e. Subpackage) of Matplotlib


H0_Per_Gyr = 0.07474032       # Value of Hubble Constant At Present In Units of Gyrs^(-1)
                                    # Such Unit Conversion Was Made To Have More Intuitive Plot Axis For 't0'

OLambda0 = np.arange(0.01, 1.0, 0.01)     # OLambda0 = Density Parameter of Dark Energy (Lambda) At Present
                            
            # "np.arange" --> Creates Matrix of Values
            # Stated Range of Values For 'OLambda0' (<Min. Value>, <Max. Value (BUT NOT Included)>, <Interval Steps Between Values>)
            # Range Does Not Start At '0' & Does Not End Up At '1' Because Want To Avoid Equation Being 'Undefined'
            # Such Small Interval Steps To Smoothen Out the Plot-Curve As Much As Possible

t0 = np.zeros_like(OLambda0)     # Theoretical Age of the Universe At Present
                                
                        # "np.zeros_like(<Variable Represented As Matrix>)" --> Makes the New Variable a Full 0-Matrix of Length 
                        #                               (i.e. Same Number of Entries) of An Older Variable Represented As a Matrix


for i in range(len(OLambda0)):
    t0[i] = ((2*math.log((1+np.sqrt(OLambda0[i]))/(np.sqrt(1-OLambda0[i]))))/(3*H0_Per_Gyr*np.sqrt(OLambda0[i])))
    
                            # Equation For Theoretical Age of the Universe At Present
                            # A "For Loop" Is Performed To Iterate Through Every Entry In the 'OLambda0' Matrix,
                            #                Place It In the Equation & Obtain a 1-To-1 Mapping For Value of 't0'
                            # "math.log()" With NO Specified Base = ln  (i.e. Natural Logarithm)
                            # "math.sqrt()" = Square Root
                            
plt.plot(OLambda0, t0, 'b-', label = 't_0 vs. Ω_Λ_0 Curve')        # 'b-' = Blue Solid-Line
plt.ylabel('t_0 (Gyrs)')      # Inserts the y-Axis Label
plt.xlabel('Ω_Λ_0')    # Inserts the x-Axis Label


t_two_sig_minus = 10.6            # IMPORTANT VALUES: For 1+- & 2+- S.D.s & For the Mean 't0'
t_one_sig_minus = 11.7
t_mean = 12.8
t_one_sig_plus = 13.9
t_two_sig_plus = 15.0


t_2sig_minus = np.zeros_like(OLambda0)          # This Block Plots a Constant Horizontal Line For 't0 = 10.6 Gyrs'
for i in range(len(OLambda0)):
    t_2sig_minus[i] = t_two_sig_minus
plt.plot(OLambda0, t_2sig_minus, 'r:', alpha = 0.5 , label = '2-σ of t_0')      # "alpha = #" Makes Curve Fainter


t_1sig_minus = np.zeros_like(OLambda0)          # This Block Plots a Constant Horizontal Line For 't0 = 11.7 Gyrs'
for i in range(len(OLambda0)):
    t_1sig_minus[i] = t_one_sig_minus
plt.plot(OLambda0, t_1sig_minus, 'r--', alpha = 0.5 , label = '1-σ of t_0')


t_mean_ = np.zeros_like(OLambda0)                # This Block Plots a Constant Horizontal Line For the Mean 't0 = 12.8 Gyrs'
for i in range(len(OLambda0)):
    t_mean_[i] = t_mean
plt.plot(OLambda0, t_mean_, 'r-', alpha = 0.5 , label = 'Mean of t_0')


t_1sig_plus = np.zeros_like(OLambda0)           # This Block Plots a Constant Horizontal Line For 't0 = 13.9 Gyrs'
for i in range(len(OLambda0)):
    t_1sig_plus[i] = t_one_sig_plus
plt.plot(OLambda0, t_1sig_plus, 'r--', alpha = 0.5)


t_2sig_plus = np.zeros_like(OLambda0)           # This Block Plots a Constant Horizontal Line For 't0 = 15.0 Gyrs'
for i in range(len(OLambda0)):
    t_2sig_plus[i] = t_two_sig_plus
plt.plot(OLambda0, t_2sig_plus, 'r:', alpha = 0.5)




O_two_sig_minus = 0.416124            # IMPORTANT VALUES: For 1+- & 2+- S.D.s & For the Mean 'OLambda0'
O_one_sig_minus = 0.573958
O_mean = 0.690000
O_one_sig_plus = 0.772752
O_two_sig_plus = 0.827323


O_2sig_minus = np.zeros_like(t0)           # This Block Plots a Constant Vertical Line For 'OLambda0 = 0.45'
for i in range(len(t0)):
    O_2sig_minus[i] = O_two_sig_minus
plt.plot(O_2sig_minus, t0, 'g:', alpha = 0.5 , label = '2-σ of Ω_Λ_0')


O_1sig_minus = np.zeros_like(t0)           # This Block Plots a Constant Vertical Line For 'OLambda0 = 0.55'
for i in range(len(t0)):
    O_1sig_minus[i] = O_one_sig_minus
plt.plot(O_1sig_minus, t0, 'g--', alpha = 0.5 , label = '1-σ of Ω_Λ_0')


O_mean_ = np.zeros_like(t0)           # This Block Plots a Constant Vertical Line For 'OLambda0 = 0.65'
for i in range(len(t0)):
    O_mean_[i] = O_mean
plt.plot(O_mean_, t0, 'g-', alpha = 0.5 , label = 'Mean of Ω_Λ_0')


O_1sig_plus = np.zeros_like(t0)           # This Block Plots a Constant Vertical Line For 'OLambda0 = 0.75'
for i in range(len(t0)):
    O_1sig_plus[i] = O_one_sig_plus
plt.plot(O_1sig_plus, t0, 'g--', alpha = 0.5)


O_2sig_plus = np.zeros_like(t0)           # This Block Plots a Constant Vertical Line For 'OLambda0 = 0.85'
for i in range(len(t0)):
    O_2sig_plus[i] = O_two_sig_plus
plt.plot(O_2sig_plus, t0, 'g:', alpha = 0.5)


plt.scatter(0.00806452, 8.98628, marker = 'o', color = 'magenta')       # These Plot Marks & Label At Specific Points On the Plot That Will Be Used For the Analysis
plt.text(0.01, 9.35, "A")

plt.scatter(0.416124, 10.6, marker = 'o', color = 'magenta')
plt.text(0.42, 10.9, "B")

plt.scatter(0.827323, 15, marker = 'o', color = 'magenta')
plt.text(0.80, 15.3, "B")

plt.scatter(0.772752, 13.9, marker = 'o', color = 'magenta')
plt.text(0.78, 13.15, "C")

plt.scatter(0.573958, 11.7, marker = 'o', color = 'magenta')
plt.text(0.586, 11, "C")

plt.scatter(0.69, 12.8, marker = 'o', color = 'magenta')
plt.text(0.66, 13.05, "M")


plt.legend()      # Inserts Automatically the Plot's Legend

plt.show()      # Creates/Visualises Plot