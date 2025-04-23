# List of torque values (25 samples from 0° to 360° in 15° steps)
torques = [
    -0.023859173, -0.025152996, -0.005491972, 0.02921337, 0.074618972,
    0.122546316, 0.16852687, 0.199694269, 0.237488443, 0.26975223,
    0.290276636, 0.278661845, -0.023859173, 0.213184154, 0.228110242,
    0.201450898, 0.157078181, 0.10221415, 0.044205134, -0.00936593,
    -0.050833341, -0.067811266, -0.044679159, -0.031766162, -0.023859173
]

# Step size for spacing (e.g., 8 steps = 120° since 360°/25 = 15° per step)
step_size = 8
n = len(torques)

best_sum = float('-inf')
best_indices = ()

# Only loop over valid starting points to avoid duplicate angles (avoid wrapping)
for i in range(n):
    i2 = (i + step_size) % n
    i3 = (i + 2 * step_size) % n

    # Avoid circular repeats (e.g., 0, 8, 16 and 24, 7, 15 are the same angles)
    if i < i2 < i3:  # ensure unique order
        total = torques[i] + torques[i2] + torques[i3]
        if total > best_sum:
            best_sum = total
            best_indices = (i, i2, i3)

# Convert to angles
angles = [15 * idx for idx in best_indices]

# Output
print("✅ Best torque combination:")
print(f"Indices: {best_indices}")
print(f"Angles (degrees): {angles}")
print(f"Torques: {[torques[i] for i in best_indices]}")
print(f"Total torque: {best_sum:.6f} N·m")
