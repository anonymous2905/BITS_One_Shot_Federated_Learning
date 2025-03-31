import os
import cv2
import numpy as np
from skimage.feature import hog
from skimage import exposure
import json
from collections import defaultdict

# Constants
SAVE_PATH = "dataset"
ANONYMIZED_PATH = os.path.join(SAVE_PATH, "anonymized_screenshots")
FEATURES_PATH = os.path.join(SAVE_PATH, "features")
SCREENSHOTS_PATH = os.path.join(SAVE_PATH, "screenshots")

# Function to blur sensitive information
def blur_sensitive_info(image_path, output_path):
    image = cv2.imread(image_path)
    if image is not None:
        # Example coordinates for blurring (you may need to adjust these)
        height, width = image.shape[:2]

        # Define areas to blur (these are just example coordinates)
        cv2.rectangle(image, (0, 0), (width // 2, height // 10), (0, 0, 0), -1)  # Black rectangle for name
        cv2.rectangle(image, (0, height // 10), (width // 2, height // 5), (0, 0, 0), -1)  # Black rectangle for location

        blurred = cv2.GaussianBlur(image, (25, 25), 0)
        cv2.imwrite(output_path, blurred)

# Function to extract features using HOG
def extract_features(image_path, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is not None:
        features, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8),
                                   cells_per_block=(2, 2), visualize=True)
        np.save(output_path, features)

        # Optionally, save the HOG image for visualization
        hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
        hog_image_path = output_path.replace(".npy", "_hog.png")
        cv2.imwrite(hog_image_path, hog_image_rescaled * 255)

# Main function to process existing screenshots
def process_existing_screenshots():
    # Load metadata to get the paths of the screenshots
    metadata_path = os.path.join(os.getcwd(), "metadata_partial.json")
    with open(metadata_path, "r") as f:
        metadata = json.load(f)

    # Debugging output to check loaded metadata
    print("Loaded metadata entries:")
    for entry in metadata:
        print(entry)

    # Initialize a dictionary to hold counts for each label
    label_count = defaultdict(int)

    for entry in metadata:
        screenshot_path = entry.get("Screenshot Path")
        label = entry.get("Activity Label", "Unknown")
        
        # Debugging output for labels
        print(f"Processing label: {label}")

        if screenshot_path and os.path.exists(screenshot_path):
            # Create paths for anonymized and feature files
            anonymized_path = screenshot_path.replace("/screenshots/", "/anonymized_screenshots/")
            feature_path = screenshot_path.replace("/screenshots/", "/features/").replace(".png", ".npy")

            # Blur the screenshot and extract features
            blur_sensitive_info(screenshot_path, anonymized_path)
            extract_features(screenshot_path, feature_path)

            # Update the label count
            label_count[label] += 1

            # Debugging output to check the current count
            print(f"Updated count for label '{label}': {label_count[label]}")

            print(f"Processed: {screenshot_path}")
        else:
            print(f"File not found: {screenshot_path}")

    # Print the count of screenshots for each label
    print("\nScreenshot counts per label:")
    for label, count in label_count.items():
        print(f"{label}: {count}")

    # Return the label count for further use
    return label_count

# Run the processing
if __name__ == "__main__":
    label_count = process_existing_screenshots()

    # Print the total number of screenshots processed
    print("\nFinal Summary:")
    print(f"Total Labels Processed: {len(label_count)}")
    total_screenshots = sum(label_count.values())
    print(f"Total Screenshots Processed: {total_screenshots}")

    # Print label-specific counts
    print("Screenshots per label:")
    for label, count in label_count.items():
        print(f"{label}: {count}")
