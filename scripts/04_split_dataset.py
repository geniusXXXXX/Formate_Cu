import random
from ase.io import read, write

DATASET = "fcu.xyz"
SEED = 42
N_TRAIN = 2500
N_VALID = 250

frames = read(DATASET, index=":")
indices = list(range(len(frames)))

rng = random.Random(SEED)
rng.shuffle(indices)

train_idx = indices[:N_TRAIN]
valid_idx = indices[N_TRAIN:N_TRAIN + N_VALID]
test_idx = indices[N_TRAIN + N_VALID:]

write("train.xyz", [frames[i] for i in train_idx])
write("validation.xyz", [frames[i] for i in valid_idx])
write("test.xyz", [frames[i] for i in test_idx])

for filename, values in [
    ("train_indices.txt", train_idx),
    ("validation_indices.txt", valid_idx),
    ("test_indices.txt", test_idx),
]:
    with open(filename, "w", encoding="utf-8") as f:
        for i in values:
            f.write(f"{i}\n")

print("train:", len(train_idx))
print("validation:", len(valid_idx))
print("test:", len(test_idx))
