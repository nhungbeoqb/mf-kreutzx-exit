import os

TEXT = "I am resigning from the aquarium, effective immediately: the penguins have unionised, and frankly, their demands are reasonable."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
