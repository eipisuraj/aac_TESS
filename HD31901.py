#Import necessary libraries
import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from astropy.timeseries import LombScargle
from scipy.optimize import curve_fit

# Search for HD 31901 in TESS database
search_result = lk.search_lightcurve("HD 31901", mission="TESS")
print(search_result) 

# 9 objects are available --> we will do analysis for first entry
# Download the first available light curve
lc = search_result.download()
lc.plot(title="Raw Light Curve of HD 31901")

# Removing outliners(NaN values) and Normalizing
lc_clean = lc.remove_nans().remove_outliers(sigma=5).normalize()
lc_clean.plot(title="Cleaned & Normalized Light Curve of HD 31901")

# Convert time and flux to unitless NumPy arrays
time_days = lc_clean.time.value  # Remove time units (days)
flux = lc_clean.flux.value  # Remove flux units

# Compute Lomb-Scargle power spectrum
frequency, power = LombScargle(time_days, flux).autopower(
    minimum_frequency=5, maximum_frequency=100
)

# Convert frequency to period (P = 1/f)
period = 1 / frequency

# Plot the power spectrum
plt.figure(figsize=(8, 5))
plt.plot(period, power, 'k')
plt.xlabel("Period (days)")
plt.ylabel("Power")
plt.xlim([0.01, 0.1])  # Expected period range for Delta Scuti
plt.title("Lomb-Scargle Periodogram of HD 31901")
plt.show()


