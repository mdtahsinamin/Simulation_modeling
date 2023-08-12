import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate a random sample from a normal distribution

sample_size = 1000
mean = 100
standard_deviation = 20

random_sample = np.random.normal(mean, standard_deviation, sample_size)

# Plot the histogram of the blood pressure distribution


# Plot the unimodal density curves

x = np.linspace(min(random_sample), max(random_sample), 200)
unimodal_curve = (1 / (standard_deviation * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * standard_deviation ** 2))

# Plot the multimodal density curves
mean2 = 80
standard_deviation2 = 20
multimodal_curve = (1 / (standard_deviation * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * standard_deviation ** 2)) + (1 / (standard_deviation2 * np.sqrt(2 * np.pi))) * np.exp(-((x - mean2) ** 2) / (2 * standard_deviation2 ** 2))




plt.plot(x, unimodal_curve, label='Unimodal')
plt.legend()
plt.show()



plt.figure(figsize=(10, 6))
sns.kdeplot(multimodal_curve, label="multimodal_curve")

plt.title("Density Curves of Normal Distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()

# Create histograms for comparison
plt.figure(figsize=(10, 6))

sns.histplot(random_sample, kde=True, label="Sample 1 (Mean 100, Std Dev 20)")
plt.title("Histograms of Normal Distributions")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()
