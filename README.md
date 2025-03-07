# GPL to JSON Converter

## Overview
This Python script converts `.gpl` (GIMP Palette) files into JSON format. It extracts RGB color values, normalizes them, and structures them into a JSON object with metadata such as width and height.

## Features
- Automatically detects `.gpl` files in the current directory.
- Converts color values to normalized RGBA format.
- Saves the output JSON files in a dedicated folder (`json_output`).
- Skips invalid or comment lines in `.gpl` files.

## Installation
No additional dependencies are required. This script runs with standard Python libraries.

## Usage
1. Place your `.gpl` files in the script's directory.
2. Run the script:
   ```bash
   python script.py
   ```
3. Converted JSON files will be saved in the `json_output` folder.

## JSON Structure
Each generated JSON file follows this format:
```json
{
  "colors": [
    { "color": "(0.1234, 0.5678, 0.9101, 1)", "index": 0 },
    { "color": "(0.2345, 0.6789, 0.1011, 1)", "index": 1 }
  ],
  "comment": "",
  "height": X,
  "width": 16
}
```

## Notes
- The script assumes a fixed width of `16` colors per row.
- If no `.gpl` files are found, it will display an error message.

## License
This script is released under the MIT License.

