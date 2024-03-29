"""Script to make all the section folders and blank tex files."""

import os

number_of_sections = 2

# Define the base folder name
base_folder_name = "section"
DIRECTORY_PATH = os.path.dirname(__file__)
PARENT_DIRECTORY = os.path.basename(DIRECTORY_PATH)

# Create 12 folders
for i in range(number_of_sections):
    # Use f-strings to format the folder name with leading zeros
    folder_name = f"{base_folder_name}{(i+1):02}"
    os.makedirs(folder_name)

    # Create a blank .tex file in each folder
    with open(os.path.join(folder_name, f"{PARENT_DIRECTORY}{folder_name}.tex"), "w") as tex_file:
        pass

print("Folders and blank .tex files created successfully!")
