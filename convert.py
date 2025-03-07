import json
import os
import math

def gpl_to_json(gpl_file, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the output JSON file path
    json_file = os.path.join(output_folder, os.path.basename(gpl_file).replace(".gpl", ".json"))

    # Read the GPL file
    with open(gpl_file, 'r') as file:
        lines = file.readlines()

    # Extract colors
    colors = []
    for line in lines:
        if line.startswith("#") or line.strip() == "" or "GIMP Palette" in line:
            continue  # Skip comments and empty lines
        parts = line.split()
        if len(parts) < 3:
            continue  # Skip invalid lines

        try:
            r, g, b = map(int, parts[:3])  # Extract RGB values
            colors.append({
                "color": f"({r/255:.4f}, {g/255:.4f}, {b/255:.4f}, 1)",  # Convert to normalized RGBA
                "index": len(colors)
            })
        except ValueError:
            continue  # Skip lines that can't be converted

    # Calculate height and width
    width = 16  # Fixed width (columns)
    height = math.ceil(len(colors) / width)  # Calculate rows based on number of colors

    # Create JSON data
    json_data = {
        "colors": colors,
        "comment": "",  # Add an empty comment field
        "height": height,  # Number of rows
        "width": width  # Number of columns
    }

    # Save the JSON data
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=2)

    print(f"✅ Conversion complete! {gpl_file} → {json_file}")

# Find all .gpl files in the current directory
def find_gpl_files():
    return [file for file in os.listdir(".") if file.endswith(".gpl")]

if __name__ == "__main__":
    output_folder = "json_output"  # Folder to store JSON files
    gpl_files = find_gpl_files()

    if gpl_files:
        for gpl_file in gpl_files:
            gpl_to_json(gpl_file, output_folder)
    else:
        print("❌ No .gpl files found in the directory.")
