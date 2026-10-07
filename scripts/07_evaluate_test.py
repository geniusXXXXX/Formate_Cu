import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from nequip.integrations.ase import NequIPCalculator

TEST_SET = "test.xyz"
COMPILED_MODEL = "best_model.nequip.pt2"

test_data = read(TEST_SET, index=":")
print("Number of test structures:", len(test_data))

calc = NequIPCalculator.from_compiled_model(
    compile_path=COMPILED_MODEL,
    device="cuda",
    chemical_species_to_atom_type_map=True,
)

dft_energies, ml_energies = [], []
dft_forces, ml_forces = [], []

for i, atoms in enumerate(test_data):
    dft_energy = atoms.get_potential_energy()
    dft_force = atoms.get_forces().copy()

    atoms.calc = calc
    ml_energy = atoms.get_potential_energy()
    ml_force = atoms.get_forces()

    dft_energies.append(dft_energy)
    ml_energies.append(ml_energy)
    dft_forces.append(dft_force)
    ml_forces.append(ml_force)

    if (i + 1) % 200 == 0:
        print(f"Finished {i + 1}/{len(test_data)}")

dft_energies = np.asarray(dft_energies)
ml_energies = np.asarray(ml_energies)
dft_forces = np.concatenate(dft_forces, axis=0)
ml_forces = np.concatenate(ml_forces, axis=0)

energy_error = ml_energies - dft_energies
energy_mae = np.mean(np.abs(energy_error))
energy_rmse = np.sqrt(np.mean(energy_error ** 2))

n_atoms = len(test_data[0])

force_error = ml_forces - dft_forces
force_mae = np.mean(np.abs(force_error))
force_rmse = np.sqrt(np.mean(force_error ** 2))

print("\nFINAL TEST RESULTS")
print("Energy MAE:", energy_mae, "eV")
print("Energy RMSE:", energy_rmse, "eV")
print("Energy MAE / atom:", energy_mae / n_atoms * 1000, "meV/atom")
print("Energy RMSE / atom:", energy_rmse / n_atoms * 1000, "meV/atom")
print("Force MAE:", force_mae, "eV/A")
print("Force RMSE:", force_rmse, "eV/A")

plt.figure(figsize=(6, 6))
plt.scatter(dft_energies, ml_energies, s=10, alpha=0.5)
lo = min(dft_energies.min(), ml_energies.min())
hi = max(dft_energies.max(), ml_energies.max())
plt.plot([lo, hi], [lo, hi], "--")
plt.xlabel("DFT Energy (eV)")
plt.ylabel("NequIP Energy (eV)")
plt.tight_layout()
plt.savefig("test_energy_parity.png", dpi=300)
plt.show()

x = dft_forces.ravel()
y = ml_forces.ravel()
plt.figure(figsize=(6, 6))
plt.scatter(x, y, s=2, alpha=0.2)
lo = min(x.min(), y.min())
hi = max(x.max(), y.max())
plt.plot([lo, hi], [lo, hi], "--")
plt.xlabel("DFT Force (eV/A)")
plt.ylabel("NequIP Force (eV/A)")
plt.tight_layout()
plt.savefig("test_force_parity.png", dpi=300)
plt.show()
