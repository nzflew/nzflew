import os
import json
import xml.etree.ElementTree as ET

# Set the base directory (where all Sublime snippets are stored)
BASE_INPUT_DIR = r"C:\Users\MarkFlewellen\AppData\Roaming\Sublime Text\Packages\User\Snippets"

# Set the base output directory (where VS Code snippets will be saved)
BASE_OUTPUT_DIR = os.path.join(BASE_INPUT_DIR, "converted_vscode_snippets")
os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)  # Ensure the base output directory exists

# Function to convert a Sublime snippet to VS Code format
def convert_sublime_to_vscode(snippet_file):
    try:
        tree = ET.parse(snippet_file)
        root = tree.getroot()

        # Extract values from XML
        content = root.find("content").text.strip() if root.find("content") is not None else ""
        tab_trigger_element = root.find("tabTrigger")
        description_element = root.find("description")

        # If tabTrigger is missing, use the filename instead
        filename = os.path.splitext(os.path.basename(snippet_file))[0]
        tab_trigger = tab_trigger_element.text.strip() if tab_trigger_element is not None else filename
        description = description_element.text.strip() if description_element is not None else filename

        # Format the snippet body (split by lines)
        body = content.split("\n")

        return {
            description: {
                "prefix": tab_trigger,
                "body": body,
                "description": description
            }
        }
    except Exception as e:
        print(f"❌ Error converting {snippet_file}: {e}")
        return None

# Walk through all subdirectories to find and process Sublime snippets
for root_dir, _, files in os.walk(BASE_INPUT_DIR):
    for filename in files:
        if filename.endswith(".sublime-snippet"):
            filepath = os.path.join(root_dir, filename)

            # Convert the snippet
            snippet_data = convert_sublime_to_vscode(filepath)
            if snippet_data:
                # Maintain subdirectory structure in the output folder
                relative_path = os.path.relpath(root_dir, BASE_INPUT_DIR)
                output_dir = os.path.join(BASE_OUTPUT_DIR, relative_path)
                os.makedirs(output_dir, exist_ok=True)  # Ensure the subdirectory exists

                # Create output file path
                output_filename = os.path.splitext(filename)[0] + ".code-snippets"
                output_filepath = os.path.join(output_dir, output_filename)

                # Save as individual JSON file
                with open(output_filepath, "w", encoding="utf-8") as f:
                    json.dump(snippet_data, f, indent=4)

                print(f"✅ Converted: {filepath} → {output_filepath}")

print(f"\n🎉 Conversion complete! All VS Code snippets are in: {BASE_OUTPUT_DIR}")
