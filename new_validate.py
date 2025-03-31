import json
import os
from collections import Counter
import cv2

# Path to the metadata file and screenshots directory
metadata_file = r"C:\Users\KIIT\arpita\dataset\metadata_partial.json"
screenshots_dir = r"C:\Users\KIIT\arpita\dataset\screenshots"

# Function to load metadata and inspect structure
def load_metadata(metadata_file):
    with open(metadata_file, "r") as f:
        metadata = json.load(f)
    return metadata

# Load and inspect metadata
metadata = load_metadata(metadata_file)

# Function to process screenshots and their labels
def process_data(metadata, screenshots_dir):
    label_counts = Counter()  # To store counts for each label

    for entry in metadata:
        # Check if the screenshot file exists and label key is present
        try:
            screenshot_filename = entry["filename"]
            label = entry.get("label")  # Change "label" to the correct key if needed

            if label is None:
                continue  # Skip if label is missing

            # Skip images that are blurred or anonymized
            if "blurred" in screenshot_filename or "anonymized" in screenshot_filename:
                continue

            screenshot_path = os.path.join(screenshots_dir, screenshot_filename)
            
            if os.path.exists(screenshot_path):
                label_counts[label] += 1  # Count the label for valid screenshots
            else:
                print(f"File not found: {screenshot_path}")
        
        except KeyError as e:
            print(f"KeyError: {e} in entry: {entry}")

    return label_counts

# Process the metadata and screenshots to collect label counts
label_counts = process_data(metadata, screenshots_dir)

# Print out the total number of training samples collected
print(f"\nTotal training data collected: {sum(label_counts.values())}")

# Print the class labels and their counts
print("\nClass Labels and Counts:")
for label, count in label_counts.items():
    print(f"{label}: {count}")
