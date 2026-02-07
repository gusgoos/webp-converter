import os
from PIL import Image

def convert_webp_to_jpg(webp_path, jpg_path):
    # Open the WebP image
    webp_image = Image.open(webp_path)

    # Save the image as JPG
    webp_image.convert("RGB").save(jpg_path, "JPEG")

def explore_directory(directory_path):
    # Get the current script directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Create the full path to the "files" subdirectory
    files_directory = os.path.join(script_directory, directory_path)

    # Check if the "files" directory exists
    if os.path.exists(files_directory):
        # Iterate through all files in the "files" directory
        for filename in os.listdir(files_directory):
            file_path = os.path.join(files_directory, filename)

            # Check if the file is a WebP image
            if filename.lower().endswith(".webp"):
                # Create a corresponding JPG filename
                jpg_filename = os.path.splitext(filename)[0] + ".png"
                jpg_path = os.path.join(files_directory, jpg_filename)

                # Convert WebP to JPG
                convert_webp_to_jpg(file_path, jpg_path)
        
        print("Conversion completed.")
    else:
        print("Directory not found.")

if __name__ == "__main__":
    # Specify the subdirectory containing WebP images
    webp_directory = 'files'

    # Explore the specified directory and convert WebP to JPG
    explore_directory(webp_directory)
