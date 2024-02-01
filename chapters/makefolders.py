"""Script to make all the chapter folders, figures folders, and blank tex files."""

import os

# Define the base folder name
base_folder_name = "chapter"
secondary_folder_name = "figures"

# Create 12 folders
for i in range(1, 13):
    # Use f-strings to format the folder name with leading zeros
    folder_name = f"{base_folder_name}{i:02}"
    os.makedirs(folder_name)

    secondary_folder_name = f"{secondary_folder_name}{i:02}"
    os.makedirs(os.path.join(folder_name, secondary_folder_name))

    # Create a blank .tex file in each folder
    with open(os.path.join(folder_name, f"{folder_name}.tex"), "w") as tex_file:
        pass  # Pass does nothing, creating an empty file

print("Folders and blank .tex files created successfully!")
