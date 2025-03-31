import os
import shutil
from pathlib import Path

# Define paths
screenshots_folder = "C:\\Users\\paray\\OneDrive\\Desktop\\bits new research\\dataset\\dataset\\screenshots"
output_folder = "C:\\Users\\paray\\OneDrive\\Desktop\\bits new research\\dataset\\dataset\\organized_screenshots"

# Create the output folder if it doesn't exist
Path(output_folder).mkdir(parents=True, exist_ok=True)

# Iterate through all images in the screenshots folder
for image_name in os.listdir(screenshots_folder):
    # Construct the full path to the image
    image_path = os.path.join(screenshots_folder, image_name)
    
    # Extract the label from the filename
    # Assuming the format is: <UUID>_<Label>_<Timestamp>_<UUID>
    try:
        # Split the filename by underscores
        parts = image_name.split('_')
        
        # The label is the second part (index 1)
        label = parts[1]
        
        # Create a folder for the label if it doesn't exist
        label_folder = os.path.join(output_folder, label)
        Path(label_folder).mkdir(parents=True, exist_ok=True)
        
        # Copy the image to the corresponding label folder
        shutil.copy(image_path, label_folder)
        print(f"Copied {image_name} to {label_folder}")
    except IndexError:
        print(f"Filename {image_name} does not match the expected format. Skipping.")

print("Organization complete!")