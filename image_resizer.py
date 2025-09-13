# Image Resizer Tool - Beginner Friendly Version
# This script resizes all images in a folder

import os
from PIL import Image

def resize_single_image(input_path, output_path, new_width, new_height):
    """
    This function takes one image and resizes it
    
    input_path: where the original image is
    output_path: where to save the resized image
    new_width: how wide you want the new image
    new_height: how tall you want the new image
    """
    try:
        # Open the image file
        print(f"Opening image: {input_path}")
        image = Image.open(input_path)
        
        # Show original size
        original_width, original_height = image.size
        print(f"Original size: {original_width} x {original_height}")
        
        # Resize the image (this keeps the aspect ratio)
        image.thumbnail((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Show new size
        final_width, final_height = image.size
        print(f"New size: {final_width} x {final_height}")
        
        # Save the resized image
        image.save(output_path)
        print(f"Saved resized image to: {output_path}")
        
        return True
        
    except Exception as error:
        print(f"ERROR: Could not process {input_path}")
        print(f"Error message: {error}")
        return False

def find_image_files(folder_path):
    """
    This function finds all image files in a folder
    """
    # These are the image file types we can work with
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    
    image_files = []
    
    # Look through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file ends with an image extension
        file_lower = filename.lower()
        for extension in image_extensions:
            if file_lower.endswith(extension):
                image_files.append(filename)
                break
    
    return image_files

def resize_all_images():
    """
    Main function that resizes all images
    """
    print("=== IMAGE RESIZER TOOL ===")
    print()
    
    # Get information from the user
    print("Please provide the following information:")
    print()
    
    # Ask for input folder
    input_folder = input("Enter the path to your input folder (where your images are): ")
    
    # Ask for output folder  
    output_folder = input("Enter the path to your output folder (where resized images will go): ")
    
    # Ask for new dimensions
    try:
        new_width = int(input("Enter the maximum width you want (in pixels): "))
        new_height = int(input("Enter the maximum height you want (in pixels): "))
    except ValueError:
        print("ERROR: Please enter numbers only for width and height!")
        return
    
    print()
    print("Starting to resize images...")
    print("-" * 50)
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"ERROR: Input folder '{input_folder}' does not exist!")
        return
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")
    
    # Find all image files
    image_files = find_image_files(input_folder)
    
    if len(image_files) == 0:
        print("No image files found in the input folder!")
        print("Supported formats: JPG, JPEG, PNG, BMP, GIF, TIFF")
        return
    
    print(f"Found {len(image_files)} image files to resize")
    print()
    
    # Keep track of results
    successful_resizes = 0
    failed_resizes = 0
    
    # Process each image file
    for i, filename in enumerate(image_files, 1):
        print(f"Processing image {i} of {len(image_files)}: {filename}")
        
        # Create full paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Resize the image
        success = resize_single_image(input_path, output_path, new_width, new_height)
        
        if success:
            successful_resizes += 1
        else:
            failed_resizes += 1
        
        print("-" * 30)
    
    # Show final results
    print()
    print("=== RESULTS ===")
    print(f"Successfully resized: {successful_resizes} images")
    print(f"Failed to resize: {failed_resizes} images")
    print(f"Output folder: {output_folder}")
    print()
    print("Done! Check your output folder for the resized images.")

# This is where the program starts running
if __name__ == "__main__":
    resize_all_images()