from pathlib import Path

# Absolute path
# Relative path
# path = Path("ecommerce")
# print(path.exists()) # False there is no directory

# path = Path("emails")
# print(path.mkdir()) # Created a directory

# path = Path("emails")
# print(path.rmdir()) # Removed a directory

### finding the .py files in the directory


import os

# # Print the current working directory
# print(f"Current working directory: {os.getcwd()}")

# # Get the directory containing the script 
script_dir = Path(__file__).parent
print(f"Script directory: {script_dir}")

# # SErarch for .py files in the script directory
for file in script_dir.glob('*.py'):
    print(file)
    