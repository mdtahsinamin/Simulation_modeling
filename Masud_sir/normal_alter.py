import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Generate a random sample from a normal distribution

sample_size = 200
mean = 100
standard_deviation = 20
mean2 = 80
standard_deviation2 = 20

random_sample = np.random.normal(mean2, standard_deviation2, sample_size)


# Plot the unimodal density curves

# numpy.linspace(start, stop, num)
x = np.linspace(min(random_sample), max(random_sample), 200) # create an array of evenly spaced numbers within a specified interval.
unimodal_curve = (1 / (standard_deviation * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * standard_deviation ** 2))


# Plot the multimodal density curves
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
sns.histplot(random_sample, kde=True, label="Diastolic Blood Pressure")
plt.title("Histograms of Normal Distributions")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()
