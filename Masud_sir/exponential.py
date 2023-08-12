import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Average time between waves (in days)
avg_time_between_waves = 100

# Calculate the rate parameter (λ) for the exponential distribution
rate_parameter = 1 / avg_time_between_waves

# Time threshold for the next wave (in days)
threshold = 120

# Calculate the probability that the next wave occurs within 120 days
probability_within_120 = expon.cdf(threshold, scale=1/rate_parameter)

# Calculate the probability that it will take more than 120 days for the next wave
probability_more_than_120 = 1 - probability_within_120

print(f"Probability of more than {threshold} days between waves: {probability_more_than_120:.4f}")

# Simulate Exponential distributions with different rate parameters
rate_parameters = [0.5, 1.0, 2.0, 4.0]
num_simulations = 1000

simulated_times = {}

for rate in rate_parameters:
    simulated_times[rate] = np.random.exponential(scale=1/rate, size=num_simulations)

# Plot simulated distributions
plt.figure(figsize=(10, 6))

for rate in rate_parameters:
    plt.hist(simulated_times[rate], bins=30, density=True, alpha=0.6, label=f'Rate = {rate}')

plt.axvline(x=threshold, color='red', linestyle='--', label=f'Threshold ({threshold} days)')
plt.title("Simulated Exponential Distributions")
plt.xlabel("Time Until Next Wave (days)")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
