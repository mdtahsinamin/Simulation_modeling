import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv

# Parameters
# Exponential distribution rate parameter
num_samples = 10000  # Number of random variates to generate
mean = 2.5
# Generate random variates using inverse transform function
def inverse_transform_exponential(mean, num_samples):
    u = np.random.uniform(0, 1, num_samples)  # Generate uniform random numbers between 0 and 1
    x = -mean * np.log(1 - u)   # Apply the inverse transform
    return x

# Generate random variates

def generate_normal_inverse_transform(n, mean, std_dev):
    u = np.random.uniform(0, 1, n)
    x = mean + std_dev * np.sqrt(2) * erfinv(2 * u - 1)
    return x

# Parameters for the normal distribution
n_samples = 1000  # Number of random variates to generate
mean = 2.5       # Mean of the normal distribution
std_dev = 20     # Standard deviation of the normal distribution

# Generate random variates using the inverse transform method
random_variates = generate_normal_inverse_transform(n_samples, mean, std_dev)
generated_variates = inverse_transform_exponential(mean, num_samples)

# Plot the histogram of generated random variates
plt.hist(generated_variates, bins=50, density=True, alpha=0.7, color='blue', label='Generated Data')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram of Generated Random Variates from Exponential Distribution')
plt.legend()

# Calculate theoretical PDF for comparison
theoretical_x = np.linspace(0, max(generated_variates), 1000)
theoretical_pdf = pdf = (1 / mean) * np.exp(-theoretical_x / mean)
plt.plot(theoretical_x, theoretical_pdf, color='red', label='Theoretical PDF')
plt.legend()

plt.grid(True)
plt.show()

# Display some generated random variates
print("Generated Random Variates:")
print(generated_variates[:10])

# Plot a histogram of the generated random variates
plt.hist(random_variates, bins=30, density=True, alpha=0.6, color='b')

# Plot the true normal probability density function
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 100)
pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev)**2)
plt.plot(x, pdf, 'r', label='True PDF')

plt.title('Generated Random Variates from Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
