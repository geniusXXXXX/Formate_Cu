# Training configuration

This directory is reserved for the exact NequIP YAML configuration used for the sanity-check and formal training runs.

The formal training used:

- NequIP 0.19.1
- cutoff: 5.0 Å
- chemical species: C, H, O, Cu
- number of interaction layers: 3
- l_max: 2
- number of features: 32
- optimizer: Adam
- learning rate: 0.001
- force and per-atom-energy loss terms
- GPU training
- checkpointing monitored by validation force MAE
- early stopping with patience 15
- maximum epochs: 100

The exact YAML file should be committed from the original Colab run rather than reconstructed from memory.
