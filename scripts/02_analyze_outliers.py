import numpy as np
import matplotlib.pyplot as plt
from ase.io import read, write

DATASET = "fcu.xyz"

frames = read(DATASET, index=":")

max_force = -1.0
max_frame = None
max_atom = None
max_vector = None

all_force_norms = []

for i, atoms in enumerate(frames):
    forces = atoms.get_forces()
    norms = np.linalg.norm(forces, axis=1)
    all_force_norms.extend(norms)

    j = int(np.argmax(norms))
    if norms[j] > max_force:
        max_force = float(norms[j])
        max_frame = i
        max_atom = j
        max_vector = forces[j].copy()

all_force_norms = np.asarray(all_force_norms)

print("Maximum-force frame:", max_frame)
print("Atom index:", max_atom)
print("Element:", frames[max_frame][max_atom].symbol)
print("|F|:", max_force, "eV/A")
print("Force vector:", max_vector)

for p in [50, 90, 95, 99, 99.9]:
    print(f"{p}th percentile:", np.percentile(all_force_norms, p))

for threshold in [5, 10, 20]:
    print(f"Number of atoms with |F| > {threshold} eV/A:",
          np.sum(all_force_norms > threshold))

write("max_force_structure.xyz", frames[max_frame])

plt.figure(figsize=(6, 5))
plt.hist(all_force_norms, bins=150)
plt.xlabel("Force norm (eV/A)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("force_norm_histogram.png", dpi=300)
plt.show()
