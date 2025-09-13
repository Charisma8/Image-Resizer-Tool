 Image Resizer Tool - Task 7


A Python script that automatically resizes all images in a folder using Pillow library. Built as part of internship training to learn file handling, image processing, and batch operations.

##  Project Objective
Resize and convert images in batch using Python and Pillow library.

## 🛠 Technologies Used
- Python 3.x
- Pillow (PIL)- Image processing library
- OS module - File system operations

##  Project Structure

image-resizer/
├── image_resizer.py      # Main script
├── input_images/         # Source images folder
├── output_images/        # Processed images folder
└── README.md            # Project documentation


##  Features
- Batch resize all images in a folder
- Maintains aspect ratio 
- Supports multiple formats: JPG, PNG, BMP, GIF, TIFF
- Interactive user prompts
- Progress tracking and file size comparison
- Error handling for unsupported files

##  Installation & Usage

### Prerequisites

pip install Pillow


### Run the Script

python image_resizer.py


### Follow Interactive Prompts

Enter input folder: input_images
Enter output folder: output_images
Enter max width: 700
Enter max height: 500

## Output

Enter the path to your input folder (where your images are): input_images
Enter the path to your output folder (where resized images will go): output_images
Enter the maximum width you want (in pixels): 700
Enter the maximum height you want (in pixels): 500

Starting to resize images...
--------------------------------------------------
Found 4 image files to resize

Processing image 1 of 4: WhatsApp Image 2025-09-13 at 8.43.24 PM (1).jpeg
Opening image: input_images\WhatsApp Image 2025-09-13 at 8.43.24 PM (1).jpeg
Original size: 576 x 288
New size: 576 x 288
Saved resized image to: output_images\WhatsApp Image 2025-09-13 at 8.43.24 PM (1).jpeg
------------------------------
Processing image 2 of 4: WhatsApp Image 2025-09-13 at 8.43.24 PM.jpeg
Opening image: input_images\WhatsApp Image 2025-09-13 at 8.43.24 PM.jpeg
Original size: 284 x 178
New size: 284 x 178
Saved resized image to: output_images\WhatsApp Image 2025-09-13 at 8.43.24 PM.jpeg
------------------------------
Processing image 3 of 4: WhatsApp Image 2025-09-13 at 8.43.25 PM (1).jpeg
Opening image: input_images\WhatsApp Image 2025-09-13 at 8.43.25 PM (1).jpeg
Original size: 576 x 321
New size: 576 x 321
Saved resized image to: output_images\WhatsApp Image 2025-09-13 at 8.43.25 PM (1).jpeg
------------------------------
Processing image 4 of 4: WhatsApp Image 2025-09-13 at 8.43.25 PM.jpeg
Opening image: input_images\WhatsApp Image 2025-09-13 at 8.43.25 PM.jpeg
Original size: 452 x 678
New size: 333 x 500
Saved resized image to: output_images\WhatsApp Image 2025-09-13 at 8.43.25 PM.jpeg
------------------------------

=== RESULTS ===
Successfully resized: 4 images
Failed to resize: 0 images
Output folder: output_images

Done! Check your output folder for the resized images.



##  Key Learning Outcomes
- File I/O operations with `os` module
- Image processing using Pillow library
- Batch processing implementation
- Error handling and user input validation
- Aspect ratio calculations and preservation

## 💡 Use Cases
- Web image optimization
- Thumbnail generation
- Social media image preparation
- Storage space optimization


