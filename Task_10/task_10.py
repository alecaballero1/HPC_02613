import sys
import time
from os.path import join
import numpy as np
import cupy as cp

def load_data(load_dir, bid):
    SIZE = 512
    u_cpu = np.zeros((SIZE + 2, SIZE + 2), dtype=np.float32)
    u_cpu[1:-1, 1:-1] = np.load(join(load_dir, f"{bid}_domain.npy"))
    interior_mask_cpu = np.load(join(load_dir, f"{bid}_interior.npy"))
    #Convert to CuPy
    u = cp.asarray(u_cpu)
    interior_mask = cp.asarray(interior_mask_cpu)
    return u, interior_mask

#Instead of original loop
def jacobi_noloop(u, interior_mask, max_iter=20000, atol=1e-6):
    u = u.copy()
    mask_full = cp.zeros_like(u, dtype=bool)
    mask_full[1:-1, 1:-1] = interior_mask

    for i in range(max_iter):
        u_new = cp.zeros_like(u)
        u_new[1:-1, 1:-1] = 0.25 * (
            u[1:-1, :-2] +  #left
            u[1:-1, 2:] +   #right
            u[:-2, 1:-1] +  #up
            u[2:, 1:-1]     #down
        )

        delta = cp.abs(u_new - u)[mask_full].max()
        u[mask_full] = u_new[mask_full]
        if delta < atol:
            break
    return u

def summary_stats(u, interior_mask):
    u_interior = u[1:-1, 1:-1][interior_mask]
    mean_temp = cp.mean(u_interior).item()
    std_temp = cp.std(u_interior).item()
    pct_above_18 = cp.sum(u_interior > 18).item() / u_interior.size * 100
    pct_below_15 = cp.sum(u_interior < 15).item() / u_interior.size * 100
    return {
        'mean_temp': mean_temp,
        'std_temp': std_temp,
        'pct_above_18': pct_above_18,
        'pct_below_15': pct_below_15,
    }

if __name__ == '__main__':
    start = time.time()
    # Load data
    LOAD_DIR = '/dtu/projects/02613_2025/data/modified_swiss_dwellings/'
    with open(join(LOAD_DIR, 'building_ids.txt'), 'r') as f:
        building_ids = f.read().splitlines()

    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    building_ids = building_ids[:N]

    stat_keys = ['mean_temp', 'std_temp', 'pct_above_18', 'pct_below_15']
    print('building_id, ' + ', '.join(stat_keys))

    MAX_ITER = 20_000
    ABS_TOL = 1e-4

    #Use a loop for all buildings
    for bid in building_ids:
        u0, interior_mask = load_data(LOAD_DIR, bid)
        u = jacobi_noloop(u0, interior_mask, MAX_ITER, ABS_TOL)
        stats = summary_stats(u, interior_mask)
        print(f"{bid},", ", ".join(f"{stats[k]:.6f}" for k in stat_keys))

    print(f"\nTotal execution time: {time.time() - start:.2f} seconds")
