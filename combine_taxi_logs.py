import os
import csv
import random

# 🔧 Path to folder and output CSV
folder_path = "D:/Research/Papers/repo/IEEE_SubResizeUsingAIForFleetVehicles/data/taxi_log_2008_by_id"
output_csv = "D:/Research/Papers/repo/IEEE_SubResizeUsingAIForFleetVehicles/data/taxi_data_merged.csv"

# Get all .txt files in the folder
all_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

# 🔢 Select 500 files randomly (or fewer if <500 available)
sample_files = random.sample(all_files, min(500, len(all_files)))

# Write to output CSV
with open(output_csv, mode="w", newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(["taxiid", "timestamp", "longitude", "latitude"])  # Header

    # Loop through the 500 sampled text files
    for filename in sample_files:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as txt_file:
            for line in txt_file:
                line = line.strip()
                if line:  # Skip empty lines
                    fields = line.split(",")  # Adjust if not comma-separated
                    if len(fields) == 4:
                        writer.writerow(fields)