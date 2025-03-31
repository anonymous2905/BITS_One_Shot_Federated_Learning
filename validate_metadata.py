import os
import json
from collections import Counter

# Absolute path to the screenshots directory
screenshots_dir = "C:\\Users\\KIIT\\arpita\\dataset\\screenshots\\"  # Correct path
json_file = "C:\\Users\\KIIT\\arpita\\dataset\\metadata_partial.json"  # Correct JSON file name

# Check if the JSON file exists
if not os.path.exists(json_file):
    print(f"File not found: {json_file}")
else:
    with open(json_file, "r") as f:
        data = json.load(f)

    # Initialize counters and structure for training data
    training_data = []
    label_counts = Counter()  # Counter to keep track of screenshot counts per label

    # Process each entry
    for entry in data:
        # Extract metadata fields (we will skip "Blurred Screenshot Path" and "Extracted Features Path")
        screenshot_filename = entry.get("Screenshot Path", "").split("\\")[-1]  # Get the filename only
        screenshot_path = os.path.join(screenshots_dir, screenshot_filename)  # Use the correct path
        activity_label = entry.get("Activity Label", "Unknown")
        
        # Check if screenshot exists
        if os.path.exists(screenshot_path):
            # Add valid data to training data
            training_data.append({
                "screenshot_path": screenshot_path,
                "label": activity_label
            })
            label_counts[activity_label] += 1  # Increment the count for the label
            print(f"Valid data found for {activity_label}: {screenshot_path}")
        else:
            print(f"File not found: {screenshot_path}")

    # Summary
    print("\nProcessing complete.")
    print(f"Total training data collected: {len(training_data)}")

    # Print the class labels and their counts
    print("\nClass Labels and Counts:")
    for label, count in label_counts.items():
        print(f"{label}: {count}")
