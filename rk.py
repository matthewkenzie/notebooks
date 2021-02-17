from scipy.stats import norm, chi2
import numpy as np

obs = [0.7,0.1]

def nll(exp, obsval, obserr):
  n = norm(obsval,obserr)
  return -2*n.logpdf(exp)

best_fit = obs[0]
sm = 1.

print( np.sqrt( nll(sm,*obs) - nll(best_fit,*obs) ) )

true_dist = norm(1,0.1)

toys = true_dist.rvs(size=100000)

toy_dlls = nll( sm, toys, 0.1 ) - nll( toys, toys, 0.1 )
data_dll = nll( sm, obs[0], 0.1 ) - nll( obs[0], obs[0], 0.1 )

frac_toys_above_data = len(toy_dlls[toy_dlls>data_dll]) / len(toy_dlls)
print(frac_toys_above_data)

pval     = frac_toys_above_data
pval_err = (pval * ( 1 - pval ) / len(toy_dlls) )**0.5

print(f'p-value = {pval} +/- {pval_err}')

sig_1side = chi2.ppf(1-pval/2,1)**0.5
sig_2side = chi2.ppf(1-pval,1)**0.5
print(sig_1side)
print(sig_2side)

import matplotlib.pyplot as plt

#plt.hist(toys, range=(0.5,1.5), bins=50 )
plt.hist(toy_dlls, range=(0,10), bins=50)
plt.plot( [data_dll,data_dll], [0,plt.ylim()[1]] )
plt.show()
