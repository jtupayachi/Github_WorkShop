"""
stats.py — Statistical analysis module.

This file is added during the BRANCHING demo to show
how feature branches and pull requests work.
"""

import numpy as np


def t_test(sample1, sample2):
    """Perform a simple two-sample t-test."""
    n1, n2 = len(sample1), len(sample2)
    mean1, mean2 = np.mean(sample1), np.mean(sample2)
    var1, var2 = np.var(sample1, ddof=1), np.var(sample2, ddof=1)

    pooled_se = np.sqrt(var1 / n1 + var2 / n2)
    t_stat = (mean1 - mean2) / pooled_se
    df = n1 + n2 - 2

    return {"t_statistic": t_stat, "degrees_of_freedom": df}


def correlation(x, y):
    """Compute Pearson correlation coefficient."""
    return np.corrcoef(x, y)[0, 1]


def linear_regression(x, y):
    """Fit a simple linear regression: y = mx + b."""
    coeffs = np.polyfit(x, y, 1)
    return {"slope": coeffs[0], "intercept": coeffs[1]}


def summary_report(x, y):
    """Generate a complete statistical summary."""
    reg = linear_regression(x, y)
    r = correlation(x, y)

    report = f"""
    ===== Statistical Summary =====
    N samples:      {len(x)}
    X range:        [{np.min(x):.2f}, {np.max(x):.2f}]
    Y range:        [{np.min(y):.2f}, {np.max(y):.2f}]
    Correlation:    {r:.4f}
    Regression:     y = {reg['slope']:.4f}x + {reg['intercept']:.4f}
    R-squared:      {r**2:.4f}
    ================================
    """
    return report


if __name__ == "__main__":
    # Quick test
    np.random.seed(42)
    x = np.linspace(0, 10, 50)
    y = 3 * x + np.random.normal(0, 2, 50)

    print(summary_report(x, y))
