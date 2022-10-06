# Random Walk 1D(To compute configuration average value)

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly


# N=Ensemble members,T=Total time steps
N,T=10000,1000
t=range(1,T+1)     # Time scale
# 2D array: Time axis along row ,each row is one configeration
walks=2*np.random.randint(2,size=(N,T))-1
# Compute the configeration average
positions=np.cumsum(walks,axis=1)
pos_sq=positions**2
mean_pos_sq=np.mean(pos_sq,axis=0)
rms=np.sqrt(mean_pos_sq)         # Root mean square distance
# values in LOG scale
t=np.log(t)
rms=np.log(rms)
# To fit log-values in linear scale
coeffs=poly.polyfit(t,rms,1)
rmsfit=poly.polyval(t,coeffs)
print (coeffs)

# To plot along with fitted curve
plt.plot(t,rms,'o',t,rmsfit,'-')
plt.xlabel('log(time)',fontsize=18)
plt.ylabel('log($R_(rms)$)',fontsize=18)
plt.title('Random walk in 1D',fontsize=20)
plt.show()









































































































