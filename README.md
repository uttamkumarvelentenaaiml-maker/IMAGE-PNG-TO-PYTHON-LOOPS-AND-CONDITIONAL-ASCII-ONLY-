Image to ASCII Art Using Python Loops and Conditionals

This project converts a PNG/JPG image into ASCII art using only Python loops and conditional statements — *with no external libraries for the ASCII logic*.

How It Works

1. Run `jpg_to_pgm_converter.py` to convert your image to a `.pgm` grayscale format.
2. Use `pgm_to_output_loops_conditional.py` to generate a Python script (`ascii_art_code.py`) that prints ASCII art.
3. Run `ascii_art_code.py` to see the ASCII art in your terminal.

Example


Files

- jpg_to_pgm_converter.py — Convert JPEG to PGM.
- pgm_to_output_loops_conditional.py — Generates the ASCII printing logic.
- ascii_art_code.py — The generated ASCII art script.
- face3.pgm, "Jhumpa_lahiri_test_image.jpeg" — Sample files.

Requirements

- Python 3.x
- PIL (for image → PGM conversion)

 License

MIT License
