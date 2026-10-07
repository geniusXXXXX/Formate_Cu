# Model artifacts

The final model was trained with NequIP 0.19.1 and PyTorch 2.11.0 on an NVIDIA Tesla T4 GPU.

During the project, the best checkpoint was packaged as a NequIP model package and compiled for ASE inference.

Large or environment-specific model artifacts are not committed by default:

- `*.ckpt` — Lightning/NequIP training checkpoints
- `*.nequip.zip` — packaged NequIP models
- `*.pt2` — compiled PyTorch model; may depend on the PyTorch/CUDA runtime

For long-term reproducibility, the packaged model is generally more portable than the compiled CUDA-specific artifact.
