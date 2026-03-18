"""
analysis.py — Simple data analysis script for Git demo.

This file is used during the live coding demonstration
to show Git add, commit, diff, and push workflows.
"""

import numpy as np


def generate_data(n_samples=100, seed=42):
    """Generate sample data for analysis."""
    np.random.seed(seed)
    x = np.linspace(0, 10, n_samples)
    y = 2.5 * x + np.random.normal(0, 2, n_samples)
    return x, y


def compute_statistics(data):
    """Compute basic statistics for a dataset."""
    return {
        "mean": np.mean(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data),
        "median": np.median(data),
    }


def plot_data(x, y, title="Data Visualization"):
    """Plot the data with a trend line.

    NOTE: This function is added in the SECOND commit
    during the live demo to show 'git diff'.
    """
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y, alpha=0.6, label="Data points")

    # Fit and plot trend line
    coeffs = np.polyfit(x, y, 1)
    trend = np.polyval(coeffs, x)
    ax.plot(x, trend, "r--", linewidth=2, label=f"Trend: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(title)
    ax.legend()
    plt.tight_layout()
    plt.savefig("output.png", dpi=150)
    print("Plot saved to output.png")
    plt.show()


if __name__ == "__main__":
    print("Generating data...")
    x, y = generate_data()

    print("\nStatistics for Y:")
    stats = compute_statistics(y)
    for key, value in stats.items():
        print(f"  {key}: {value:.4f}")

    print("\nCreating visualization...")
    plot_data(x, y, title="Sample Data Analysis")
    print("Done!")
