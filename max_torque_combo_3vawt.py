# List of torque values (25 samples from 0° to 360° in 15° steps)
torques = [
    -0.023859173, -0.025152996, -0.005491972, 0.02921337, 0.074618972,
    0.122546316, 0.16852687, 0.199694269, 0.237488443, 0.26975223,
    0.290276636, 0.278661845, -0.023859173, 0.213184154, 0.228110242,
    0.201450898, 0.157078181, 0.10221415, 0.044205134, -0.00936593,
    -0.050833341, -0.067811266, -0.044679159, -0.031766162, -0.023859173
]

# Step size for spacing between samples (e.g. 8 for 120° with 15° steps)
step_size = 8

# Initialize tracking variables
best_sum = float('-inf')
best_indices = ()

# Loop through each index as the starting point
for i in range(len(torques)):
    idx2 = (i + step_size) % len(torques)
    idx3 = (i + 2 * step_size) % len(torques)

    t1 = torques[i]
    t2 = torques[idx2]
    t3 = torques[idx3]
    total = t1 + t2 + t3

    if total > best_sum:
        best_sum = total
        best_indices = (i, idx2, idx3)

# Convert indices to angles
angles = [15 * idx for idx in best_indices]

# Display the results
print("Best torque combination:")
print(f"Indices: {best_indices}")
print(f"Angles (degrees): {angles}")
print(f"Torques: {[torques[i] for i in best_indices]}")
print(f"Total torque: {best_sum:.6f} N·m")
