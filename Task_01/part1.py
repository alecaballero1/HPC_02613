import os
import numpy as np
import matplotlib.pyplot as plt
from os.path import join


LOAD_DIR = '/dtu/projects/02613_2025/data/modified_swiss_dwellings/'
OUT_DIR = 'floorplan_visualizations'
os.makedirs(OUT_DIR, exist_ok=True)

with open(join(LOAD_DIR, 'building_ids.txt'), 'r') as f:
    building_ids = f.read().splitlines()
print(len(building_ids))

# Number of buildings to visualize
N = 4

fig, axs = plt.subplots(2, N, figsize=(3 * N, 6))

for i, bid in enumerate(building_ids[:N]):
    domain_path = join(LOAD_DIR, f"{bid}_domain.npy")
    interior_path = join(LOAD_DIR, f"{bid}_interior.npy")

    if not os.path.exists(domain_path) or not os.path.exists(interior_path):
        print(f"Skipping {bid}, missing files.")
        continue

    domain = np.load(domain_path)
    interior = np.load(interior_path)

    axs[0, i].imshow(domain, cmap='hot')
    axs[0, i].set_title(f"{bid}_domain")
    axs[0, i].axis('off')

    axs[1, i].imshow(interior, cmap='gray')
    axs[1, i].set_title(f"{bid}_interior")
    axs[1, i].axis('off')

plt.tight_layout()
out_path = os.path.join(OUT_DIR, "combined_visualization.png")
plt.savefig(out_path)
plt.close()
print(f"Saved combined visualization to {out_path}")
