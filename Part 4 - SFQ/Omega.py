import matplotlib.pyplot as plt

a_range = 1/3
values = []
while a_range <1:
    values.append(a_range)
    a_range += 0.001
#range of a values    
omega_x = []
z = []
for i in values:
     z.append(1/i-1)
     omega_x.append(-1)     
plt.plot(z, omega_x, label = 'ΛCDM', linestyle = '--', color ='r')
#lambdaCDM and redshift
def omega_x_func(a):
    return -1 +(1)/(1+(a/0.5)**(1/0.33))
omega_x = []
for i in values:
     omega_x.append(omega_x_func(i))
plt.plot(z, omega_x, label = 'SFQ1')
#SFQ1
def omega_x_func(a):
    return -1 +(1)/(1+(a/0.23)**(1/0.33))
omega_x = []
for i in values:
     omega_x.append(omega_x_func(i))
plt.plot(z, omega_x, label = 'SFQ2')
#SFQ2
plt.xlabel('Redshift, z')
plt.ylabel('Dark Energy Barotropic Parameter, ω')
plt.legend()
plt.savefig('Omega.png', bbox_inches='tight')
plt.show()