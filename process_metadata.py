import os
import json

# Step 1: Load JSON data
# Replace 'metadata_partial.json' with the actual path to your JSON file
json_file = "metadata_partial.json"

# Open and read the JSON file
with open(json_file, "r") as f:
    data = json.load(f)

# Initialize counters for summary
total_labels_processed = 0
total_files_found = 0
total_files_missing = 0
screenshot_count_by_label = {}

# Step 2: Process each entry in the JSON data
for entry in data:
    # Extract metadata fields
    screenshot_path = os.path.normpath(entry.get("Screenshot Path", ""))
    blurred_path = os.path.normpath(entry.get("Blurred Screenshot Path", ""))
    features_path = os.path.normpath(entry.get("Extracted Features Path", ""))
    activity_label = entry.get("Activity Label", "Unknown")

    # Update label counter
    screenshot_count_by_label[activity_label] = screenshot_count_by_label.get(activity_label, 0) + 1

    # Display details for debugging
    print(f"Processing label: {activity_label}")
    print(f"Screenshot Path: {screenshot_path}")
    print(f"Blurred Screenshot Path: {blurred_path}")
    print(f"Extracted Features Path: {features_path}")
    
    # Check if screenshot file exists
    if os.path.exists(screenshot_path):
        print(f"File exists: {screenshot_path}")
        total_files_found += 1
    else:
        print(f"File not found: {screenshot_path}")
        total_files_missing += 1

    total_labels_processed += 1

# Step 3: Display Summary
print("\nProcessing complete.")
print(f"Total Labels Processed: {total_labels_processed}")
print(f"Total Files Found: {total_files_found}")
print(f"Total Files Missing: {total_files_missing}")
print("\nScreenshot counts per label:")

# Display screenshot counts per label
for label, count in screenshot_count_by_label.items():
    print(f"{label}: {count}")
