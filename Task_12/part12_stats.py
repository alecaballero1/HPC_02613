import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

plt.figure(figsize=(8, 5))
plt.hist(df['mean_temp'], bins=30, color='orange', edgecolor='black')
plt.title("Distribution of Mean Temperatures")
plt.xlabel("Mean Temperature (°C)")
plt.ylabel("Number of Buildings")
plt.grid(True)
plt.tight_layout()
plt.savefig("histogram_mean_temp.png")
plt.close()

avg_mean = df['mean_temp'].mean()
print(f"avg_mean: {avg_mean:.2f} °C")

avg_std = df['std_temp'].mean()
print(f"avg_std: {avg_std:.2f} °C")

above_18_count = (df['pct_above_18'] >= 50).sum()
print(f"above_18_count: {above_18_count} / {len(df)}")

below_15_count = (df['pct_below_15'] >= 50).sum()
print(f"below_15_count: {below_15_count} / {len(df)}")
