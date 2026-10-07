import pandas as pd
import matplotlib.pyplot as plt

METRICS = "metrics.csv"

df = pd.read_csv(METRICS)
val = df.dropna(subset=["val0_epoch/forces_mae"]).copy()

best_idx = val["val0_epoch/forces_mae"].idxmin()
best = val.loc[best_idx]

print("Best epoch:", int(best["epoch"]))
print("Best force MAE:", best["val0_epoch/forces_mae"], "eV/A")
print("Force RMSE:", best["val0_epoch/forces_rmse"], "eV/A")
print("Energy MAE/atom:",
      best["val0_epoch/per_atom_energy_mae"] * 1000,
      "meV/atom")
print("Total energy MAE:",
      best["val0_epoch/total_energy_mae"],
      "eV")

plt.figure(figsize=(6, 5))
plt.plot(val["epoch"], val["val0_epoch/forces_mae"])
plt.xlabel("Epoch")
plt.ylabel("Validation Force MAE (eV/A)")
plt.tight_layout()
plt.savefig("validation_force_mae.png", dpi=300)
plt.show()

plt.figure(figsize=(6, 5))
plt.plot(val["epoch"], val["val0_epoch/per_atom_energy_mae"] * 1000)
plt.xlabel("Epoch")
plt.ylabel("Validation Energy MAE (meV/atom)")
plt.tight_layout()
plt.savefig("validation_energy_mae.png", dpi=300)
plt.show()
