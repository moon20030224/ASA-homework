
k_values = np.arange(1, 4.1, 0.1)
theoretical_bounds = 1 / k_values**2


sample_size = 1000
means = [np.mean(np.random.exponential(scale=1, size=sample_size)) for _ in range(1000)]


empirical_probabilities = []
for k in k_values:
    count = len([m for m in means if abs(m - mean) >= k * standard_deviation])
    empirical_probabilities.append(count / len(means))


plt.figure(figsize=(10, 6))
plt.plot(k_values, theoretical_bounds, label='Theoretical Bounds (Chebyshev)', color='red', linestyle='--')
plt.plot(k_values, empirical_probabilities, label='Empirical Probabilities', marker='o', linestyle='-', color='blue')
plt.xlabel('k (Number of Standard Deviations)')
plt.ylabel('Probability')
plt.title('Concentration Inequality Verification: Theoretical vs. Empirical')
plt.legend()
plt.grid(True)
plt.show()
plt.show()





