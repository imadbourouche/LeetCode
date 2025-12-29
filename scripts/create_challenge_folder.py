import os


name_challenge = input('name of the challenge: ')
folder_name = name_challenge.strip().replace(" ", "_")
print(folder_name)

# Get parent directory of the current script
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Folder path one level above
folder_path = os.path.join(parent_dir, "..", folder_name)

# Create the folder
os.makedirs(folder_path, exist_ok=True)

# Create files inside the folder
open(os.path.join(folder_path, "solution.py"), "w").close()
open(os.path.join(folder_path, "README.md"), "w").close()
