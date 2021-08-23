from pathlib import Path

# Absolute Path : Starts from root of the hard disk
# Relative Path : Path Module works with this relative path i.e. with respect to current directory

path = Path("test")
# check if path mentioned exist or no
print(path.exists())
if not path.exists():
    path.mkdir()
else:
    path.rmdir()

print(path.exists())

path_main = Path("..")
all_python_file = path_main.glob("*.py")

for file in all_python_file:
    print(file.name)
