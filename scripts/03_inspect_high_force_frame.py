import numpy as np
from ase.io import read

DATASET = "fcu.xyz"
FRAME_INDEX = 539
ATOM_INDEX = 1

atoms = read(DATASET, index=FRAME_INDEX)

print("Frame:", FRAME_INDEX)
print("Energy:", atoms.get_potential_energy(), "eV")
print("Target atom:", ATOM_INDEX, atoms[ATOM_INDEX].symbol)
print("Position:", atoms.positions[ATOM_INDEX])

distances = []
for j, atom in enumerate(atoms):
    if j == ATOM_INDEX:
        continue
    d = atoms.get_distance(ATOM_INDEX, j, mic=True)
    distances.append((d, j, atom.symbol))

for d, j, symbol in sorted(distances)[:10]:
    print(f"{symbol:>2s}  index={j:3d}  distance={d:.4f} A")
