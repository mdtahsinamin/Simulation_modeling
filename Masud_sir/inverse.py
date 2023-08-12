import numpy as np
import matplotlib.pyplot as plt

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
