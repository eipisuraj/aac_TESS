What we did :

1) Selected a Delta Scruti type star "HD 31901" to study its pulsationg period and concerning properties

2) used following python libraries for analysis
Lightkurve → To access, clean, and analyze TESS light curves.
NumPy → For numerical operations like handling arrays and filtering data.
Matplotlib → To visualize light curves and periodograms.
Scipy.signal (find_peaks) → To identify peaks in light curves or periodograms.
Astropy.timeseries (LombScargle) → To perform frequency analysis and detect periodic signals.
Scipy.optimize (curve_fit) → To fit models (e.g., sinusoidal) to periodic data.

3 )Then i got 9 files when we searched for TESS data of HD31901 object / of which here for simplicity i analysed first file 

4) In next step i plotted the raw data as available / further with help of lightkurve library functions normalized the data which is distorted due to satellite repositioning and jitters

5) Also to maintain any possible errors due to wrong dimension converted the time and flux into unitless numpy arrays

6) Then i computed Lomb-Scargle power spectrum and plotted power verseus period plot
From which following conclusions may be drawn :
Key Observations
 1)Strong Peak at ~0.04 days (~57.6 minutes)
 2)The highest peak in the power spectrum indicates the dominant period of variability in the star's brightness.
 3)This suggests that HD 31901 has a periodic pulsation around 0.04 days.
 4) Multiple Small Peaks at Lower Periods / These could correspond to secondary pulsation modes or harmonics of the primary period.
 5) Delta Scuti stars often exhibit multiple pulsation frequencies due to non-radial oscillations.
 6) The Peak is Very Sharp and Distinct / This suggests a strong, well-defined pulsation rather than random noise / A high-power peak means the period is statistically significant.
