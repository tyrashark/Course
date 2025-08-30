# --- Code Cell 1 ---
# Count number of sequences with no 4 consecutive heads
def count_valid_sequences(n):
    a = [0] * (n + 1)
    a[0] = 1  # empty sequence
    if n >= 1: a[1] = 2
    if n >= 2: a[2] = 4
    if n >= 3: a[3] = 8
    if n >= 4: a[4] = 15  # all except 'HHHH'
    for i in range(5, n+1):
      a[i] = a[i-1] + a[i-2] + a[i-3] + a[i-4]
    return a[n]

# Total possible sequences
n = 10
total = 2 ** n
valid = count_valid_sequences(n)
at_least_4_heads = total - valid
probability = at_least_4_heads / total

print(f"Number of sequences with at least 4 consecutive heads: {at_least_4_heads}")
print(f"Probability: {probability:.5f}")

# --- Code Cell 2 ---
import numpy as np

# Set seed
np.random.seed(0)

# Simulate 1000 throws of two 6-sided dice
die1 = np.random.randint(1, 7, 1000)
die2 = np.random.randint(1, 7, 1000)
sums = die1 + die2

# Calculate empirical probability
empirical_prob = np.mean(sums == 2)
print(f"Empirical probability of sum = 2: {empirical_prob:.5f}")

# --- Code Cell 3 ---
# Repeat simulation 10 times with the same seed
results = []

for i in range(10):
  np.random.seed(i)
  die1 = np.random.randint(1, 7, 1000)
  die2 = np.random.randint(1, 7, 1000)
  sums = die1 + die2
  prob = np.mean(sums == 2)
  results.append(prob)

# Print results
for i, prob in enumerate(results, 1):
    print(f"Run {i}: Empirical probability of sum = 2: {prob:.5f}")

# --- Code Cell 4 ---
import matplotlib.pyplot as plt

# Parameters
mu = 70
sigma = 2

# Generate an array x
delta_x = 2 # increment of the array x
x = np.arange(68, 80+delta_x, delta_x)

# Gaussian PDF
def gaussian_pdf(x, mu, sigma):
  coef = 1 / (np.sqrt(2 * np.pi)*sigma)
  exponent = -((x-mu)**2) / (2 * sigma**2)
  return coef * np.exp(exponent)

# Evaluate the PDF at each x
p = gaussian_pdf(x, mu, sigma)

# Plot as a bar chart
plt.figure(figsize=(8, 5))

plt.bar(x, p, width=1.5, color="skyblue", edgecolor="black")
plt.title("Discrete Approximation of Gaussian PDF (μ=70, σ=2)")
plt.xlabel("x")
plt.ylabel("PDF Value")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# --- Code Cell 5 ---
# Find an integral using a Riemann sum.

integral_approx = np.sum(gaussian_pdf(x, mu, sigma)*delta_x)

print(f"Intergral approximation with the delta x = 2 : {integral_approx:.5f}")

# --- Code Cell 6 ---
# Generate a finer grid for x with smaller spacing
delta_x_fine = 0.01
x_fine = np.arange(68, 80 + delta_x_fine, delta_x_fine)

# Approximate the integral of the Gaussian PDF over [68, 80]
integral_approx = np.sum(gaussian_pdf(x_fine, mu, sigma) * delta_x_fine)

print(f"Integral approximation over [68, 80] with Δx = {delta_x_fine}: {integral_approx:.5f}")


# --- Code Cell 7 ---
x_wide = np.arange(20, 120 + delta_x_fine, delta_x_fine)

# PDF
p_wide = gaussian_pdf(x_wide, mu, sigma)

# Approximate the integral of the Gaussian PDF over [68, 80]
integral_approx = np.sum(p_wide * delta_x_fine)

# Print the approximation result
print(f"Approximate probability P(20 ≤ X < 120): {integral_approx:.10f}")

# --- Code Cell 8 ---
from google.colab import drive
drive.mount('/content/drive')

# --- Code Cell 9 ---
# Replace 'CSC535_hw1.ipynb' with the actual path to your file in Google Drive
file_path = '/content/drive/My Drive/Colab Notebooks/CSC535_hw1.ipynb'


try:
    with open(file_path, 'r') as f:
        # You can now work with your file
        print(f"Successfully opened: {file_path}")
        # Example: read the first few lines
        for i, line in enumerate(f):
            if i < 5:
                print(line.strip())
            else:
                break
except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# --- Code Cell 10 ---


# --- Code Cell 11 ---
import json

# Load the notebook content
# Make sure to replace 'your_notebook.ipynb' with the correct path to your notebook file
notebook_path = '/content/drive/My Drive/Colab Notebooks/CSC535_hw1.ipynb'
output_file_path = '/content/drive/My Drive/Colab Notebooks/extracted_code.py' # Define the output file path

try:
    with open(notebook_path, 'r') as f:
        notebook_content = json.load(f)

    # Extract only code cells
    code_cells = [cell for cell in notebook_content['cells'] if cell['cell_type'] == 'code']

    # Write the extracted code to a .py file
    with open(output_file_path, 'w') as f:
        for i, code_cell in enumerate(code_cells):
            f.write(f"# --- Code Cell {i+1} ---\n")
            f.write("".join(code_cell['source']))
            f.write("\n\n")

    print(f"Successfully extracted code to: {output_file_path}")

except FileNotFoundError:
    print(f"Error: The notebook file was not found at {notebook_path}")
except Exception as e:
    print(f"An error occurred: {e}")

