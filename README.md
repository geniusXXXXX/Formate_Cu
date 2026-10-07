# Machine-Learning Interatomic Potential for Formate Decomposition on Cu

## Overview

This repository documents an independent reproduction-and-extension project using an E(3)-equivariant graph neural network interatomic potential (NequIP) for a formate/Cu catalytic surface.

The goal is to establish an end-to-end **DFT-to-MLIP workflow for heterogeneous catalysis**: data inspection, quality control, train/validation/test splitting, GPU training, checkpoint selection, model packaging and compilation, ASE-based inference, and independent test-set evaluation. The next stage will apply the trained potential to the **formate decomposition reaction pathway on Cu**.

> **Data provenance:** the underlying DFT dataset is a published public dataset associated with the NequIP work by Batzner *et al.* The raw DFT configurations were not generated in this project and are therefore not redistributed here.

## Current model performance

| Metric | Independent test set |
|---|---:|
| Energy MAE | **0.506 meV/atom** |
| Energy RMSE | **0.810 meV/atom** |
| Force MAE | **0.048 eV/Å** |
| Force RMSE | **0.062 eV/Å** |

The independent test set contains 4,105 configurations that were not used for model optimization.

## Workflow

```text
Published DFT dataset
        ↓
Dataset inspection
        ↓
Force/energy quality analysis
        ↓
Train / validation / test split
        ↓
Small sanity-check training
        ↓
Formal NequIP GPU training
        ↓
Best-checkpoint selection
        ↓
Model packaging
        ↓
Model compilation
        ↓
ASE inference
        ↓
Independent test-set evaluation
        ↓
Reaction-pathway application
```

## Repository structure

```text
Formate_Cu/
├── README.md
├── requirements.txt
├── .gitignore
├── scripts/
│   ├── 01_inspect_dataset.py
│   ├── 02_analyze_outliers.py
│   ├── 03_inspect_high_force_frame.py
│   ├── 04_split_dataset.py
│   ├── 05_make_small_dataset.py
│   ├── 06_plot_training_metrics.py
│   └── 07_evaluate_test.py
├── configs/
│   └── README.md
├── results/
│   └── metrics_summary.md
├── models/
│   └── README.md
└── reaction_pathway/
    └── README.md
```

## Key dataset checks completed

- 6,855 configurations
- 52 atoms per configuration
- composition: Cu48 O2 C1 H1
- periodic boundary conditions enabled
- reference total energies and atomic forces available through ASE
- high-force configurations inspected explicitly rather than removed automatically

## Model-training workflow

The training workflow used NequIP 0.19.1 with PyTorch on an NVIDIA Tesla T4 GPU in Google Colab. A small sanity-check model was trained first to verify the full pipeline before launching the formal run.

The formal model used an E(3)-equivariant NequIP architecture with a 5 Å cutoff and atomic species C, H, O, and Cu. Training was monitored using validation force MAE, and the best checkpoint was packaged and compiled for ASE inference.

## Validation result

At the best epoch:

- validation force MAE: 0.0484 eV/Å
- validation force RMSE: 0.0582 eV/Å
- validation energy MAE: 0.444 meV/atom
- validation total-energy MAE: 0.0231 eV/structure

Validation and test errors are very similar, indicating that the trained model generalizes consistently to the held-out test set.

## Reproducibility notes

The exact raw DFT dataset should be obtained from the original public source. Large raw XYZ files, Colab cache directories, Lightning logs, and compiled CUDA-specific artifacts are intentionally excluded from this repository.

The scripts in this repository document the data inspection, splitting, metric analysis, and final model evaluation workflow.

## Tools

- Python
- PyTorch
- NequIP
- e3nn
- ASE
- NumPy
- pandas
- Matplotlib
- Google Colab / CUDA GPU

## Next stage: catalytic reaction pathway

The next stage of this project will test whether the trained MLIP can reproduce DFT energetics along the formate decomposition pathway on Cu. This section will be expanded with pathway extraction, reaction-coordinate analysis, DFT-vs-MLIP energy profiles, and interpretation of the catalytic mechanism.

## Reference

Batzner *et al.*, “E(3)-equivariant graph neural networks for data-efficient and accurate interatomic potentials,” *Nature Communications* (2022).
