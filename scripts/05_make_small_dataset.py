from ase.io import read, write

train = read("train.xyz", index=":")
validation = read("validation.xyz", index=":")

write("train_500.xyz", train[:500])
write("val_100.xyz", validation[:100])

print("train_500:", 500)
print("val_100:", 100)
