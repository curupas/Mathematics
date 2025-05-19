import numpy as np
import matplotlib.pyplot as plt

def sequence(x0, iterations=10):
    """Generate the sequence x_n = (x_{n-1}/2) + (1/x_{n-1})"""
    x = [x0]
    for _ in range(iterations):
        x.append(x[-1]/2 + 1/x[-1])
    return x

# Parameters
iterations = 10
sqrt2 = np.sqrt(2)

# Three cases to plot
cases = [
    {"x0": 3.0, "label": f"$x_0 = 3.0 > sqrt{2}$", "color": "blue"},
    {"x0": 1.0, "label": f"$x_0 = 1.0 < sqrt{2}$", "color": "green"},
    {"x0": sqrt2, "label": f"$x_0 = sqrt{2}$", "color": "red"}
]

# Create figure with 3 subplots
plt.figure(figsize=(15, 5))

for i, case in enumerate(cases, 1):
    plt.subplot(1, 3, i)
    seq = sequence(case["x0"], iterations)
    
    # Plot sequence
    plt.plot(seq, 'o-', color=case["color"], label=case["label"])
    
    # Plot √2 reference line
    plt.axhline(y=sqrt2, color='black', linestyle='--', label='$\sqrt{2}$')
    
    plt.title(case["label"])
    plt.xlabel('Iteration (n)')
    plt.ylabel('$x_n$ value')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()