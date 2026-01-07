import sys

def read_pgm(filename):
    """Read a PGM file and return the image data."""
    with open(filename, 'rb') as f:
        # Read magic number
        magic = f.readline().decode('ascii').strip()
        
        # Skip comments
        while True:
            line = f.readline().decode('ascii')
            if not line.startswith('#'):
                break
        
        # Read dimensions
        width, height = map(int, line.split())
        
        # Read max gray value
        max_val = int(f.readline().decode('ascii').strip())
        
        # Read pixel data
        if magic == 'P2':  # ASCII format
            pixels = []
            for line in f:
                pixels.extend(map(int, line.split()))
        elif magic == 'P5':  # Binary format
            pixels = list(f.read())
        else:
            raise ValueError(f"Unsupported PGM format: {magic}")
        
        return width, height, max_val, pixels

def resize_for_terminal(width, height, max_width=80):
    """Calculate optimal size for terminal display."""
    aspect_ratio = height / width
    if width > max_width:
        new_width = max_width
        new_height = int(new_width * aspect_ratio * 0.5)
    else:
        new_width = width
        new_height = int(height * 0.5)
    return new_width, new_height

def pgm_to_ascii_array(filename, chars="@%#*+=-:. ", max_width=80):
    """Convert PGM image to 2D array of ASCII characters."""
    # Read the PGM file
    width, height, max_val, pixels = read_pgm(filename)
    
    # Calculate display size
    display_width, display_height = resize_for_terminal(width, height, max_width)
    
    # Calculate sampling steps
    x_step = width / display_width
    y_step = height / display_height
    
    # Convert to ASCII array
    ascii_array = []
    for y in range(display_height):
        row = []
        for x in range(display_width):
            # Sample pixel at this position
            src_x = int(x * x_step)
            src_y = int(y * y_step)
            pixel_index = src_y * width + src_x
            
            if pixel_index < len(pixels):
                pixel_val = pixels[pixel_index]
                intensity = pixel_val / max_val
                char_index = int(intensity * (len(chars) - 1))
                char_index = min(char_index, len(chars) - 1)
                row.append(chars[char_index])
            else:
                row.append(' ')
        ascii_array.append(row)
    
    return ascii_array

def generate_if_else_code(ascii_array, output_file="ascii_art_code.py"):
    """Generate Python code using if-else statements to print ASCII art."""
    
    height = len(ascii_array)
    width = len(ascii_array[0]) if height > 0 else 0
    
    code = []
    code.append("def print_ascii_art(x, y):")
    code.append("    \"\"\"Print ASCII character at position (x, y).\"\"\"")
    
    # Generate nested if-else for each position
    for y in range(height):
        if y == 0:
            code.append(f"    if y == {y}:")
        else:
            code.append(f"    elif y == {y}:")
        
        for x in range(width):
            char = ascii_array[y][x]
            # Escape special characters
            if char == '\\':
                char = '\\\\'
            elif char == "'":
                char = "\\'"
            
            if x == 0:
                code.append(f"        if x == {x}:")
            else:
                code.append(f"        elif x == {x}:")
            code.append(f"            return '{char}'")
        
        code.append(f"        else:")
        code.append(f"            return ' '")
    
    code.append("    else:")
    code.append("        return ' '")
    code.append("")
    code.append("")
    code.append("def display_ascii_art():")
    code.append("    \"\"\"Display the complete ASCII art.\"\"\"")
    code.append(f"    for y in range({height}):")
    code.append(f"        for x in range({width}):")
    code.append("            print(print_ascii_art(x, y), end='')")
    code.append("        print()  # New line")
    code.append("")
    code.append("")
    code.append("if __name__ == '__main__':")
    code.append("    display_ascii_art()")
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write('\n'.join(code))
    
    return '\n'.join(code)

if __name__ == "__main__":
    # Get filename from command line or use default
    input_file = sys.argv[1] if len(sys.argv) > 1 else "face3.pgm"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "ascii_art_code.py"
    max_width = int(sys.argv[3]) if len(sys.argv) > 3 else 80
    
    try:
        print(f"Converting {input_file} to ASCII art code...")
        
        # Convert image to ASCII array
        ascii_array = pgm_to_ascii_array(input_file, max_width=max_width)
        
        # Generate code with if-else statements
        code = generate_if_else_code(ascii_array, output_file)
        
        print(f"Successfully generated {output_file}")
        print(f"Image size: {len(ascii_array[0])}x{len(ascii_array)} characters")
        print(f"\nTo run the generated code:")
        print(f"  python {output_file}")
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")