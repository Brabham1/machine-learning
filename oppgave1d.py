import math

# Parameters
mass    = 5        # kg
g       = 9.81     # m/s²
delta_p = 60_000   # Pa (60 kPa)
S       = 1.2      # safety margin
F_req   = mass * g # N required

print(f"Required lifting force: {F_req:.2f} N\n")
print(f"{'z':>4} | {'d (mm)':>8} | {'Dead vol. (rel, mm²)':>22}")
print("-" * 42)

results = []

for z in range(1, 21):
    # Minimum area to lift the load
    A_min = F_req * S / (delta_p * z)

    # Minimum diameter, rounded UP to nearest mm
    d_min_mm = math.ceil(math.sqrt(4 * A_min / math.pi) * 1000)

    # Total dead volume ∝ z × π × (d/2)² (height cancels out)
    r_m = (d_min_mm / 1000) / 2
    dead_vol = z * math.pi * r_m ** 2 * 1e6  # in mm² (per unit height)

    results.append((z, d_min_mm, dead_vol))
    print(f"{z:>4} | {d_min_mm:>8} | {dead_vol:>22.4f}")

# Best combination
best = min(results, key=lambda x: x[2])
print(f"\nOptimal choice: {best[0]} suction cup(s) with diameter {best[1]} mm")
print(f"  Dead volume ~ {best[2]:.4f} mm^2 (per unit cup height)")
