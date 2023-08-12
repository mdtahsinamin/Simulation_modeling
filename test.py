import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Parameters for the normal distributions
sample_size = 200
mean_unimodal = 100
std_dev_unimodal = 20
mean_multimodal1 = 80
mean_multimodal2 = 120
std_dev_multimodal = 20

# Generate random samples from normal distributions
sample_unimodal = np.random.normal(mean_unimodal, std_dev_unimodal, sample_size)
sample_multimodal = np.concatenate([
    np.random.normal(mean_multimodal1, std_dev_multimodal, sample_size // 2),
    np.random.normal(100, std_dev_multimodal, sample_size // 2)
])

# Create density plots (unimodal and multimodal)
plt.figure(figsize=(10, 6))

sns.kdeplot(sample_unimodal, label="Unimodal (Mean 100, Std Dev 20)")
sns.kdeplot(sample_multimodal, label="Multimodal (Means 80 and 120, Std Dev 20)")

plt.title("Density Curves of Normal Distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()

# Generate random samples for diastolic blood pressure distribution
diastolic_blood_pressure = np.random.normal(80, 20, sample_size)

# Create histogram of diastolic blood pressure distribution
plt.figure(figsize=(10, 6))

sns.histplot(diastolic_blood_pressure, bins=20, kde=True, label="Diastolic Blood Pressure")

plt.title("Histogram of Diastolic Blood Pressure Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()
