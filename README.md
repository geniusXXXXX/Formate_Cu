# Machine-Learning Interatomic Potential for Formate Decomposition on Cu

This project reproduces and extends an E(3)-equivariant graph neural network interatomic potential workflow using NequIP for a formate/Cu catalytic surface.

The project covers the complete workflow from DFT-derived atomistic data preprocessing and quality analysis to GPU training, model validation, packaging, compilation, and ASE-based inference.

The trained NequIP model achieved:

- Test energy MAE: 0.506 meV/atom
- Test energy RMSE: 0.810 meV/atom
- Test force MAE: 0.048 eV/Å
- Test force RMSE: 0.062 eV/Å

The next stage applies the trained MLIP to reproduce the formate decomposition reaction pathway on Cu.
