import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parameters
lambda_10 = 10  # Calls per hour for simulation 1
lambda_15 = 15  # Calls per hour for simulation 2

k_values = np.arange(0, 11)  # Number of calls from 0 to 10
k_values1 = np.arange(0, 16)

# Calculate PMF using Poisson distribution
pmf_5 = poisson.pmf(k_values, 5)
pmf_10 = poisson.pmf(k_values, lambda_10)
pmf_15 = poisson.pmf(k_values1, lambda_15)

# Print probabilities
print("Simulation 1 - 10 calls per hour:")
for k, p in zip(k_values, pmf_10):
    print(f"P(X = {k}): {p:.6f}")

print("\nSimulation 2 - 15 calls per hour:")
for k, p in zip(k_values1, pmf_15):
    print(f"P(X = {k}): {p:.6f}")

print("\nSimulation 3 - 5 calls per hour")
for k, p in zip(k_values, pmf_5):
    print(f"P(X = {k}): {p:.6f}")

# Plot PMFs
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.bar(k_values, pmf_10)
plt.title("PMF - 10 Calls per Hour")
plt.xlabel("Number of Calls")
plt.ylabel("Probability")

plt.subplot(1, 2, 2)
plt.bar(k_values1, pmf_15)
plt.title("PMF - 15 Calls per Hour")
plt.xlabel("Number of Calls")
plt.ylabel("Probability")

plt.tight_layout()
plt.show()


'''

def poisson_pmf(x, lambd):
    return (math.exp(-lambd) * (lambd**x)) / math.factorial(x)
'''