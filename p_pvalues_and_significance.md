## P: P-values and Significance

Very often we want to ascertain the compatibility (or lack there of) between our observation and some other hypothesis.
This is normally quantified using a $`p`$-value which determines the probability of seeing the observed outcome or worse.
This is a hypothesis test which is not the same as a goodness of fit test.

The p-value can sometimes be obtained from formulae, or in most cases computed using toy Monte Carlo, in which toys are generated from the null-hypothesis (the hypothesis we want to test against), and then finding the fraction of toys which are as far away, or further away, from the observation.
The p-value is the fundamental quantity but the convention is often to interpret the p-value in terms of a more natural quantity: the significance (usually called $`Z`$ or sometimes the $`Z`$-score).
We then have conventions in particle physics for what language is used for certain $`Z`$-score thresholds:
 - $`3\sigma`$ allows one to write "evidence"
 - $`5\sigma`$ allows one to write "observation" or "discovery"
 - when setting limits the convention is to use $`p < 0.05`$ and state "exclusion at the 95% confidence level (CL)"

### Computing p-values

The observed $`p`$-value is a measure of the compatibility of the data with the tested hypothesis.
It is the probability, under the assumption of the null hypothesis, $`H_{0}`$, of finding data of equal or greater incompatibility with the predictions of $`H_0`$.
In order to compute the $`p`$-value you need to find the probability distribution of your test-statistic under the null hypothesis (either with use of a formulae or generated with toys).
The test-statistic can really be anything (a poor choice will simply give you suboptimal statistical power) but it should take larger values for stronger evidence of departure from the null. Commonly it is either
- simply a parameter of your fit, which might be the signal yield or a ratio of yields or perhaps the time-dependent oscillation rate between meson flavours, or
- a log-likelihood-ratio (LLR) between the global best-fit and the null hypotheis. The [Neyman-Pearson lemma](https://en.wikipedia.org/wiki/Neyman–Pearson_lemma) states that the LLR is the most powerful hypothesis test that you can do (at least for two so-called simple hypotheses), which is why the LLR is very common for hypothesis tests. 

Here is an example where the test-statistic is simply the number of signal events seen, called $`N_s`$.
I can generate the test-statistic distribution by throwing background only toys and fitting them for the amount of signal (shown in blue).
The amount I see in my actual dataset is given by the orange line.
Normally, when trying to reject a hypothesis when performing searches for signal, we usually only consider the one-sided tail probaility.
In other words the $`p`$-value quantifies the chances of seeing a signal as big or larger than the one I observe.
This means that downward fluctutatioins of the background do not serve as evidence against the background and similarly upward fluctuations of the signal will not be considered as evidence against the signal.
Thus the $`p`$-value is the fraction of toys with $`N_s > N_s^{\rm obs}`$.

<img src="resources/p_null.png" width=480>

Notice, that in this case the test-statistic looks to be fairly Gaussian distributed (it is infact a counting experiment so this is a Poisson distribution with a large expectation) but the test-statistic will not necessarily be distributed like this.

As another example we could consider a measurement of some parameter, this time a weak phase, called $`\phi`$, where the null-hypothesis expectation is $`\phi=0`$ (no $`C\!P`$-violation).
In this case we are interested in fluctuations on both sides of the null expectation (either a very positive or a very negative phase) so our $`p`$-value contains both sides of the distribution and is the fraction of toys with $`|\phi|>|\phi^{\rm obs}|`$ (note the symmetrisation with the modulus here only works when the null expectation is zero).

<img src="resources/p_measurement.png" width=480>

Another very common approach is making use of the LLR as the test-statistic.
Notice that in this case the test-statistic distribution will be automatically symmetrised because the likelihood does not care about the direction of a fluctuation.
So in the first example above, if we use the LLR and ask what fraction of toys have an LLR worse than the observation we will include both positive and negative fluctuations of the signal.
Therefore, normally when performing signal searches the LLR test-statistic is defined so that the LLR is set to zero for negative fluctuations of the signal:
```math
q(N_s) = \begin{cases} -2 \ln \lambda(0) & \text{if $\hat{N}_{s}>0$} \\
 0 & \text{otherwise}
 \end{cases}
 ```
 where $`\lambda(0)`$ is the likelihood ratio between the null hypothesis point and the best fit point, $`\mathcal{L}(N_s=0) / \mathcal{L}(N_s=\hat{N}_s)`$.
 The difference between these is shown below, on the left we do not set the LLR=0 for negative fluctuations (and we end up with a $`p`$-value twice as large as in the first plot above), on the right we do set the LLR=0 for negative fluctuations and then recover the same $`p`$-value.
 **So, please make sure you keep this in mind. It is not of huge concern which p-value you compute providing you explain clearly in your publication what you have done. Normally for signal searches and observation of new resonances the one-sided approach is used (the convention adopted by ATLAS and CMS as well as in the PDG). For measurements, you should make a choice depending on what sort of measurement it is and if you really are equally surprised by fluctuations on either side.**

<img src="resources/p_null_dll.png" width=480>
<img src="resources/p_null_dll_zero.png" width=480>

### Converting p-values into significance or Z-score

Now that we have established how to compute the $`p`$-value, it is a custom (and some find this custom distasteful) to express the $`p`$-value as a significance. This is based upon the question of how many Gaussian $`\sigma`$ (standard deviations) is my observation from the null hypothesis expectation had the test statistic distribution been Gaussian. **One needs to be careful here because there are two ambiguous defintions: one-sided or two-sided.**
It seems to be uniformly agreed that the $`p`$-value is the meaningful quantity. The conversion into significance or $`Z`$-score some argue is just a matter of convention. I (Matt Kenzie) am of the view that it is more than convention, and that using the wrong conversion gives at best a misleading result (and at worst the wrong result).

#### One-sided conversion

For a one-sided $`p`$-value, e.g. the typical search for a new resonance, then the $`p`$-value (had the test-statistic been Gaussian distributed) would be
```math
p = \displaystyle\int_{Z}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = 1 - \Phi(Z)
```
where $`\Phi`$ is the cummalitive density function (c.d.f) of the normal distribution. The significance can therefore be computed using the inverse c.d.f (sometimes also called the "percentile point function")
```math
Z = \Phi^{-1}(1-p)
```
**This is the one-sided conversion.** Notice that if the data comes out exactly at the background-only expectation (null-hypothesis) then your $`p`$-value in this case will be $`p=0.5`$. Thus you want a conversion that will give you zero significance for such an observation, and that conversion is the one-sided one.

<img src="resources/p_conversion1.png" width=480>

In this case a significance of $`Z=5`$ corresponds to $`p=2.87 \times 10^{-7}`$. Note, that in this case a significance of $`Z=1`$ does not correspond to $`p=1-0.683`$. Some generic tools for computing the one-sided significance from the p-value and vice-versa:

```python
from scipy.stats import norm
Z = 5
p = 1 - norm.cdf(Z)
print(p)
>>> 2.866515719235352e-07
Z = norm.ppf(1-p)
print(Z)
>>> 4.999999999970176
```

```python
from ROOT import RooStats
Z = 5
p = RooStats.SignificanceToPValue(Z)
print(p)
>>> 2.866515718791945e-07
Z = RooStats.PValueToSignificance(p)
print(Z)
>>> 5.0
```

#### Two-sided conversion

For the case where you are comparing a measurement with the null point and you think it's significant if they differ in either direction, you then would need to use a two-sided conversion.
In this case the $`p`$ value (had the test-statistic been Gaussian distributed) would be
```math
\begin{aligned}
p & =  \displaystyle\int_{-\infty}^{-Z} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx + \displaystyle\int_{Z}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx \\
  & =  2\displaystyle\int_{Z}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx \\
	& =  2(1 - \Phi(Z))
	\end{aligned}
```
meaning that the significance is
```math
Z = \Phi^{-1}(1-p/2)
```

**This is the two-sided conversion.** Notice that if the data comes out exactly at the background-only expectation (null-hypothesis) then your $`p`$-value in this case will be $`p=1`$. Thus you want a conversion that will give you zero significance for such an observation, and that conversion is the two-sided one.

<img src="resources/p_conversion2.png" width=480>

In this case a significance of $`Z=5`$ corresponds to $`p=5.73 \times 10^{-7}`$. Note, that in this case a significance of $`Z=1`$ does correspond to $`p=1-0.683`$. Some generic tools for computing the two-sided significance from the p-value and vice-versa (you can cleary also use the same as those above with $`p\to p/2`$):

```python
from scipy.stats import chi2
Z = 5
p = 1 - chi2.cdf(Z**2,1)
print(p)
>>> 5.733031438470704e-07
Z = (chi2.ppf(1-p,1))**0.5
print(Z)
>>> 5.000000000007513
```

```python
from ROOT import TMath
Z = 5
p = TMath.Prob(Z**2,1)
print(p)
>>> 5.733031437583875e-07
Z = TMath.ChisquareQuantile(1-p,1)**0.5
print(Z)
>>> 5.000000000010241
```

#### On the use of which conversion

The statistics group conveners had some discussion with Glen Cowan on the topic who pointed out another argument which explains which conversion rule to use.
If you use $`Z=\Phi^{-1}(1-p)`$ for the one-sided problem and $`Z=\Phi^{-1}(1-p/2)`$ for the two-sided problem, then in both cases you asympotically recover that $`Z=\sqrt{q_0}`$, where $`q_0`$ is the relevant LLR test-statistic for the null hypothesis:

**One-sided problem**:
```math
q_0 = \begin{cases} -2\ln \lambda(0) & \text{for $\hat{\mu}>0$} \\
 0 & \text{otherwise} \end{cases}
 ```
 **Two-sided problem**:
 ```math
 q_0 = -2\ln\lambda(0)
 ```


This gives the expected result that the significance squared, or variance, follows a $`\chi^2`$ distribution.
Moreover, this is a demonstration that the methodology outlined here obeys [Wilks' theorem](https://en.wikipedia.org/wiki/Wilks%27_theorem) which states that:

*"As the sample size approaches infinity, the distribution of the test statistic, $`q=-2\log\lambda`$, asympotically approaches the chi-squared, $`\chi^2`$, distribution under the null hypothesis"*

Consequently, if you use the wrong conversion then you violate Wilks' theorem, hence my assertion that the wrong conversion is more than just a convention.
