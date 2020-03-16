import matplotlib.pyplot as plt
import numpy as np
import math

z=np.arange(0.5,2.1,0.2)
lamb=[-1]*len(z)
error1=np.sqrt(0.002**2 +(1-1/(1+z))*0.1**2)
error2=np.sqrt(0.004**2 +(1-1/(1+z))*0.2**2)
#plt.plot(-0.934+(1-(1/(1+z)))*0.18, z)
#fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)
eb2=plt.errorbar(-0.934+(1-(1/(1+z)))*0.18, z, xerr=error2, color='b', linestyle='dotted', label=r'$2\sigma$')
eb1=plt.errorbar(-0.934+(1-(1/(1+z)))*0.18, z, xerr=error1, color='b', linestyle='-.', label=r'$1\sigma$')
eb3=plt.errorbar(lamb,z, color='r', label="cosmological constant")
#plt.plot(eb3)
#ax0.legend()
#eb1[-1][0].set_linestyle('--')
eb2[-1][0].set_linestyle('dotted')

plt.xlabel(r'$\omega_X$')
plt.ylabel("z")

#plt.plot(lamb,z, color ='coral',label="cosmological constant")
plt.legend(handles=[eb1,eb2,eb3])
plt.savefig('sigma errors.png')
plt.show()
