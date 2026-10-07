from collections import Counter
import numpy as np
from ase.io import read

DATASET = "fcu.xyz"

frames = read(DATASET, index=":")
print("Number of structures:", len(frames))

atoms0 = frames[0]
print("Atoms in first structure:", len(atoms0))
print("Composition:", Counter(atoms0.get_chemical_symbols()))
print("PBC:", atoms0.pbc)
print("Cell lengths (A):", atoms0.cell.lengths())

energies = []
force_norms = []

for atoms in frames:
    energies.append(atoms.get_potential_energy())
    forces = atoms.get_forces()
    force_norms.extend(np.linalg.norm(forces, axis=1))

energies = np.asarray(energies)
force_norms = np.asarray(force_norms)

print("\nEnergy statistics (eV)")
print("min:", energies.min())
print("max:", energies.max())
print("mean:", energies.mean())

print("\nForce norm statistics (eV/A)")
print("min:", force_norms.min())
print("max:", force_norms.max())
print("mean:", force_norms.mean())
