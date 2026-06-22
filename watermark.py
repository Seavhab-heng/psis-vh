from PIL import Image
import os

# Configuration
input_folder = 'input'
output_folder = 'output'
watermark_path = 'watermark.png'

# Validate inputs
if not os.path.exists(input_folder):
    print(f"Error: '{input_folder}/' folder not found")
    print("Please create an 'input/' folder and add PNG/JPG images to process")
    exit(1)

if not os.path.exists(watermark_path):
    print(f"Error: '{watermark_path}' not found in project root")
    exit(1)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

watermark = Image.open(watermark_path).convert("RGBA")

images = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
if not images:
    print(f"No images found in '{input_folder}/' folder")
    exit(1)

for filename in images:
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        base_image = Image.open(os.path.join(input_folder, filename)).convert("RGBA")
        
        # Position watermark at bottom-right
        width, height = base_image.size
        watermark_width, watermark_height = watermark.size
        position = (width - watermark_width - 10, height - watermark_height - 10)
        
        # Overlay
        transparent = Image.new('RGBA', base_image.size, (0,0,0,0))
        transparent.paste(base_image, (0,0))
        transparent.paste(watermark, position, mask=watermark)
        
        # Save
        transparent.convert("RGB").save(os.path.join(output_folder, filename), "JPEG")
        print(f"Processed: {filename}")