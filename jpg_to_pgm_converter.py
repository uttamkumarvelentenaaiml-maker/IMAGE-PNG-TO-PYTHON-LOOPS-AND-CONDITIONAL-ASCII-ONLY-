from PIL import Image
import sys

def jpg_to_pgm(input_file, output_file):
    """Convert JPG image to PGM format.
    
    Args:
        input_file: Path to input JPG file
        output_file: Path to output PGM file
    """
    try:
        # Open the image
        img = Image.open(input_file)
        
        # Convert to grayscale
        img_gray = img.convert('L')
        
        # Save as PGM
        img_gray.save(output_file, format='PPM')
        
        print(f"Successfully converted {input_file} to {output_file}")
        print(f"Image size: {img_gray.width}x{img_gray.height}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Get filenames from command line or use defaults
    input_file = "C:\\Users\\uttam\\OneDrive\\Desktop\\Uttam_minor_final\\Jhumpa_lahiri_test_image.jpeg"
    output_file = "face3.pgm"
    
    jpg_to_pgm(input_file, output_file)