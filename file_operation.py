from pathlib import Path

# Absolute path
# Relative path

p = Path("package/")
print(p.exists())

for file in p.glob("*.py"):
    print("file", file.name)

new_dir_path = Path("New_Dir")

new_dir_path.mkdir()

new_dir_path.rmdir()
