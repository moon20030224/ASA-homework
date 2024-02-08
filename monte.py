
N_values = np.logspace(1, 4, 20).astype(int)
sample_averages = [np.mean(np.random.exponential(scale=1, size=N)) for N in N_values]

plt.figure(figsize=(10, 6))
plt.plot(N_values, sample_averages, marker='o', linestyle='-', color='blue', label='Sample Averages')
plt.axhline(y=1, color='r', linestyle='--', label='Theoretical Mean = 1')
plt.xscale('log')
plt.xlabel('Number of Observations (N)')
plt.ylabel('Sample Average')
plt.title('Weak Law of Large Numbers (WLLN) Verification')
plt.legend()
plt.grid(True)
plt.show()


sample_sizes = [30, 100, 1000]
sample_means = []

plt.figure(figsize=(10, 6))
for size in sample_sizes:
    means = [np.mean(np.random.exponential(scale=1, size=size)) for _ in range(1000)]
    sample_means.append(means)
    plt.hist(means, bins=30, alpha=0.5, label=f'N={size}')

plt.title('Central Limit Theorem (CLT) Verification')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.legend()
plt.show()





