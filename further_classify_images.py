import os
import shutil
from pathlib import Path

# Define the parent folders to process
parent_folders = [
    "C:\\Users\\paray\\OneDrive\\Desktop\\bits new research\\dataset\\dataset\\organized_screenshots\\Entertainment",
    "C:\\Users\\paray\\OneDrive\\Desktop\\bits new research\\dataset\\dataset\\organized_screenshots\\Gaming",
    "C:\\Users\\paray\\OneDrive\\Desktop\\bits new research\\dataset\\dataset\\organized_screenshots\\Shopping",
    "C:\\Users\\paray\\OneDrive\\Desktop\\bits new research\\dataset\\dataset\\organized_screenshots\\Social",
    "C:\\Users\\paray\\OneDrive\\Desktop\\bits new research\\dataset\\dataset\\organized_screenshots\\Education"
]

# Iterate through each parent folder
for parent_folder in parent_folders:
    # Iterate through all images in the parent folder
    for image_name in os.listdir(parent_folder):
        # Construct the full path to the image
        image_path = os.path.join(parent_folder, image_name)
        
        # Extract the sub-label from the filename
        # Assuming the format is: <UUID>_<MainLabel>_<SubLabel>_<Timestamp>_<UUID>
        try:
            # Split the filename by underscores
            parts = image_name.split('_')
            
            # The sub-label is the third part (index 2)
            sub_label = parts[2]
            
            # Create the sub-label folder inside the parent folder
            sub_label_folder = os.path.join(parent_folder, sub_label)
            Path(sub_label_folder).mkdir(parents=True, exist_ok=True)
            
            # Move the image to the corresponding sub-label folder
            shutil.move(image_path, sub_label_folder)
            print(f"Moved {image_name} to {sub_label_folder}")
        except IndexError:
            print(f"Filename {image_name} does not match the expected format. Skipping.")

print("Further classification complete!")